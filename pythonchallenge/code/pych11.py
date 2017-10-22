import cv2

a=cv2.imread(r'C:\users\team2\desktop\pych\cave.jpg')
cv2.imshow('ok',a)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(len(a)):
        for j in range(len(a[0])):
                
                for k in [0,1,2]:
                        if (i+j)%2:
                                a[i][j][k]=0
                        else:
                                a[i][j][k]*=10#in retrospect:D just used stegsolve originally:(

cv2.imshow('ok',a)
cv2.waitKey(0)
cv2.destroyAllWindows()
