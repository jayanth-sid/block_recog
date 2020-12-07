import cv2
def getcontours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        #print(area)
        if area>100:
            #cv2.drawContours(imgcontour, cnt, -1, (255, 0, 0), 3)(draw borders)
            peri=cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.03*peri,True)
            if (len(approx))==3:
                x,y,w,h=cv2.boundingRect(approx)
                cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),1)





img=cv2.imread(r"")#path of file
imgcontour = img.copy()
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurimg=cv2.GaussianBlur(grayimg,(7,7),1)
cannyimg=cv2.Canny(blurimg,20,20)
getcontours(cannyimg)
cv2.imshow("graqy",cannyimg)
cv2.imshow("gray",imgcontour)

cv2.waitKey(0)