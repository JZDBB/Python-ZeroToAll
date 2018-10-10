import cv2

def detectFaces(img):
    face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img #if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)#1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
    result = []
    for (x,y,width,height) in faces:
        result.append((x,y,x+width,y+height))
    return result



def main():

    # list_name = []
    # list_id = []
    # dict_label = {}
    #
    # f = open("Anno/identity_CelebA.txt")
    # for i in range(2000):
    #     line = f.readline()
    #     filename, id = line.split(' ')
    #     if id in list_id:
    #         continue
    #     list_id.append(id)
    #     list_name.append(filename)
    # f.close()
    #
    # f = open("Anno/list_attr_celeba.txt")
    # line = f.readline()
    # line = f.readline()
    # while line:
    #     line = f.readline()
    #     try:
    #         filename, label = line.split('g')
    #     except
    #     filename = filename + 'g'
    #     dict_label[filename] = label
    #
    # for file in list_name:
    img = cv2.imread("Img/img_align_celeba/img_align_celeba/000001.jpg")
    coordinate = detectFaces(img)
    x1, y1, x2, y2 = coordinate[0]
    # print(x1, y1, x2, y2)
    # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
    # cv2.imshow('', img)
    # cv2.waitKey(0)
    img = img[y1:y2, x1:x2]
    img_save = cv2.resize(img, (256, 256), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('Img/img_align_celeba/1.jpg', img_save)
    print('ok')

if __name__ == '__main__':
    main()