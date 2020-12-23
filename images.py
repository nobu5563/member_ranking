import os
import re
from PIL import Image
import glob
import matplotlib.pyplot as plt



def show_images(group_name):

    # path = f'image/{group_name}/all.png'
    # if os.path.isfile(path):
    #     img = Image.open(path)
    #     img.show()
    #     return None

    files = glob.glob(f'image/{group_name}/*.png')

    member_title = []

    for file_name in files:
        member_name = file_name[7+len(group_name):-4]
        member_title.append(member_name)

    im_list = []

    for file_name in files:
        img = Image.open(file_name)
        # img_size = img.size
        im_list.append(img)

    for i in range(len(member_title)):
        if len(member_title) <= 5:
            plt.subplot(1, len(member_title), i+1)
        else:
            plt.subplot(3, 3, i+1)
        plt.title(member_title[i])
        plt.axis('off')
        plt.subplots_adjust(wspace=0, hspace=0.2)
        plt.imshow(im_list[i])
    plt.pause(.01)

    # 画像の配置を一般化したい

##################################################################

    # if os.path.isfile(path) is False:
    #     print('(画像の保存完了)')
    #     fig.savefig(f'image/{group_name}/all.png')

    # concat_image(im_list, path, group_name, img_size)





# 今は使っていない
def concat_image(im_list, path, group_name, img_size):
    canvas = Image.new('RGB', (img_size[0]*len(group_name), img_size[1])) # 画像を並べるための領域を作成 (横, 縦)
    size = 0
    for i in range(len(im_list)):
        canvas.paste(im_list[i], (size, 0))
        size += img_size[0]

    canvas.show() # 画像を並べて表示

    # 初回実行時、並べた画像を保存
    if os.path.isfile(path) is False:
        print('(画像の保存完了)')
        canvas.save(f'image/{group_name}/all.png')