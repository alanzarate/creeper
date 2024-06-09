from minio import Minio
from minio.error import S3Error
import os
import json
import creeper_for_v2.main as mainV2

MINIO_URL = "192.168.100.28:9000"
ACCESS_KEY = "bUXfpLrKqeGxDAnTaC7z"
SECRET_KEY = "IJVnBbUwiM2kq2j9bz8vGADv16hOIzncyPs9iGlE"
BUCKET_WRITED = "creeper-output"

def uploadFilesToMinio(bucketName, objectsPath:list): # list of tuples
    minio_client = Minio(
        MINIO_URL,
        access_key = ACCESS_KEY,
        secret_key =  SECRET_KEY,
        secure = False
    )
    #chekck if the bucket exist
    found = minio_client.bucket_exists(bucketName)
    if not found:
        minio_client.make_bucket(bucketName)
    else:
        print("Bucket already exits")
    
    for filePathTuple in objectsPath:
        objectName = filePathTuple[0]
        filePath  = filePathTuple[1]
        try:
            minio_client.fput_object(bucketName, objectName, filePath )
            print(f"File '{filePath}' uploaded as '{objectName}'")
        except S3Error as err:
            print(f"Error occurred: {err}")


def downloadFromMinio(bucketName, objectName, destinyPath ):
    minio_client = Minio(
        MINIO_URL,
        access_key = ACCESS_KEY,
        secret_key =  SECRET_KEY,
        secure = False
    )
    bucket_name = bucketName # "flash-v2-files"
    object_name = objectName # "D415.tmp.xml"
    download_path = destinyPath # f"C:\\Users\\Alan\\Projects\\textSelecterBondingBox\\adssad.xml"
    minio_client.fget_object(bucket_name, object_name, download_path)
    print(f"File {object_name} downloaded to {download_path}")

def __init__():
    with open("rules.json", 'r') as json_file:
        instructions = json.load(json_file)
    
    if(instructions['activity'] == "ENCRYPT-V2"):
        currentPathV2 = os.getcwd() + "\\" + "creeper_for_v2\\"
        # download file
        for fileToDownload in instructions['data']:
            relativePath = os.getcwd() + "\\creeper_for_v2\\input\\" + fileToDownload["xmlName"]
            if fileToDownload['downloadFrom'] == "MINIO":

                downloadFromMinio(
                    bucketName = fileToDownload["folder"], 
                    objectName = fileToDownload["xmlName"] , 
                    destinyPath = relativePath )
            
            if os.path.isfile(relativePath):
                # the file was downloaded correctly
                print("The files was correctly downloaded")
                mainV2.main(fileToDownload)
                #mainV2.main2(fileToDownload)
                tmpFile =  f"{os.getcwd()}\\creeper_for_v2\\output\\{fileToDownload['fileName']}.tmp"
                if os.path.isfile(tmpFile):
                    print("TMP file was generated correctly")
                    interstoDB =   f"{os.getcwd()}\\creeper_for_v2\\output\\intersto.mdb"
                    
                    listToUpload = [
                        (f"/{instructions['activity']}/{instructions['activityId']}/{fileToDownload['fileName']}.tmp", tmpFile ),
                        (f"/{instructions['activity']}/{instructions['activityId']}/intersto.mdb", interstoDB)
                    ]
                    uploadFilesToMinio(BUCKET_WRITED, listToUpload)

                
            else:
                print("The file wasn't downloaded")

 
__init__()