import cv2
import os

data_path = 'Img/img_align_celeba/img_align_celeba/'

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

    list_name = []
    list_id = []
    dict_label = {}

    f = open("Anno/identity_CelebA.txt")
    for i in range(3000):
        line = f.readline()
        filename, id = line.split(' ')
        if id in list_id:
            continue
        list_id.append(id)
        list_name.append(filename)
    f.close()

    f = open("Anno/list_attr_celeba.txt")
    line = f.readline()
    line = f.readline()
    for i in range(20000):
        line = f.readline()
        filename, label = line.split('g')
        filename = filename + 'g'
        dict_label[filename] = label
    f.close()

    for i in range(len(list_name)):
        img = cv2.imread(data_path + list_name[i])
        coordinate = detectFaces(img)
        print(list_name[i])
        try:
            x1, y1, x2, y2 = coordinate[0]
        except:
            continue
        img = img[y1:y2, x1:x2]
        img_save = cv2.resize(img, (256, 256), interpolation=cv2.INTER_CUBIC)
        name = list_id[i].strip('\n') + '.jpg'
        img_name = data_path + 'processing_Data/' + name
        cv2.imwrite(img_name, img_save)
        with open(data_path + 'processing_Data/' + 'label.txt', 'a') as f:
            f.write(name + dict_label[list_name[i]])


def select():
    dict_label = {}
    f = open("Anno/list_attr_celeba.txt")
    line = f.readline()
    line = f.readline()
    while line:
        line = f.readline()
        filename, label = line.split('g')
        filename = filename + 'g'
        dict_label[filename] = label
    f.close()

    list_file = os.listdir(data_path + 'processing_Data/')
    for filename in list_file:
        with open(data_path + 'processing_Data/' + 'label.txt', 'a') as f:
            f.write(filename + dict_label[filename])



if __name__ == '__main__':
    main()