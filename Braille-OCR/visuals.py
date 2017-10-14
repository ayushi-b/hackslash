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


def preprocessing(input_image, op_path):

    cvimg = cv2.imread(input_image, 0)
    # display(cvimg, 'img1')

    row, cols = cvimg.shape

    integ = cv2.adaptiveThreshold(cvimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, 21, 10)
    # cv2.imwrite(integ, 'img2')

    # sh = integ.shape
    # max_val = min(sh[0], sh[1])
    # min_size = max_val/30
    # for x in range(0, max_val//2):
    #     i = x*min_size
    #     for y in range(0, max_val//2):
    #         j = y*min_size

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

    # display(new_integ, 'img3')

    bilateral_filtered_image = cv2.bilateralFilter(new_integ, 5, 175, 175)
    edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
    cv2.imwrite(op_path, edge_detected_image)
    # cv2.waitKey(0)

