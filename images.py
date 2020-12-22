from PIL import Image
import glob
import matplotlib.pyplot as plt



def show_images(group_name):

    path = f'image/{group_name}/all.png'
    files = glob.glob(f'image/{group_name}/*.png')

    im_list = []

    for file_name in files:
        print(file_name)
        img = Image.open(file_name)
        im_list.append(img)
    concat_image(im_list, path)



def concat_image(im_list, path):
    canvas = Image.new('RGB', (334*4, 500))
    size = 0
    for i in range(len(im_list)):
        canvas.paste(im_list[i], (size, 0))
        size += 334

    canvas.show()
    # if path is None:
    #     canvas.save('image/{group_name}/all.png')
    # 一括で表示したい
    # 初回にその画像を保存して、次回からそれを読み込む