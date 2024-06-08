import json
import pyautogui as pa
import os
from entities import Coord, Attributes 
import shutil
import time
 


def moveAndClick(x, y, duration = 0):
    #pa.moveTo(x, y, duration)
    pa.click(x = x, y = y, )

def moveAndDoubleClick(x, y, duration = 0):
    pa.doubleClick(x = x, y = y)

def moveClickAndWrite(x, y, string = "", duration = 0):
    pa.click(x = x , y = y)
    pa.write(string, interval = 0.01)

def selectFromFiles(coord1, coord2, path, fileStr):
    moveClickAndWrite(
            x = coord1.x,
            y = coord2.y,
            string = path
        )
    pa.press('enter')

    moveClickAndWrite(
        x = coord2.x,
        y = coord2.y,
        string = fileStr
    )
    pa.press('enter')


def init():
    json_file_path = "actions.json"
    with open(json_file_path, 'r') as json_file:
        data_dict = json.load(json_file)

    if data_dict['action'] == "ENCRYPT":
        ## is to encrypt xmlfile
        filename = data_dict['fileName']
        path_tmp = data_dict['routeTmp']
        xml_name = data_dict['xmlName']

        xmp_path = f"{os.getcwd()}\\input\\{xml_name}"

        ## copy the xml that is in input to output also copy the mdb 

        shutil.copyfile( f"{os.getcwd()}\\input\\{xml_name}", f"{os.getcwd()}\\output\\{data_dict['fileName']}\\.xml")
        shutil.copyfile(f"{os.getcwd()}\\constant_files\\intersto.mdb", f"{os.getcwd()}\\output\\intersto.mdb")

        ## end of copy
        moveAndClick(
            x = Coord.XML_SELECT_FILE_BTN.x,
            y = Coord.XML_SELECT_FILE_BTN.y )
        

        selectFromFiles(coord1 = Coord.SEARCH_DIRECTORY_INPUT, 
                        coord2 =  Coord.FILENAME_INPUT,
                        path = f"{os.getcwd()}\\output", 
                        fileStr = f"{data_dict['newXmlFileName']}" )

        
        
        #load database
        moveAndClick(
            x = Coord.INSERSTO_SECTION_TAB.x,
            y = Coord.INSERSTO_SECTION_TAB.y )

        moveAndClick(
            x = Coord.INSERSTO_SECTION_TAB.x,
            y = Coord.INSERSTO_SECTION_TAB.y )

        selectFromFiles(coord1 = Coord.SEARCH_DIRECTORY_INPUT, 
                        coord2 =  Coord.FILENAME_INPUT,
                        path = f"{os.getcwd()}\\output", 
                        fileStr = "intersto.mdb" )
        
        moveClickAndWrite(
        x = Coord.MDB_CLIENT_ID_FIELD.x , 
        y = Coord.MDB_CLIENT_ID_FIELD.y, 
        string = data_dict['clientId'],
        )

        moveClickAndWrite(
        x = Coord.MDB_DEALER_ID_FIELD.x , 
        y = Coord.MDB_DEALER_ID_FIELD.y, 
        string = data_dict['dealerId'],
        )
        moveClickAndWrite(
        x = Coord.MDB_USER_ID_FIELD.x , 
        y = Coord.MDB_USER_ID_FIELD.y, 
        string = data_dict['userId'],
        )

        moveAndDoubleClick(x = Coord.MDB_DATE_RECEIVED_FIELD.x, 
        y  = Coord.MDB_DATE_RECEIVED_FIELD.y)

        #pa.press('backspace')
        pa.write(f"{data_dict['month']}/{data_dict['day']}/{data_dict['year']}")

        moveAndClick(
            x = Coord.MDB_XML_LOCATION_FIELD.x,
            y = Coord.MDB_XML_LOCATION_FIELD.y )
        
        for i in range(13):
            pa.doubleClick()
            pa.press('backspace')
        pa.write(data_dict['routeTmp'])

        moveAndClick(
            x = Coord.SAVE_UPDATE_BTN.x,
            y = Coord.SAVE_UPDATE_BTN.y )
        time.sleep(1.5)

        # back to xml section
        moveAndClick(
            x = Coord.SECTION_XML.x,
            y = Coord.SECTION_XML.y )
        
        moveClickAndWrite(
        x = Coord.CLIENT_ID_INPUT.x , 
        y = Coord.CLIENT_ID_INPUT.y, 
        string = data_dict['clientId'],
        )

        moveClickAndWrite(
        x = Coord.DEALER_ID_INPUT.x , 
        y = Coord.DEALER_ID_INPUT.y, 
        string = data_dict['dealerId'],
        )


        moveAndClick(
            x = Coord.DATE_INPUT_FIELD.x,
            y = Coord.DATE_INPUT_FIELD.y )
        
        for i in range(13):
            pa.doubleClick()
            pa.press('backspace')

        pa.write(f"{data_dict['year']}-{data_dict['month']}-{data_dict['day']}")

        #encrypt
        moveAndClick(
            x = Coord.ENCRYPT_BTN.x,
            y = Coord.ENCRYPT_BTN.y )
        time.sleep(1.5)

        


        
    

        
   

    



    