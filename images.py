from PIL import Image



def show_images(group_name, name_1, name_2):

    filename_1 = f"image/{group_name}/{name_1}.png"
    filename_2 = f"image/{group_name}/{name_2}.png"

    im1 = Image.open(filename_1)
    im2 = Image.open(filename_2)

    im1.show()
    im2.show()