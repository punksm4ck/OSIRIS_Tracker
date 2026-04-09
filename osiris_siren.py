"© 2026 Punksm4ck. All rights reserved."
import os
import time
import subprocess

AIRTAG_MAC = "REPLACE_WITH_AIRTAG_BT_ADDR" 

def trigger_siren():
    print(f"OSIRIS: Targeting AirTag at {AIRTAG_MAC}...")
    # This command uses gatttool to write to the 'Alert Level' characteristic
    # '02' is the hex code for 'High Alert' (Ringing)
    cmd = f"gatttool -b {AIRTAG_MAC} --char-write-req --handle=0x0032 --value=02"
    
    try:
        subprocess.run(cmd.split(), check=True)
        print("Siren Command Dispatched Successfully.")
    except Exception as e:
        print(f"Siren Failed: {e}")

if __name__ == "__main__":
    trigger_siren()
