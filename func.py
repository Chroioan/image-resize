from PIL import Image
import sys
import os

in_directory = sys.argv[1]
L_size = int(sys.argv[2])
H_size = int(sys.argv[3])
out_size = (L_size, H_size)
out_directory = sys.argv[4]

print(in_directory, out_size, out_directory)

if not os.path.exists(in_directory):
    os.makedirs(in_directory)
if not os.path.exists(out_directory):
    os.makedirs(out_directory)
if len(os.listdir(in_directory))>0:
    for file in os.listdir(in_directory):
        in_file = Image.open(f'{in_directory}{file}')
        in_file.thumbnail(out_size)
        in_file.save(f'{out_directory}{file}', 'png')
        print(f' Your image is in {out_directory} directory! \n '
              f' The size is {in_file.size}')
else:
    print('no such a file in direcotry')
