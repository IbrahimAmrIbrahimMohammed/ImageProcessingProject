'''
@author sara khaled
'''
import cv2
import numpy as np
from utils import object_file

#======================================================================================================================#
def sort_contours(contours):
    '''
    description : sort the contours from left to right based on the xmin
    :param contours: list of contours
    :return: list of sorted contours
    '''
    sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])
    return sorted_contours
#======================================================================================================================#
def image_preprocessing(image,label="nothing"):
    '''
    description : taking part of the big image(state condition or state) and preprocessing it in with mean threshold method
    and resize the image to make better predict
    :param image: image passed by the predict of state condition or state, np.array
    :param label: given label by the predict function, string
    :return:new image , ratio of the new width and new height to draw back on the big image again
    '''
    im=image.copy()#copy of the image
    width = im.shape[0]  # the width of the image
    height = im.shape[1]  # the height of the image

    ratio_factor=2
    resize_width_value = float(width * ratio_factor)  # new width
    resize_height_value = float(height * ratio_factor)  # new height

    # -------------------------------------------#
    width_ratio = float(width / resize_width_value) # ratio of the width is the original width / new width after scaling

    height_ratio = float(height / resize_height_value)# ratio of the height is the original height / new height after scaling
    # ---------------------------------------#
    # ==========================================#
    im = cv2.resize(im, (int(resize_height_value), int(resize_width_value)))# resize the copy image
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)# change the color from BGR to gray

    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY_INV,11,2) # adaptive thresh mean method to get the image in black and white only

    preprocessed_image = thresh# the preprocessed image is the output of the thresh

    if label=="state":#special case if the label is state we need dilate
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 4))# kernal 2 * 4
        preprocessed_image=cv2.dilate(preprocessed_image,kernel,iterations=1)#dilate the numbers for low resolution image

    return preprocessed_image,width_ratio,height_ratio
#======================================================================================================================#
def model_preprocessing():
    '''
    description : load the model knn for numbers predict
    :return: knn model
    '''
    model = cv2.ml.KNearest_load("weights/model_7.text")
    return model
#======================================================================================================================#
def reshape_state(img):
    '''
    description : taking an image of state and crop it to get only the numbers inside as a new image
    :param img:  state image ,np.array
    :return: new image of numbers only inside the state , np.array  and extra_xmin and extra_ymin for getting to coordinates on the original image
    '''
    width=img.shape[1]# x axis
    height=img.shape[0]# y axis
    center_y=int ((height)/2)
    center_x=int(width/2)
    perecntage_of_extra_width=  (30 /100)
    perecntage_of_extra_height = (30 / 100)

    extra_width_to_center=int(width * perecntage_of_extra_width)
    extra_height_to_center = int(height * perecntage_of_extra_height)

    #most likely to have the numbers inside the center
    #so i will ge the center and move for like 30 % of the image

    new_img=img[center_y - extra_height_to_center   :   center_y+extra_height_to_center,  center_x-extra_width_to_center  :  center_x+extra_width_to_center]
    extra_ymin=center_y - extra_height_to_center
    extra_xmin=center_x-extra_width_to_center
    return new_img,extra_xmin,extra_ymin
#======================================================================================================================#
def get_inputs_outputs_slash_for_state_condition(image,xmin,ymin,label):
    '''
    description : main function of this file, taking cropped image(state anchor or state condition anchor )
    from the original image and predict the numbers inside it and ignore any noise input like "/" or ")" from the cropped
    image, need the xmin,ymin and label of the cropped image to add this values later to draw back on the original image.
    :param image: cropped image, np.array
    :param xmin: xmin of the cropped image , int
    :param ymin: ymin of the cropped image , int
    :param label: label of the cropped image , string
    :return:void
    '''
    if label=="state":# if the label state
        im,extra_xmin,extra_ymin = reshape_state(image)# send it to reshape state
        xmin=xmin+extra_xmin # the xmin is now incremented by the extra xmin of the cropped image from reshape state
        ymin=ymin+extra_ymin# the ymin is now incremented by the extra ymin of the cropped image from reshape state
    else:#not a state
        im=image
    model=model_preprocessing()# load the knn model
    preprocessed_image,width_ratio,height_ratio=image_preprocessing(im,label)# preprocess the image
    contours, hierarchy = cv2.findContours(preprocessed_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)# find the contours  of every object not inside another object
    contours = sort_contours(contours)# sort the contors from left to right
    preprocessed_image_width = preprocessed_image.shape[1] # width of the preprocessed image
    preprocessed_image_height = preprocessed_image.shape[0] # height of the preprocessed image
    preprocessed_image_area=preprocessed_image_width*preprocessed_image_height # area of the preprocessed image

    area_ratio_threshold=30/100 # area ratio threshold, if contour area more than 30 % of the image area, ignore it
    width_ratio_max_threshold=50/100# if the width of the contour more than 50% of the image ignore it
    width_ratio_min_threshold=5/100 # if the width of the contour less than 5% of the image ignore it
    height_ratio_min_threshold=15/100# if the height of the contour less than 20% of the image ignore it
    height_ratio_max_threshold=80/100# if the height of the contour more than 80% of the image ignore it
    shrunk_value=30# resize the contour with value shrunk value

    preprocessed_image_width_threshold_max  = int(preprocessed_image_width * width_ratio_max_threshold)# the max width threshold value
    preprocessed_image_width_threshold_min  = int(preprocessed_image_width * width_ratio_min_threshold)# the min width threshold value
    preprocessed_image_height_threshold_max = int(preprocessed_image_height* height_ratio_max_threshold)# the max height threshold value
    preprocessed_image_height_threshold_min = int(preprocessed_image_height * height_ratio_min_threshold)# the min height threshold value

    for cnt in contours:# for every contour
        if cv2.contourArea(cnt) > 1 and cv2.contourArea(cnt) < preprocessed_image_area*area_ratio_threshold:#check the area first
            [x, y, w, h] = cv2.boundingRect(cnt) # get the contour width and height
            if w <preprocessed_image_width_threshold_max and w > preprocessed_image_width_threshold_min \
                and h <preprocessed_image_height_threshold_max and h > preprocessed_image_height_threshold_min:# the threshold conditions

                number_only_image = preprocessed_image[y:y + h, x:x + w]  # take this contour from the image
                number_only_image_resized = cv2.resize(number_only_image, (shrunk_value, shrunk_value))# resize this contour with the shrunk value
                kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))#kernal 3 x 3 cross
                number_only_image_resized = cv2.dilate(number_only_image_resized,kernel,iterations=1)
                number_only_image_resized = number_only_image_resized.reshape((1, shrunk_value*shrunk_value))#changing the shape for the model config-> shrunk_value*shrunk_value
                number_only_image_resized = np.float32(number_only_image_resized) # image must be float np array
                retval, results, neigh_resp, dists = model.findNearest(number_only_image_resized, k=3)# use the knn model with k= 3 to predict the numbers
                string = str(int((results[0][0]))) # the result in string type
                if label=="state condition" and (string!="0" and string!="1"):
                    continue

                if int((results[0][0]))==-1 :# -1 --->/
                    string="/"
                    continue


                object_file.all_objects_as_dic[str(string)].append(
                    object_file.DC.Data(str(string),
                                        str(int(x * width_ratio)+xmin), str(int(y * height_ratio)+ymin),
                                        str(int(x * width_ratio + w * width_ratio)+xmin), str(int(y * height_ratio + h * height_ratio)+ymin),
                                        str("90"), object_file.object_id))  # insert the anchor in the dictionary

                object_file.object_id = object_file.object_id + 1 # increment the object id by 1
#======================================================================================================================#
