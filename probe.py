import os
from findmy import AppleAccount
from findmy.reports import RemoteAnisetteProvider

APPLE_ID = "tsannasardo@gmail.com"
APPLE_PASS = "S4l4db4r2040!"

anisette = RemoteAnisetteProvider("http://127.0.0.1:6969")
account = AppleAccount(anisette)
account.login(APPLE_ID, APPLE_PASS)

print("\n--- SURGICAL PROBE: APPLE ACCOUNT METHODS ---")
methods = [m for m in dir(account) if not m.startswith('_')]
for m in methods:
    print(m)
