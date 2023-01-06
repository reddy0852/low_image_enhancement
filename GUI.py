import cv2
import easygui
import glob
import os
import time
import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter import filedialog

import model
import numpy as np
import torch
import torch.optim
import torchvision
from PIL import Image
from PIL import ImageTk

originalImage = None


def upload():
    global originalImage, tkImage
    imagePath = easygui.fileopenbox()  # image path
    if imagePath is None:
        return
    originalImage = cv2.imread(imagePath)  # open image
    originalImage = cv2.resize(originalImage, (600, 400))  # resize image
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)
    tkImage = Image.fromarray(originalImage)  # convert to PIL format
    tkImage = ImageTk.PhotoImage(tkImage)  # convert to Imagetk format
    Label(right_frame, image=tkImage).grid(row=0, column=0, padx=3, pady=3)  # display image in right frame
    IMAGE = cv2.imread(imagePath)
    os.chdir(r"D:\Low light Image\data\test_data\images")
    newName = "Inputimage.jpg"
    cv2.imwrite(newName, IMAGE)


def lowlight(image_path):
    global originalImage2, tkImage2
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    data_lowlight = Image.open(image_path)
    data_lowlight = (np.asarray(data_lowlight) / 255.0)
    data_lowlight = torch.from_numpy(data_lowlight).float()
    data_lowlight = data_lowlight.permute(2, 0, 1)
    data_lowlight = data_lowlight.unsqueeze(0)
    DCE_net = model.enhance_net_nopool()
    DCE_net.load_state_dict(
        torch.load(r'D:\Low light Image\snapshots\Epoch99.pth',
                   map_location={'cuda:0': 'cpu'}))
    start = time.time()
    _, enhanced_image, _ = DCE_net(data_lowlight)

    end_time = (time.time() - start)
    print(end_time)
    # image_path = image_path.replace('test_data','result')
    # result_path = image_path
    # if not os.path.exists(image_path.replace('/'+image_path.split("/")[-1],'')):
    #     os.makedirs(image_path.replace('/'+image_path.split("/")[-1],''))

    torchvision.utils.save_image(enhanced_image,
                                 r"D:\Low light Image\data\result\images\output.jpg")
    imagePath2 = (
        r"D:\Low light Image\data\result\images\output.jpg")  # image path
    originalImage2 = cv2.imread(imagePath2)  # open image
    originalImage2 = cv2.resize(originalImage2, (600, 400))  # resize image
    originalImage2 = cv2.cvtColor(originalImage2, cv2.COLOR_BGR2RGB)
    tkImage2 = Image.fromarray(originalImage2)  # convert to PIL format
    tkImage2 = ImageTk.PhotoImage(tkImage2)  # convert to Imagetk format
    Label(mid_frame, image=tkImage2).grid(row=0, column=0, padx=3, pady=3)


def image_enhancement():
    # test_images
    with torch.no_grad():
        # filePath = (r'F:\6thsem\AIML\Lab\GUI\Newfolder\data\test_data')
        # file_list = os.listdir(filePath)
        # for file_name in file_list:
        test_list = glob.glob(
            r"D:\Low light Image\data\test_data\images*")
        for image in test_list:
            print(image)
            lowlight(image)


def savefile():
    imagePath3 = (
        r"D:\Low light Image\data\result\images\output.jpg")  # image path
    originalImage3 = cv2.imread(imagePath3)
    originalImage3 = cv2.cvtColor(originalImage3, cv2.COLOR_BGR2RGB)
    edge = Image.fromarray(originalImage3)
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    edge.save(filename)


def Close():
    top.destroy()


top = tk.Tk()

window_width = 2200

window_height = 700

# get the screen dimension
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# top.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

icon_img = ImageTk.PhotoImage(
    Image.open(r"D:\Low light Image\download.png"))
top.iconphoto(False, icon_img)
top.title('Image enhancement using deep learning')

top.config(bg="grey16")

left_frame = Frame(top, width=300, height=530, bg='grey16')
left_frame.grid(row=1, column=0, padx=10, pady=55)
mid_frame = Frame(top, width=700, height=530, bg='light slate grey')
mid_frame.grid(row=1, column=2, padx=15, pady=25)
right_frame = Frame(top, width=700, height=530, bg='light slate grey')
right_frame.grid(row=1, column=1, padx=15, pady=25)
button_frame = Frame(top, width=18, height=5, bg='grey16')
button_frame.grid(row=2, column=1, padx=0, pady=0)

ai_image = ImageTk.PhotoImage(
    Image.open(r"D:\Low light Image\index.jpg"))
Label(right_frame, image=ai_image).grid(row=0, column=0, padx=3, pady=3)

a_image = ImageTk.PhotoImage(
    Image.open(r"D:\Low light Image\index.jpg"))
Label(mid_frame, image=a_image).grid(row=0, column=0, padx=3, pady=3)

button_font = font.Font(family='Times', size=11)

upload_button = tk.Button(left_frame, text="UPLOAD IMAGE", command=upload, fg="black", height=2, width=20, border='0')
upload_button.grid(row=0, column=1, padx=10, pady=15)
upload_button['font'] = button_font

enhance_button = tk.Button(left_frame, text="ENHANCE IMAGE", command=image_enhancement, fg="black", height=2, width=20)
enhance_button.grid(row=1, column=1, padx=0, pady=15)
enhance_button['font'] = button_font

save_button = tk.Button(left_frame, text="SAVE IMAGE", command=savefile, fg="black", height=2, width=20)
save_button.grid(row=4, column=1, padx=0, pady=15)
save_button['font'] = button_font

exit_button = tk.Button(left_frame, text="EXIT", command=Close, fg="black", height=2, width=20)
exit_button.grid(row=5, column=1, padx=0, pady=15)
exit_button['font'] = button_font

top.mainloop()
