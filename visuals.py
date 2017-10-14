import cv2
import numpy as np

'''
Steps:-
1. Read color
2. Cvt to BW
3. Cvt to Binary
4. Horizontal and vertical segmentation
'''


# Display Image
def display(image, name):
    cv2.imshow(name, image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return


def sliding_window(image, stepSize, windowSize):
    # slide a window across the image
    for x in range(0, image.shape[0], stepSize):
        for y in range(0, image.shape[1], stepSize):
            # yield the current window
            yield (x, y, image[x:x + windowSize[0], y:y + windowSize[1]])


def window_process(image):
    # Define the window size
    windowsize_r = 5
    windowsize_c = 5

    # Crop out the window and calculate the histogram
    for r in range(0, image.shape[0] - windowsize_r, windowsize_r):
        for c in range(0, image.shape[1] - windowsize_c, windowsize_c):
            window = image[r:r + windowsize_r, c:c + windowsize_c]
            print(window)


if __name__ == '__main__':

    # img = 'img2.jpeg'
    img = 'abc.jpeg'
    cvimg = cv2.imread(img, 0)
    display(cvimg, 'img1')

    row, cols = cvimg.shape

    integ = cv2.adaptiveThreshold(cvimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, 21, 10)
    display(integ, 'img2')

    max_val = min(shape[0], shape[1])
    min_size = max_val/30
    for x in range(0, max_val/2):
        i = x*min_size
        for y in range(0, max_val/2):
            j = y*min_size



    img_arr = []
    win_s = 5

    new_integ = integ.copy()
    # display(new_integ)
    stepSize = 3
    win_x = 3
    win_y = 8

    for x in range(0, integ.shape[0], stepSize):
        for y in range(0, integ.shape[1], stepSize):
            win = integ[x:x+win_x, y:y+win_y]
            black = np.count_nonzero(win == 0)
            white = np.count_nonzero(win == 255)
            val = 255
            if black > white:
                val = 0
            new_integ[x:x+win_x, y:y+win_y] = np.full(win.shape, val)

    display(new_integ, 'img3')

    bilateral_filtered_image = cv2.bilateralFilter(new_integ, 5, 175, 175)
    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
    cv2.imshow('Edge', edge_detected_image)
    cv2.waitKey(0)
