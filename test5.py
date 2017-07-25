import os
import cv2
import matplotlib.pylab as plt

HaarDirectory = '/usr/local/Cellar/opencv/2.4.9/share/OpenCV/haarcascades'
face_cascade = cv2.CascadeClassifier(os.path.join(HaarDirectory, 'haarcascade_frontalface_default.xml'))
eye_cascade = cv2.CascadeClassifier(os.path.join(HaarDirectory, 'haarcascade_eye.xml'))

Image = plt.imread('face.jpg')
BW_Image = cv2.cvtColor(Image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(BW_Image, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(Image, (x,y), (x + w,y + h), (255,0,0), 2)
    roi_gray = BW_Image[y:y + h, x:x + w]
    roi_color = Image[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0,255,0), 2)

plt.imsave('detected.png', Image)
plt.subplot(121)
plt.imshow(plt.imread('face.jpg'))
plt.subplot(122)
plt.imshow(Image)
plt.show()
