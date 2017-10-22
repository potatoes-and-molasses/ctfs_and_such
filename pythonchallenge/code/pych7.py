import cv2

a=cv2.imread(r'C:\users\team2\desktop\oxygen.png')
cv2.imshow('ok',a[45:])
cv2.waitKey(0)
cv2.destroyAllWindows()
st='#'
for i in a[46]:
    print i
    if i[0]==i[1]==i[2]:
        nxt=chr(i[0])
        if st[-1]!=nxt:
            st+=nxt

print st
#[105, 10, 16, 101, 103, 14, 105, 16, 121] in message - fix because my method sucks in handling repeat chars: 10=110(100?),16=116,14=114,16=116

print ''.join(chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121])
