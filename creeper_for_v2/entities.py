from dataclasses import dataclass
@dataclass
class Attributes:
    desc: str
    x:int
    y:int


class Coord(Enum):
    ## SECTION XML

    GENERAL_CLOSE = Attributes("Button to close everithing", 1232, 181)

    SECTION_XML = Attributes("section xml", 731,245)
    XML_SELECT_FILE_BTN = Attributes("Button for select file for XML", 1162,304)
    TMP_SELECT_FILE_BTN = Attributes("Button to select the file .tmp", 1166, 358)
    ENCRYPT_BTN = Attributes("Button to encrypt the file", 716,397)
    DECRYPT_BTN = Attributes("Button to decrypt the .tmp", 822,397)
    ECU_INFORMATION_BTN = Attributes("Button to open dialog with ecu Information", 943, 397)
    CLIENT_ID_INPUT = Attributes("Input to write client ID", 674,446)
    DEALER_ID_INPUT = Attributes("Input to write dealer ID", 782,447)
    GET_MDB_IDS_BUTTON = Attributes("Button to get ids from database", 935, 446)
    DATE_INPUT_FIELD = Attributes("The date ", 1121, 445)

    ## BOX ECU INFORMATION
    BOX_ECU_INFO_INIT = Attributes("", 745,314)
    BOX_ECU_INFO_FINAL = Attributes("", 1176,761)
    SAVE_INFO_INTO_FILE = Attributes("button inside that store a txt into desktop", 820, 744)
    CLOSE_ECU_INFO_BOX = Attributes("Button to close the dialog of ecu information", 1156, 328)

    ## Dialog to select file
    SEARCH_DIRECTORY_INPUT = Attributes("The input box to search the main", 1550,59)
    FILENAME_INPUT = Attributes("The input box to write the file name of the input", 1695, 951)
    SAVE_BTN = Attributes("Button that confirms the file to load into ", 1713, 1040)
    CANCEL_BTN = Attributes("Button that cancel the select file dialog ", 1838, 1037)
    CLOSE_SELECT_FILE_BTN = Attributes("Buttton that closes everything", 1882, 21)

    ## intersto treatment
    INSERSTO_SECTION_TAB = Attributes("The tab to click to enter into Intersto Section", 865,245)
    SELECT_MDB_BTN = Attributes("The button that opens the file selection ", 1236, 306)
    LOAD_INFO_BTN = Attributes("Button that loads information of DB into the fields", 743, 348)
    SAVE_UPDATE_BTN = Attributes("Button that saves or update info of fields into DB", 860, 342)
    COPY_PASS_CLIP_BTN = Attributes("Button that copy the password of db into clipboard", 1115, 345)

    MDB_CLIENT_ID_FIELD = Attributes("Input to write client id ", 806, 507)
    MDB_DEALER_ID_FIELD = Attributes("Input to write dealer id", 921, 508)
    MDB_USER_ID_FIELD = Attributes("Input to write user id", 1161, 510)
    ## NEEDS TO BE ERASED CAUSE ITS LOADED WITH THE CURRENT AL least need to update the year
    MDB_DATE_RECEIVED_FIELD = Attributes("Input to write DATE RECEIVED IN FORMAT dd/mm/yyyy that is usually higger that localDate", 887, 680)
    ## NEEDS TO BE ERASED CAUSE ITS LOADED WITH THE CURRENT AL least need to update the year leave as it its when the path is correct, also needs to be erased
    MDB_XML_LOCATION_FIELD = Attributes("Input to write the location of XML file", 1240, 728)

    @property
    def desc(self):
        return self.value.desc
    
    @property
    def x(self):
        return self.value.x
    
    @property
    def y(self):
        return self.value.y