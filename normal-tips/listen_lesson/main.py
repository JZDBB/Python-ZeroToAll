# gtk is use in ubuntu
# in windows we use PyQt4
# both windows and ubuntu we need PyUserInput which contain pymouse and pykeyboard!

# import gtk.gdk 
import cv2
import matplotlib.pyplot as plt
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import sys
from PyQt4.QtGui import QPixmap, QApplication

import numpy as np
# a = cv2.imread('screenshot.png', 0)
# plt.imshow(a)
# plt.show()
def det(img, kn):
    res = np.zeros(shape=[img.shape[0] - kn.shape[0] + 1,
                          img.shape[1] - kn.shape[1] + 1])
    for i in range(img.shape[0] - kn.shape[0]):
        for j in range(img.shape[1] - kn.shape[1]):
            a = img[i:i + kn.shape[0], j:j + kn.shape[1]]
            res[i, j] = (a == kn).all()

    return res

kernel = cv2.imread("pt.png", 0)
kernel = kernel[430:460, 696:710]
m = PyMouse()
app = QApplication(sys.argv)
# w = gtk.gdk.get_default_root_window()
# sz = w.get_size()
while(True):
    # pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    # pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    # pb.save("screenshot.png","png")
    QPixmap.grabWindow(QApplication.desktop().winId()).save('screenshot.png', 'png')

    screenshot = cv2.imread("screenshot.png", 0)
    # # kernel = screenshot[430:460, 696:710]
    # plt.imshow(kernel)
    # plt.show()
    res = det(screenshot, kernel)
    x = max(np.argmax(res, 0))
    y = max(np.argmax(res, 1))
    if x + y:
    # k = PyKeyboard()
    # x_dim, y_dim = m.screen_size()
        m.click(y, x, 1)
    # k.type_string('Hello, World!')
    time.sleep(30)
