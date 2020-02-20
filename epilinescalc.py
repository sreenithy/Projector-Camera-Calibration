import cv2
import numpy as np
import matplotlib.pyplot as plt

def drawlines(img1,lines):
    ''' img1 - image on which we draw the epilines for the points in img2
        lines - corresponding epilines '''
    r,c = img1.shape
    img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)
    
    for r in lines:
        print("r",r)
        color = tuple(np.random.randint(0,255,3).tolist())
        x0,y0 = map(int, [0, -r[2]/r[1] ])
        x1,y1 = map(int, [c, -(r[2]+r[0]*c)/r[1] ])
        img1 = cv2.line(img1, (x0,y0), (x1,y1), color,1)
    cv2.imwrite("linesdrawn.png",img1)
    return img1

image1 = 255*np.ones((256, 256), dtype=np.uint8)
image2=cv2.imread('test.png',0)


E=np.array( [[-3.06449728e-01, -1.61141198e+02,  9.61018837e+01],
     [ 1.55885599e+02, -1.31427734e-01, -2.99605450e+00],
     [-1.04406471e+02 , 3.20187613e+00,  1.49716634e-01]])
F=np.array([[-1.83725186e-07 ,-9.66293421e-05 , 4.07617685e-02],
     [ 9.26315832e-05 ,-7.81147575e-08 ,-1.21161605e-02],
     [-4.83311114e-02  ,1.26637346e-02  ,1.00000000e+00]]
)

pts=[]

for i in range(1,256,10):
    x=np.array([[1],[i],[1]])
    pts.append(x)
print(pts)
"""
x=np.array([[0],[0],[1]])
pts.append(x)
"""
pts = np.int32(pts)
lines2 = cv2.computeCorrespondEpilines(pts.reshape(-1,1,2), 1,F)
lines2 = lines2.reshape(-1,3)
#l=np.transpose(E)@pt
print(lines2,drawlines(image2,lines2))

"""
# Find epilines corresponding to points in right image (second image) and
# drawing its lines on left image
lines1 = cv2.computeCorrespondEpilines([0,0,0], 2,F)
lines1 = lines1.reshape(-1,3)
img5,img6 = drawlines(img1,img2,lines1,pts1,pts2)

# Find epilines corresponding to points in left image (first image) and
# drawing its lines on right image
lines2 = cv2.computeCorrespondEpilines(pts1.reshape(-1,1,2), 1,F)
lines2 = lines2.reshape(-1,3)
img3,img4 = drawlines(img2,img1,lines2,pts2,pts1)

plt.subplot(121),plt.imshow(img5)
plt.subplot(122),plt.imshow(img3)
plt.show()
"""
