import json
import pyautogui as pa
import os
from creeper_for_v2.entities import Coord, Attributes 
import shutil
import time

 


def moveAndClick(x, y, duration = 0):
    #pa.moveTo(x, y, durattion)
    pa.click(x = x, y = y, )

def moveAndDoubleClick(x, y, duration = 0):
    pa.doubleClick(x = x, y = y)

def moveClickAndWrite(x, y, string = "", duration = 0):
    pa.click(x = x , y = y)
    pa.write(string, interval = 0.01)

def selectFromFiles(coord1, coord2, path, fileStr):
    moveClickAndWrite(
            x = coord1.x,
            y = coord1.y,
            string = path
        )
    pa.press('enter')

    moveClickAndWrite(
        x = coord2.x,
        y = coord2.y,
        string = fileStr
    )
    pa.press('enter')




def aux(s):
    time.sleep(1)
    print("STEP ==== ", s)
     
def init(intructions):
     
    # json_file_path = "actions.json"
    # with open(json_file_path, 'r') as json_file:
    #     data_dict = json.load(json_file)
    # WHEN the instruictions is already in a map
    data_dict = intructions
    if data_dict['action'] == "ENCRYPT":
        ## is to encrypt xmlfile
        filename = data_dict['fileName']
        path_tmp = data_dict['routeTmp']
        xml_name = data_dict['xmlName']
        rootPath = os.getcwd()
        rootPath_creperV2 = rootPath + "\\creeper_for_v2"
        xmp_path = f"{rootPath_creperV2}\\input\\{xml_name}"

        if not os.path.exists(f"{rootPath_creperV2}\\output" ):
            os.makedirs(f"{rootPath_creperV2}\\output")
        ## copy the xml that is in input to output also copy the mdb 
        print("AQUI 1", xml_name)
        shutil.copy( f"{rootPath_creperV2}\\input\\{xml_name}", f"{rootPath_creperV2}\\output\\{data_dict['newXmlFileName']}")
        print("AQUI 2")
        shutil.copy(f"{rootPath_creperV2}\\constant_files\\intersto.mdb", f"{rootPath_creperV2}\\output\\intersto.mdb")
        print("AQUI 3")
        aux(1)
        ## end of copy
        moveAndClick(
            x = Coord.XML_SELECT_FILE_BTN.x,
            y = Coord.XML_SELECT_FILE_BTN.y )
        aux(2)

        selectFromFiles(coord1 = Coord.SEARCH_DIRECTORY_INPUT, 
                        coord2 =  Coord.FILENAME_INPUT,
                        path = f"{rootPath_creperV2}\\output", 
                        fileStr = f"{data_dict['newXmlFileName']}" )

        aux(3)
         
        #load database
        moveAndClick(
            x = Coord.INSERSTO_SECTION_TAB.x,
            y = Coord.INSERSTO_SECTION_TAB.y )
        aux(4)
        moveAndClick(
            x = Coord.SELECT_MDB_BTN.x,
            y = Coord.SELECT_MDB_BTN.y )
        aux(5)

        selectFromFiles(coord1 = Coord.SEARCH_DIRECTORY_INPUT, 
                        coord2 =  Coord.FILENAME_INPUT,
                        path = f"{rootPath_creperV2}\\output", 
                        fileStr = "intersto.mdb" )
        aux(6)
        moveClickAndWrite(
        x = Coord.MDB_CLIENT_ID_FIELD.x , 
        y = Coord.MDB_CLIENT_ID_FIELD.y, 
        string = data_dict['clientId'],
        )
        aux(7)
        moveClickAndWrite(
        x = Coord.MDB_DEALER_ID_FIELD.x , 
        y = Coord.MDB_DEALER_ID_FIELD.y, 
        string = data_dict['dealerId'],
        )
        aux(8)
        moveClickAndWrite(
        x = Coord.MDB_USER_ID_FIELD.x , 
        y = Coord.MDB_USER_ID_FIELD.y, 
        string = data_dict['userId'],
        )
        aux(9)

        moveAndDoubleClick(x = Coord.MDB_DATE_RECEIVED_FIELD.x, 
        y  = Coord.MDB_DATE_RECEIVED_FIELD.y)
        
        aux(10)
        #pa.press('backspace')
        pa.write(f"{data_dict['month']}/{data_dict['day']}/{data_dict['year']}")
        aux(11)
        moveAndClick(
            x = Coord.MDB_XML_LOCATION_FIELD.x,
            y = Coord.MDB_XML_LOCATION_FIELD.y )
        aux(12)
        for i in range(20):
            pa.doubleClick()
            time.sleep(0.1)
            pa.press('backspace')
            
        aux(13)    
        pa.write(data_dict['routeTmp'])
        aux(14)
        moveAndClick(
            x = Coord.SAVE_UPDATE_BTN.x,
            y = Coord.SAVE_UPDATE_BTN.y )
         
        aux(15)
        time.sleep(3)
        # back to xml section
        moveAndClick(
            x = Coord.SECTION_XML.x,
            y = Coord.SECTION_XML.y )
        aux(16)
        moveClickAndWrite(
        x = Coord.CLIENT_ID_INPUT.x , 
        y = Coord.CLIENT_ID_INPUT.y, 
        string = data_dict['clientId'],
        )
        aux(17)
        moveClickAndWrite(
        x = Coord.DEALER_ID_INPUT.x , 
        y = Coord.DEALER_ID_INPUT.y, 
        string = data_dict['dealerId'],
        )

        aux(18)
        moveAndClick(
            x = Coord.DATE_INPUT_FIELD.x,
            y = Coord.DATE_INPUT_FIELD.y )
        
        for i in range(50):
            pa.doubleClick()
            pa.press('backspace')
            time.sleep(0.01)
        aux(19)
        pa.write(f"{data_dict['year']}-{data_dict['month']}-{data_dict['day']}")
        aux(20)
        #encrypt
        moveAndClick(
            x = Coord.ENCRYPT_BTN.x,
            y = Coord.ENCRYPT_BTN.y )
        aux(21)
        time.sleep(1.5)

        


        
    

        
   

    



    