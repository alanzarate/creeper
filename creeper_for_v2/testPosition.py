import pyautogui as pa
import time
import pathlib
import os
def def1():
    try:
        #size of screen
        width, height = pa.size()
        print(width, height)
        while True:
            x, y = pa.position()
            positionStr = 'X: ' + str(x).rjust(4) + '  Y:' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print("END OF ===") 

def def2():
    pa.moveTo(903, 91 , duration=5)
    pa.click()

def def3():
    try:
        path = r'C:\Users\PcPotato\Desktop\Visfed\FolderToTestFiles\MAMAMIA.xml'
        os.remove(path=path)
    except FileNotFoundError as e:
        print('No se encuentra UE')

def1()