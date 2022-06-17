import cv2
import time
sj=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())  #转换一下时间
cap=cv2.VideoCapture(0)  #开启摄像头拍照
_, frame=cap.read()  #读取拍摄到的照片
name=("{}".format(sj)+'.jpg').replace(' ','_').replace(":",'_') #保存的图片名字，不能":"，所以转换以下
cv2.imwrite(r"C:\Opencv\{}".format(name),frame)  #图片保存的地方，需要修改一下
cap.release()  #关闭摄像头