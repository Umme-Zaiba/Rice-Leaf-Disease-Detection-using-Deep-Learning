from PIL import Image
import os
import shutil
import cv2


# root_folder = 'C:/Users/Gagan/PycharmProjects/FinalProject/datasets/diseases2'
# new_root= f"C:/Users/Gagan/PycharmProjects/FinalProject/datasets/new/"
root_folder = 'D:/FINAL YEAR PROJECT/senior project code/FinalProject/datasets/NEW2'
new_root = f"D: /FINAL YEAR PROJECT/senior project code/FinalProject/datasets/NEW2"
for sub2dir in os.listdir(f'{root_folder}'):
    files = os.listdir(f'{root_folder}/{sub2dir}')
    for file in files:
        path = f'{root_folder}/{sub2dir}/{file}'
        # print(path)
        img = cv2.imread(path)

        # get the rotation matrix
        # img= img.resize(100,100)
        center = (img.shape[1] / 2, img.shape[0] / 2)
        angle = [0, 90, 180, 270]
        scale = 1
        for ng in angle:

            M = cv2.getRotationMatrix2D(center, ng, scale)

            # apply the rotation to the image
            rotated_img = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))


            new_filepath = f'{new_root}/{sub2dir}/{ng}_{file}'
            os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

            # flip vertically
            imgv = cv2.flip(rotated_img, 0)
            new_filepath1 = f'{new_root}/{sub2dir}/{ng}v_{file}'
            os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

            # flip horizontally
            imgh = cv2.flip(rotated_img, 1)
            new_filepath2 = f'{new_root}/{sub2dir}/{ng}h_{file}'
            os.makedirs(os.path.dirname(new_filepath), exist_ok=True)

            print(new_filepath)
            cv2.imwrite(new_filepath, rotated_img)
            print(new_filepath1)
            cv2.imwrite(new_filepath1, imgv)
            print(new_filepath2)
            cv2.imwrite(new_filepath2, imgh)
