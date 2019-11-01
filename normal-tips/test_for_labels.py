from collections import Counter
import sys
import argparse
import os
import cv2
import random

# command: python test_for_labels.py --filename [test_file] --img_folder [all_image_path]

labels=["oval_face","round_face","rectangular_face","inverted_triangle_face","dark_brown_hair","light_brown_hair","black_hair","gray_hair","blond_hair","long_hair","short_hair","straight_hair","wavy_hair","hair_with_bangs","without_bangs","bald","not_bald","dense_eyebrow","sparse_eyebrow","thick_eyebrow","thin_eyebrow","arched_eyebrow","flat_eyebrow","up_eyebrow","down_eyebrow","big_eyes","medium_eyes","narrow_eyes","black_eyes","blue_eyes","brown_eyes","gray_eyes","wearing_eyeglasses","without_eyeglasses","big_nose","small_nose","pointy_nose","normal_nose","thick_lips","thin_lips","wide_mouth","small_mouth","wearing_lipstick","not_wearing_lipstick","with_mouth_closed","with_mouth_open","full_beard","goatee","circle_beard","five_o'clock_shadow","mustache","pale_skin","black_skin","yellow_skin","sharp_chin","round_chin","double_chin","man/boy","woman/girl","child","young","middle_aged","old","smiling_and_closing_mouth","smiling_and_showing_white_teeth","no_smiling"]
parser = argparse.ArgumentParser()
parser.add_argument('--filename', dest="filename", default="./")
parser.add_argument('--img_folder', dest="img_path", default="./")
arg = parser.parse_args()

# des_files = os.listdir(arg.folder_path)
# for des_file in des_files:
#     des_file = os.path.join(arg.folder_path, des_file)
with open(arg.filename, "r+") as f:
    feature = {}
    filenames = []
    err_file = arg.filename.replace(".txt", "_error.txt")
    file = open(err_file, "a+")
    old = sys.stdout
    sys.stdout = file
    result = f.read()
    content = result.split("\n")
    for one in content:
        if one == "":
            break
        name, attribute, text = one.split("\t")
        attributes = attribute.split(" ")
        count = Counter(attributes)
        if count['1'] < 8:
            print("{} 属性数量不够".format(name))
        elif not int(attributes[57])^int(attributes[58]):
            print("{} 必选项性别没选".format(name))
        elif not int(attributes[59])^int(attributes[60])^int(attributes[61])^int(attributes[62]):
            print("{} 必选项年龄没选".format(name))
        # elif not int(attributes[51])^int(attributes[52])^int(attributes[53]):
        #     print("{} 必选项种族没选".format(name))
        else:
            pass
        count_ = text.count("_")
        error = text.count("/")
        if error != 0:
            print("{} 有 /没删除".format(name))
        elif count_ < 5:
            print("{} 句子属性不足".format(name))
        feature[name] = attributes
        filenames.append(name)
    sys.stdout = old
    # print("random test for {} >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>".format(des_file))
    # flag = True
    # while(flag):
    #     x = input("请输入测试图片id：")
    #     if x == "q":
    #         flag = False
    #     else:
    #         print("label:{}".format(feature[x+".jpg"]))
    #         im = cv2.imread(os.path.join(arg.img_path, x+".jpg"))
    #         cv2.imshow(x+".jpg", im)
    #         cv2.waitKey(0)
    #         cv2.destroyAllWindows()
    samples = random.sample(filenames, 10)
    for sample in samples:
        attr = feature[sample]
        index = [i for i, x in enumerate(attr) if x == "1"]
        out = [labels[i] for i in index]
        print("name:{} \n attributes:{}".format(sample, out))
        im = cv2.imread(os.path.join(arg.img_path, sample))
        cv2.imshow(sample, im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

