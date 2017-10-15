from preprocessing import preprocess
from HorizontalSegmentation import horizontal_segmentation
from VerticalSegmentation import vertical_segmentation
from errorRemoval import error_removal
from visuals import preprocessing

from time import time
import os


def main():

    t = time()

    base_path = 'temp_images/'

    for file in os.listdir(base_path):
        try:
            os.remove(base_path + file)
        except FileNotFoundError:
            print('{} not deleted. \n'.format(file))
            continue

    ip_image_path = 'braille_scan.jpg'
    # ip_image_path = '/Users/ayushi/Desktop/uhack/braille_scan.jpg'

    try:
        os.remove('results.txt')
    except FileNotFoundError:
        print('results file not found.')

    preprocessed_image = base_path + 'preprecessed.jpg'

    preprocess(base_path, ip_image_path, preprocessed_image)
    # preprocessing(ip_image_path, preprocessed_image)

    n_lines = horizontal_segmentation(base_path, preprocessed_image)
    vertical_segmentation(base_path, n_lines)

    file = open('results.txt', 'r')
    text = file.read()
    file.close()
    print(text)

    error_removal()

    file = open('results.txt', 'r')
    text = file.read()
    file.close()
    print(text)

    print(time() - t)
    return text

if __name__ == '__main__':
    main()

