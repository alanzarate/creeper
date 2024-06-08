import os 
import subprocess
import time

from constants import VISFED_PATH
import xml_encrypt as xmlEnc

from enum import Enum
## IMPORTANT CONSTANTS



try:
    process = subprocess.Popen(VISFED_PATH)
    #process.wait() ## KEEPS IN THE BOX
    xmlEnc.init()
    process.terminate()
    process.wait()
except KeyboardInterrupt:
    process.terminate()
    process.wait()
except Exception as e:
    print(f"An error occurred: {e}")

 