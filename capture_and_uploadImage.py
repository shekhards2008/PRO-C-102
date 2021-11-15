import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
   
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        
        ret,frame = videoCaptureObject.read()
       
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    
    videoCaptureObject.release()
    
    cv2.destroyAllWindows()



def upload_file(img_name):
    access_token = "sl.Az3I66sQjOI7MAZcdzCFPWiqJfDWVAm5Mgh3RSUb49yfwyuCqaomh2x7bc8DOYf6pzj8qy9H2t3y59bswxOxMH9hsLllXcSiRe3c4T82dGG6Vl6kXu8scEua7PRrhIt2_qJh6f0"
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()
