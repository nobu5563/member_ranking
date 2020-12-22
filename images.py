import os
from PIL import Image
import glob
import matplotlib.pyplot as plt



def show_images(group_name):

    path = f'image/{group_name}/all.png'
    files = glob.glob(f'image/{group_name}/*.png')

    im_list = []

    for file_name in files:
        img = Image.open(file_name)
        im_list.append(img)
    concat_image(im_list, path, group_name)



def concat_image(im_list, path, group_name):
    canvas = Image.new('RGB', (334*4, 500))
    size = 0
    for i in range(len(im_list)):
        canvas.paste(im_list[i], (size, 0))
        size += 334

    canvas.show() # 画像を並べて表示

    # 初回はその画像を保存
    if os.path.isfile(path) is False:
        # save_path = f'image/{group_name}'
        canvas.save(f'image/{group_name}/all.png')

    # メンバーの名前も付けたい
    # concat_imageを一般化