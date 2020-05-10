'''
@author ahmed hessuin
description : this file is for operation on image.
'''
from cv2 import rectangle
from utils import object_file
from cv2 import imwrite
from utils import log_config
import numpy as np
import cv2
#======================================================================================================================#
def get_image():
    '''
    description : get the original image use it before any draw on the image
    :return void
    '''
    object_file.image=object_file.image_copy.copy()
#======================================================================================================================#
def draw_elements():
    '''
    description : draw all elements predicted and added or removed on the image
    by searching in all object dictionary elements and draw them
    :return: void
    '''
    headers_in_reverse = []
    for header in object_file.all_objects_as_dic:
        headers_in_reverse.insert(0, header)

    for header in headers_in_reverse:# for every header(key) in the dictionary
        for element in range(len(object_file.all_objects_as_dic[header])):# for every element  in this list
            draw_on_image(object_file.image, object_file.all_objects_as_dic[header])# draw this element on the image
#======================================================================================================================#
def draw_on_image(image,boxes):
    '''
    description: take and image and boxes list, then draw rectangle on the image based on
    the xmin, xmax, ymin ,ymax and color the rectangle depend on the label

    :param image: an image , np array
    :param boxes: an input list of boxes ,type Data, defined in data_class.py
    :return: void
    '''
    color=[1,2,3]

    #============ set color for every label ===========#
    for box in boxes:
        thickness=2 #default value
        if (box.get_label()) == ("state"):
            color = [217, 89, 80]
        elif (box.get_label()) == ("/"):
            color = [0, 255, 0]
            thickness = 1
        elif (box.get_label()) == ("loop back arrow"):
            color = [255, 0, 255]
        elif (box.get_label()) == ("state condition"):
            color = [50, 0, 255]
        elif (box.get_label()) == ("arrow head"):
            color = [249, 223, 64]
        elif (box.get_label()) == ("straight arrow") or (box.get_label()) == ("curved arrow"):
            color = [27, 189, 255]

        else:
            color = [166, 73, 36]  # this is for text and numbers
            thickness = 1


        #===============================================#
        rectangle(img=image, pt1=(box.get_xmin(), box.get_ymin()), pt2=(box.get_xmax(), box.get_ymax()), color=color, thickness=thickness)  # rectangle format
        if box.get_name()=="0" or box.get_name()=="1" or box.get_name()=="2" or box.get_name()=="3" or \
                box.get_name() == "4" or box.get_name()=="5" or  box.get_name()=="6" or  box.get_name()=="7" or \
                box.get_name() == "8" or box.get_name()=="9" or box.get_name()[0]=="g": #box.get_name()[0]=="g":  this condition for generated ids
            text_color=color
            cv2.putText(image,box.get_name(),(box.get_xmin(),box.get_ymax())
                        ,cv2.FONT_HERSHEY_SIMPLEX,1,text_color,2,cv2.LINE_4)

    #========================================#
#======================================================================================================================#
def get_element_with_x_and_y(x_input,y_input):
    '''
    description : return any element has (x_input,y_input) inside of it, if there are many objects
    share this x and y, remove the smallest area.

    :param x_input: x dimension of a point
    :param y_input: y dimension of a point
    :return: string of the element name or "didn't find anything", header,type(string), element,type(Data)
    '''

    element_name=""
    area=1920000 # a very large area as initialization value
    remove_header="" # header of the removed element
    remove_element=None # index of the removed element
    for header in object_file.all_objects_as_dic.keys():
        for element in object_file.all_objects_as_dic[header]:
                if element.get_xmin() < int(x_input) and \
                 element.get_xmax()>int(x_input) and\
                 element.get_ymin()<int(y_input) and\
                 element.get_ymax()>int(y_input):

                    element_width=element.get_xmax()-element.get_xmin()
                    element_height=element.get_ymax()-element.get_ymin()
                    element_area=element_width*element_height

                    if element_area<area: #mark this element
                        element_name= element.get_name()#get the name
                        area = element_area # update the area
                        remove_header=header  # mark the header
                        remove_element=element # mark the element


    if remove_element==None:
        return "didn't find anything to remove",remove_header,remove_element

    return element_name,remove_header,remove_element
    #--------------------------------------------#
#======================================================================================================================#
def remove_element(remove_header,remove_element):
    '''
    description : remove element from a given header, taking it's header name and the element type

    :param remove_header : the name of the dictionary key, string
    :param remove_element: the element to remove from the dictionary
    :return: text " removed "+ the element that was removed
    '''

    element_name=remove_element.get_name()
    object_file.all_objects_as_dic[remove_header].remove(remove_element)  # remove this anchor from my anchor dictionary

    update_image()

    return log_config.start_of_log()+"removed " + element_name+log_config.end_of_log()
    #--------------------------------------------#
#======================================================================================================================#
def add_element(x_min,y_min,x_max,y_max,name,accuracy="100%"):
    '''
    description : add element of label(name), defined by 2 points
    draw the rectangle on the image based on p1 and p2
    add this element to xml file

    :param x_min: point 1 xmin
    :param y_min: point 1 ymin
    :param x_max: point 2 xmax
    :param y_max: point 2 ymax
    :param name: label name
    :param accuracy: accuracy optional
    :return: text "added +" the name of the label
    '''
    # adding this anchor
    object_file.all_objects_as_dic[str(name)].append(object_file.DC.Data(str(name),str(x_min),str(y_min),str(x_max),str(y_max),str(accuracy),object_file.object_id))
    #update the object id
    object_file.object_id=object_file.object_id+1
    update_image()
    return log_config.start_of_log()+"added "+ name+log_config.end_of_log()
#======================================================================================================================#
def undo_element():
    '''
    under development
    :return:text " undo completed "
    '''
    if len(object_file.undo_all_objects)>0:
        object_file.all_objects.append(object_file.undo_all_objects.pop())

    get_image()
    draw_elements()
    return ("undo completed")
#======================================================================================================================#
def export_image():
    '''
    description : write on the hard disk the output image based on the
    output path

    :return: void
    '''
    imwrite(object_file.output_path, np.uint8(object_file.image))
#======================================================================================================================#
def set_output_path(new_output_path):
    '''
    description: set the output path of the exported image

    :param new_output_path: set the output path of the output image
    :return: void
    '''
    object_file.output_path=new_output_path
#======================================================================================================================#
def update_image():
    '''
    description : update the image by redrawing
    :return: void
    '''
    get_image()
    draw_elements()
#======================================================================================================================#