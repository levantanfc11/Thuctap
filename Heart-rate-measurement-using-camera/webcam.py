import cv2
import numpy as np
import time

class Webcam(object):
    def __init__(self):
        #print ("WebCamEngine init")
        self.dirname = "" #for nothing, just to make 2 inputs the same
        self.cap = None
    
    def start(self):
        print("[INFO] Start webcam")
        time.sleep(1) # wait for camera to be ready
        self.cap = cv2.VideoCapture(0) #Truy cập từ thiết bị gốc (Chỉ số "0")
        self.valid = False
        try:
            resp = self.cap.read() #Đọc một Frame từ webcam, trả về resp[0] (boolean) là kết quả khung hình đã đọc được hay chưa
            #resp[1] là một mảng numpy chứa dữ liệu của khung hình đọc được
            self.shape = resp[1].shape
            self.valid = True
        except:
            self.shape = None
    
    def get_frame(self):
    
        if self.valid:
            _,frame = self.cap.read() # dấu _ là để bỏ qua giá trị đầu tiên được trả về
            frame = cv2.flip(frame,1) #Sử dụng OpenCV để lật ngang khung hình
            # cv2.putText(frame, str(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            #           (65,220), cv2.FONT_HERSHEY_PLAIN, 2, (0,256,256))
        else:
            frame = np.ones((480,640,3), dtype=np.uint8) #Tạo ra một mảng numpy toàn bộ có giá trị 1, có 3 chỉ số cao, rộng, số kênh màu
            col = (0,256,256)
            cv2.putText(frame, "(Error: Camera not accessible)",
                       (65,220), cv2.FONT_HERSHEY_PLAIN, 2, col)
        return frame

    def stop(self):
        if self.cap is not None:
            self.cap.release() #Đóng kết nối
            print("[INFO] Stop webcam")
        
