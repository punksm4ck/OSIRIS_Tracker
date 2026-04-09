"© 2026 Punksm4ck. All rights reserved."
import asyncio
import os
from datetime import datetime

from findmy import KeyPair
from findmy.reports import RemoteAnisetteProvider, AsyncAppleAccount, LoginState

PRIVATE_KEY_B64 = "RJCngObbHGXgWKen2okANJNAlHRskSFA="
APPLE_ID        = "tsannasardo@gmail.com"
APPLE_PASS      = "S4l4db4r2040!"
ANISETTE_URL    = "http://localhost:6969"
DATA_DIR        = "/home/tsann/Scripts/OSIRIS_Tracker"

async def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    log = f"{DATA_DIR}/history.csv"
    if not os.path.exists(log):
        open(log, "w").write("Timestamp,Latitude,Longitude\n")

    device   = KeyPair.from_b64(PRIVATE_KEY_B64)
    anisette = RemoteAnisetteProvider(ANISETTE_URL)
    acc      = AsyncAppleAccount(anisette)

    try:
        state = await acc.login(APPLE_ID, APPLE_PASS)
        print(f"Login state: {state}")

        if state == LoginState.REQUIRE_2FA:
            methods = await acc.get_2fa_methods()
            print("2FA methods available:")
            for i, m in enumerate(methods):
                print(f"  [{i}] {m}")
            choice = int(input("Choose method number: "))
            method = methods[choice]
            await method.request()
            code = input("Enter your 2FA code: ").strip()
            await method.submit(code)
            print("2FA accepted.")

        while True:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Querying Apple Find My network...")
            try:
                result = await acc.fetch_location(device)
                if result:
                    report = result if not isinstance(result, dict) else result.get(device)
                    if report:
                        lat, lon = report.lat, report.lon
                        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        open(f"{DATA_DIR}/latest_coord.txt", "w").write(f"{lat},{lon}")
                        open(log, "a").write(f"{ts},{lat},{lon}\n")
                        print(f"[OSIRIS] ✓ Location: {lat}, {lon}")
                        os.system(f'notify-send "OSIRIS Tracker" "Location: {lat}, {lon}"')
                    else:
                        print("[OSIRIS] No reports yet — tracker needs to pass near an iPhone.")
                else:
                    print("[OSIRIS] No reports yet.")

            except Exception as e:
                print(f"[OSIRIS] Error: {e}")
                open(f"{DATA_DIR}/error.log", "a").write(f"{datetime.now()}: {e}\n")

            print("Sleeping 5 min...\n")
            await asyncio.sleep(300)

    finally:
        await acc.close()

if __name__ == "__main__":
    asyncio.run(main())
