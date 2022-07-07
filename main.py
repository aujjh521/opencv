import cv2
import numpy as np
import random

#%% 讀取image
# img = cv2.imread('GrandmaCan_python_opencv-main/colorcolor.jpg')
# #resize img
# #img = cv2.resize(img,(300,300)) #直接指定要的大小
# img = cv2.resize(img,(0,0), fx=0.5, fy=0.5) #用fx/fy倍數調整

#  #imshow 第一個要給圖片名稱,第二個是圖片本身
# cv2.imshow('img title', img)

# #waitkey 目的是不要讓圖片一出現就因為程式結束而消失 (裡面數字單位是毫秒), 給0就是不關閉
# #另外waitkey本身的目的是等待給定的秒數,要等鍵盤給一個輸入 然後把該輸入的編號回傳
# cv2.waitKey(0)

#%% 讀取video

#cap = cv2.VideoCapture('GrandmaCan_python_opencv-main/thumb.mp4')
#cap = cv2.VideoCapture(0) #直接讀取攝像頭的畫面

#影片處理上就是把它拆解成一堆的image接在一起 (每張image稱為一楨)
#.read會回傳2個東西, 第一個是是否有拿到影片的下一楨(下一張image)boolean, 第二個是下一楨(下一張image)的內容
#以下code會取得影片的第一楨
# ret,frame = cap.read()
# if ret:
#     cv2.imshow('video title', frame)

# cv2.waitKey(0)

#連續取得每一楨
# while True:
#     ret,frame = cap.read()
#     if ret:
#         frame = cv2.resize(frame, (0,0), fx=0.4, fy=0.4)
#         cv2.imshow('video title', frame)
#     else:
#         break

#     if cv2.waitKey(10) == ord('q'): #以每楨等待10毫秒撥放,同時如果接收到鍵盤 "q",就直接結束
#         break

#%% 自己產生圖片
# img = np.empty((300,300,3), np.uint8)
# for row in range(img.shape[0]):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

# cv2.imshow('img',img)
# cv2.waitKey(0)

#%% 修改已知圖片的顏色
# img = cv2.imread('GrandmaCan_python_opencv-main/colorcolor.jpg')
# for row in range(100,200):
#     for col in range(30,600):
#         img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]

# cv2.imshow('img',img)
# cv2.waitKey(0)

#%% 切割圖片
# img = cv2.imread('GrandmaCan_python_opencv-main/colorcolor.jpg')
# newImg = img[:150, :200]

# cv2.imshow('img',img)
# cv2.imshow('newImg',newImg)
# cv2.waitKey(0)

#%% 常用函式
img = cv2.imread('GrandmaCan_python_opencv-main/colorcolor.jpg')
#resize img
img = cv2.resize(img,(0,0), fx=0.5, fy=0.5) #用fx/fy倍數調整

#轉成灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#模糊化 (高斯模糊)
blur = cv2.GaussianBlur(img, (9,9), 10)

#找邊界
canny = cv2.Canny(img, 150, 200)

#膨脹 (把線條變粗)
kernel = np.ones((3,3), np.uint8)
dilate = cv2.dilate(canny, kernel, iterations=1)

#侵蝕 (把線條變細)
kernel = np.ones((3,3), np.uint8)
erode = cv2.erode(dilate, kernel, iterations=1)



cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)

