import glob
import os
import cv2
import concurrent. futures
def load_and_resize(image_filename):
    ### Read in the image data
    img = cv2. imread(image_filename)
    ### Resize the image
    img = cv2.resize(img, (600, 600))
    ### Create a pool of processes. By default, one is created for eachCPU in your machine.

with concurrent . futures.ProcessPoolExecutor as executor:
    ### Get a list of files to processimage_ files = glob.glob("*.jpg")
    image_files = glob.glob("*.jpg")
    ### Process the list of files, but split the work across theprocess pool to use all CPUs
    ### Loop through all jpg files in the current folder### Resize each one to size 600x600
    executor.map(load_and_resize, image_files)
    # executor.map()将你想要运行的函数以及要处理的图像列表作为输入。有几个核心，就可以同时处理列表中的几张图像！
