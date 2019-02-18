#213 RAL colors
# RAL base color + full RAL color
import cv2
import numpy as np
import time
##import serial
#--------------------------------------------------------------------------------
port = 'COM5'
camPort = 0
##ser = serial.Serial(port, 9600)
#--------------------------------------------------------------------------------
f = open('RALpcolor.txt')

RAL = []
R = []
G = []
B = []
E = []
Color = []
pColor = []

for line in f:
    line = line.strip()
    columns = line.split()
    RAL.append(int(columns[0]))
    R.append(int(columns[1]))
    G.append(int(columns[2]))
    B.append(int(columns[3]))
    E.append(0)
    Color.append(columns[4])
    pColor.append(columns[5])

cap = cv2.VideoCapture(camPort)

if ( not cap.isOpened()):
    print('no camera')
    exit()
while(cap.isOpened()):
    t_start = time.clock()
    ret, frame = cap.read()
    frame = cv2.flip(frame, 3)
    h,w,c = frame.shape
    b = frame[h//2,w//2,0]
    g = frame[h//2,w//2,1]
    r = frame[h//2,w//2,2]
    mini = 66000
    j = 500
    for i in range(len(RAL)):
        E[i] = (R[i]-r)**2 + (B[i]-b)**2 + (G[i]-g)**2
    j = E.index(min(E))
##    print RAL[j], Color[j], pColor[j]
    out = str(RAL[j]) + ' ' + str(Color[j])
    t = len(out)
    while(28 - t) > 0:
        out = out + ' '
        t = t + 1
    out = out + str(pColor[j])
    print(out)
##    ser.write(out)
##    time.sleep(0.01)
##    cv2.circle(frame, (w/2,h/2), 2, (255,0,255), 1)
    cv2.line(frame, (w//2-50,h//2), (w//2+50,h//2), (0,255,0), 1)
    cv2.line(frame, (w//2,h//2-50), (w//2,h//2+50), (0,255,0), 1)
    cv2.imshow('frame', frame)
    t_end = time.clock() - t_start
##    print t_end
    k = cv2.waitKey(1)
    if(k == 27 or k == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
