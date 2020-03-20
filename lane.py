import numpy as np
import cv2

def img2edge(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #defining ranges for 'yellow', pixels within this range will be picked
    lower_yellow = np.array([20, 100, 100], dtype = "uint8")    
    upper_yellow = np.array([30, 255, 255], dtype="uint8")
    #
    #cv2.inRange(): Picks pixels from the image that are in the specified range
    mask_y = cv2.inRange(hsv_image, lower_yellow, upper_yellow)     
    mask_w = cv2.inRange(gray_image, 216, 255)
    #Computing Bitwise OR, combining both the white and yellow pixels
    mask_yw = cv2.bitwise_or(mask_w, mask_y)
    #Computing Bitwise AND of mask_yw with gray_img: pixels that were yellow or white will have the same intensity as the
    #original grayscale image, the other pixels will be removed
    mask_yw_image = cv2.bitwise_and(gray_image, mask_yw)
    #
    img_blur = cv2.GaussianBlur(mask_yw_image, (3, 3), 0)
    img_canny = cv2.Canny(img_blur, 70, 200)
    return img_canny
    
def roi_select(img, canny):
    #Defining vertices of the region of interest
    imshape = img.shape
    lower_left = [0,imshape[0]]
    lower_right = [imshape[1], imshape[0]]
    top_left = [0, imshape[0]/(3.2)]
    top_right = [imshape[1], imshape[0]/(3.2)]
    vertices = [np.array([lower_left,top_left,top_right,lower_right],dtype=np.int32)]
    #
    mask = np.zeros_like(canny)      #creates a numpy array of the same dimensions as img
    fill_color = 255               #parameter for cv2.fillPoly function
    cv2.fillPoly(mask, vertices, fill_color) #pixels within 'vertices' in 'mask' will be made WHITE while all other pixels will be BLACK
    return cv2.bitwise_and(canny, mask)

def draw_lines(canny_roi, rho_acc, theta_acc, thresh, minLL, maxLG):
    lines = cv2.HoughLinesP(canny_roi, rho_acc, theta_acc, thresh, np.array([]), minLL, maxLG)
    line_img = np.zeros((canny_roi.shape[0], canny_roi.shape[1], 3), dtype=np.uint8)
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_img, (x1, y1), (x2, y2), [255, 255, 255], 2)  
    return line_img

def add_weighted(img, line_img):
    return cv2.addWeighted(img, 0.8, line_img, 1, 0)

img = cv2.imread('lane_image.jpg')
edge_img = img2edge(img)
roi_img = roi_select(img, edge_img)
hough_img = draw_lines(roi_img, 2, np.pi/180, 50, 50, 100)
lane_img = add_weighted(img, hough_img)
cv2.imshow('edge', edge_img)
cv2.imshow('roi', roi_img)
cv2.imshow('Hough lines', hough_img)
cv2.imshow('Image with lanes', lane_img)
cv2.imwrite('LD_return_imgs/test_img01.jpeg', lane_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
