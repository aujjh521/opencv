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
# img = cv2.imread('GrandmaCan_python_opencv-main/colorcolor.jpg')
# #resize img
# img = cv2.resize(img,(0,0), fx=0.5, fy=0.5) #用fx/fy倍數調整

# #轉成灰階
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #模糊化 (高斯模糊)
# blur = cv2.GaussianBlur(img, (9,9), 10)

# #找邊界
# canny = cv2.Canny(img, 150, 200)

# #膨脹 (把線條變粗)
# kernel = np.ones((3,3), np.uint8)
# dilate = cv2.dilate(canny, kernel, iterations=1)

# #侵蝕 (把線條變細)
# kernel = np.ones((3,3), np.uint8)
# erode = cv2.erode(dilate, kernel, iterations=1)


# cv2.imshow('img', img)
# cv2.imshow('gray', gray)
# cv2.imshow('blur', blur)
# cv2.imshow('canny', canny)
# cv2.imshow('dilate', dilate)
# cv2.imshow('erode', erode)
# cv2.waitKey(0)

#%%在圖片上畫圖型
# img = np.zeros((600,600,3), np.uint8)

# #line
# cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)

# #rectangle
# cv2.rectangle(img, (0,0), (400,300), (255,0,0), 3)

# #circle
# cv2.circle(img, (300,400), 50, (0,0,255), 2)

# #寫字 (不可以寫中文)
# cv2.putText(img, 'Hello', (100,500), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2.5, (255,255,255), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)

#%% 偵測顏色
# img = cv2.imread('GrandmaCan_python_opencv-main/XiWinnie.jpg')

# #resize img
# img = cv2.resize(img,(0,0), fx=0.5, fy=0.5) #用fx/fy倍數調整

# #為了接下來確認hsv圖片上面的h , s , v量值要多少,需要建立track bar
# def empty(v):
#     pass
# cv2.namedWindow('TrackBar') #整個trackbar坐落的window
# cv2.resizeWindow('TrackBar', 640, 320)

# cv2.createTrackbar('Hue min', 'TrackBar', 0, 179, empty) #新增一個叫做Hue min的bar在名稱為 'TrackBar'的window裡面
# cv2.createTrackbar('Hue max', 'TrackBar', 179, 179, empty) 
# cv2.createTrackbar('Sat min', 'TrackBar', 0, 255, empty) 
# cv2.createTrackbar('Sat max', 'TrackBar', 255, 255, empty) 
# cv2.createTrackbar('Val min', 'TrackBar', 0, 255, empty) 
# cv2.createTrackbar('Val max', 'TrackBar', 255, 255, empty) 

# #要做顏色偵測 第一步就是要先把BGR的格式轉成HSV
# #HSV跟BGR一樣也是一種表達顏色的格式,之所以要轉HSV是因為用HSV的表達格式做顏色篩選會比較容易
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# #即時取得前面做得'TrackBar'上面的設定數值,並且作顏色篩選
# while True:
#     #取得前面做得'TrackBar'上面的設定數值
#     h_min = cv2.getTrackbarPos('Hue min', 'TrackBar')
#     h_max = cv2.getTrackbarPos('Hue max', 'TrackBar')
#     s_min = cv2.getTrackbarPos('Sat min', 'TrackBar')
#     s_max = cv2.getTrackbarPos('Sat max', 'TrackBar')
#     v_min = cv2.getTrackbarPos('Val min', 'TrackBar')
#     v_max = cv2.getTrackbarPos('Val max', 'TrackBar')
#     print(h_min, h_max, s_min, s_max, v_min, v_max)

#     #把前面抓到的值存下來, 透過cv2.inRange做篩選 (篩選出來的mask存在變數mask裡面)
#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(hsv, lower, upper) #白色代表會保留下來

#     #把mask套在原圖上,直接看濾除之後的樣子
#     result = cv2.bitwise_and(img, img, mask=mask)

#     cv2.imshow('img', img)
#     cv2.imshow('hsv', hsv)
#     cv2.imshow('mask', mask)
#     cv2.imshow('result', result)
#     cv2.waitKey(2)

#%% 偵測輪廓/形狀
img = cv2.imread('GrandmaCan_python_opencv-main/shape.jpg')
imgContour = img.copy()

#檢測輪廓不需要顏色
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#邊界檢測
canny = cv2.Canny(img, 150, 200)

#抓輪廓 (把canny做完得結果傳進來抓輪廓)
contours, hierachy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

 #把每個輪廓畫在原本的image上面
for i,cnt in enumerate(contours):
    cv2.drawContours(imgContour, cnt, -1, (0,0,255), 4) #輪廓畫在原本的image上面
    print(i)
    area = cv2.contourArea(cnt) #輪廓面積
    peri = cv2.arcLength(cnt,True) #輪廓周長
    print(f'area / peri = {area} / {peri}') 

    if area > 500: #避免看到因為雜訊出現的0 area contour
        #近似出多邊形 (cv2.approxPolyDP回傳的是多邊形頂點的座標,所以取len之後就是近似出來的n邊形)
        vertices = cv2.approxPolyDP(cnt, peri*0.02, True)
        corners = len(vertices)
        print(f'corners number = {corners}')

        #產生外框框住物件的舉行座標 (回傳的是外框的左上頂點座標,以及長寬)
        #接著再畫出框框
        x,y,w,h = cv2.boundingRect(vertices)
        cv2.rectangle(imgContour, (x,y), (x+w,y+h), (0,0,0), 2 )

        #標記形狀的文字註解
        if corners == 3:
            cv2.putText(imgContour, 'Triangle', (x,y-8), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2) #文字註解
        elif corners == 4:
            cv2.putText(imgContour, 'Rectangle', (x,y-8), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2) #文字註解
        elif corners == 5:
            cv2.putText(imgContour, 'Pentagon', (x,y-8), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2) #文字註解
        elif corners > 5:
            cv2.putText(imgContour, 'circle', (x,y-8), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2) #文字註解

cv2.imshow('img', img)
cv2.imshow('canny', canny)
cv2.imshow('imgContour', imgContour)
cv2.waitKey(0)