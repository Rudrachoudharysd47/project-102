import cv2
import dropbox
import time
import random
starttime = time.time()
def takesnapshot():
    number = random.randint(0,100)
    vedioCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = vedioCaptureObject.read()
        print(ret)
        image_name = "image"+str(number)+".png"
        cv2 .imwrite(image_name,frame)
        starttime = time.time()
        result = False
    return image_name

    vedioCaptureObject.release()
    cv2.destroyAllWindows()
def uploadfile(image_name):
    access_token = 'sl.BGTrxoHKzb8l8mp_kO4N0CO0y4fNpvCu3nBicBo5ehHf3svv5CxJWXFUk5M673YpbSybLCnYdcM-ToyYuD87EIY5Wx35rCwKYQo8NbBqxj3g7Y2R1QJ9I_JTwSvRwCM6L8cB-m0'
    file_from = image_name
    file_to = "/aoutomation/"+image_name
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from,'rb')
    dbx.files_upload(f.read(),file_to)




while(True):
    if((time.time()-starttime) >= 5):
        name = takesnapshot()
        uploadfile(name)
