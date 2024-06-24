import requests
import os 

class Uploader:
    def __init__(self):
        pass

    def uploadCompleteFlashFile(self, routeXml:str, routeTmp:str, routeImage: str, data:dict ):
        xmlFile = None
        tmpFile = None
        imageFile = None
        if routeXml and os.path.exists(routeXml):
            with open(routeXml, 'rb') as file:
                xmlFile = file

        if routeTmp and os.path.exists(routeTmp):
            with open(routeTmp, 'rb') as file:
                tmpFile = file

        if routeImage and os.path.exists(routeImage):
            with open(routeImage, 'rb') as file:
                imageFile = file
        
        files = {
            'thumbnail': imageFile,
            'xmlFile': xmlFile,
            'tmpFile': tmpFile,
            'data': str(data)
        }

        response = requests.post(url = "http://localhost:8095/ms-file-mananger/v1/flashfile/v2", files = files)
        if response.status_code == 200:
            print("Files and JSON data uploaded successfully.")
        else:
            print(f"Failed to upload files and JSON data. Status code: {response.status_code}")
            print(response.text)



finalDATA = {'parameters':[{'code': '20995620', 'name': 'HardwareNo', 'value': ''}, {'code': '22991818', 'name': 'MSWNo', 'value': 'Engine'}, {'code': '22381211', 'name': 'Dataset1No', 'value': 'D13C500 EU2 VOLVO'}, {'code': '22894005', 'name': 'Dataset2No', 'value': 'TYPE-FH/FM EU2'}, {'code': '22373716', 'name': 'CSWNo', 'value': 'D13C500 EU2 VOLVO'}, {'code': '21488324', 'name': '', 'value': 'Manual gearboxes VOLVO (VT2514B/2814B)'}, {'code': '21302817', 'name': '', 'value': 'Fuel Filter: Sensor and Valve'}, {'code': '21302805', 'name': '', 'value': 'No start aid'}, {'code': '21312898', 'name': '', 'value': 'Emission OBD NOx Control, No Torque reduction'}, {'code': '21669422', 'name': '', 'value': 'Engine brake EBR-VEB+'}, {'code': '21302811', 'name': '', 'value': 'FAN TYPE FAN-VISE'}, {'code': '20763725', 'name': '', 'value': 'Extended engine protection'}, {'code': '21571523', 'name': '', 'value': 'Oil thermostat MD11COT'}, {'code': '21571516', 'name': '', 'value': 'PCJ EU5 500 hp'}, {'code': '22373734', 'name': '', 'value': 'AdBlue tank not available'}, {'code': '', 'name': 'isSWEqual', 'value': 'false'}, {'code': '', 'name': 'ChassisNo', 'value': '683748'}, {'code': '', 'name': 'GLOPPSNotRunning', 'value': 'false'}, {'code': '', 'name': 'Mid', 'value': '128'}, {'code': '', 'name': 'DSW', 'value': 'W0RTV0NvbnRlbnRdDQo6MDAwMDAwMDFGRg0K'}, {'code': '', 'name': 'ChassisSerie', 'value': 'B'}, {'code': '', 'name': 'CommercialDescription', 'value': 'Free of charge'}]}
finalData2= {'parameters':[{'code': '20995620', 'name': 'HardwareNo', 'value': ''}, {'code': '22991818', 'name': 'MSWNo', 'value': 'Engine'}, {'code': '22381211', 'name': 'Dataset1No', 'value': 'D13C500 EU2 VOLVO'}, {'code': '22894005', 'name': 'Dataset2No', 'value': 'TYPE-FH/FM EU2'}, {'code': '22373724', 'name': 'CSWNo', 'value': 'D13C500 EU2 VOLVO'}, {'code': '21488479', 'name': '', 'value': 'Gearbox AMT-D'}, {'code': '21302817', 'name': '', 'value': 'Fuel Filter: Sensor and Valve'}, {'code': '21302804', 'name': '', 'value': 'Electronic start aid 24 V'}, {'code': '21312898', 'name': '', 'value': 'Emission OBD NOx Control, No Torque reduction'}, {'code': '21354204', 'name': '', 'value': 'Engine brake EBR-VEB+'}, {'code': '21302811', 'name': '', 'value': 'FAN TYPE FAN-VISE'}, {'code': '20763725', 'name': '', 'value': 'Extended engine protection'}, {'code': '21571523', 'name': '', 'value': 'Oil thermostat MD11COT'}, {'code': '21571516', 'name': '', 'value': 'PCJ EU5 500 hp'}, {'code': '22373734', 'name': '', 'value': 'AdBlue tank not available'}, {'code': '', 'name': 'isSWEqual', 'value': 'false'}, {'code': '', 'name': 'ChassisNo', 'value': '702356'}, {'code': '', 'name': 'GLOPPSNotRunning', 'value': 'false'}, {'code': '', 'name': 'Mid', 'value': '128'}, {'code': '', 'name': 'DSW', 'value': 'W0RTV0NvbnRlbnRdDQo6MDAwMDAwMDFGRg0K'}, {'code': '', 'name': 'ChassisSerie', 'value': 'A'}, {'code': '', 'name': 'CommercialDescription', 'value': 'Free of charge'}]}
routeXML = './D415.tmp.xml'
routePNG = './pexels-garvin-st-villier-719266-3311574.jpg'

up = Uploader()
up.uploadCompleteFlashFile(routeXml= routeXML, routeTmp= None, routeImage=routePNG, data= finalDATA)