import cv2
import os
roots = ['水上漂浮物', '水体污染', '河流_塑料袋', '河道_垃圾']
out_dir = 'data'
m = 0
for root in roots:
    for n, img in enumerate(os.listdir(root)):
        print(n)
        path = os.path.join(root, img)
        i = cv2.imread(path)
        if i is None:
            print(path)
            os.remove(path)
        cv2.imshow("", i)
        k = cv2.waitKey(0)
        if k == ord('d'):
            os.remove(path)
        else:
            cv2.imwrite(os.path.join(out_dir, '%05d.jpg' % m), i)
            m += 1

        
