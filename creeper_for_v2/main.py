import os 
import subprocess
import time

from creeper_for_v2.constants import VISFED_PATH
import creeper_for_v2.xml_encrypt as xmlEnc

 
## IMPORTANT CONSTANTS

def main2(intructions):
    print(intructions)
 
def main(intructions):
    try:
        process = subprocess.Popen(VISFED_PATH)
        #process.wait() ## KEEPS IN THE BOX
     
        
        time.sleep(2)
        xmlEnc.init(intructions)
        process.terminate()
        process.wait()
    except KeyboardInterrupt:
        process.terminate()
        process.wait()
    except Exception as e:
        process.terminate()
        process.wait()
        print(f"An error occurred: {e}")

    