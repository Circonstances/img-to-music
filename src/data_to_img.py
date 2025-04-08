import librosa
from PIL import Image
import numpy as np


#global variables
width = 100
height = 200



#read mp3 file and transform it into a librosa 
def read_mp3(file_name):
    y, sr = librosa.load(file_name)
    return y, sr

#write an img from an array
def write_img_png(my_list, width, height):
    img = Image.new('RGB', [width, height],  None)
    data = img.load()
    print("writing img...")
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            img.putpixel((i, j), (my_list[i*j][0], my_list[i*j][1], my_list[i*j][2]))
            #img.putpixel((i, j), (my_list[i*j][0], 0, 0))
            #print("pixel is ", my_list[i*j])
    img.save('img/image.png')

def main():
    y, sr = read_mp3('samples/radiohead_all_i_need.mp3')
    print("this is y : ", y)
    print("this is sr : ", sr)
    print()
    length = librosa.get_duration(y=y ,sr=sr)
    print(len(y))
    first_arr = y[0:height*width*3]
    print("frist_arr lenght is ", len(first_arr))
    print(first_arr)
    X_norm = (((first_arr - first_arr.min()) / (first_arr.max() - first_arr.min()))*255)
    print("x_norm retyped" ,X_norm)
    print("x_norm length ", len(X_norm))
    X_norm = X_norm.astype(int)
    X_norm = np.array_split(X_norm, width*height)
    print(len(X_norm))
    write_img_png(X_norm, width, height)

if __name__ == "__main__":
    main()
