#! /usr/bin/env python
'''
@author ahmed hessuin
description : predict file core file for prediction on the given image
'''
#commented by ibrahiem amr / ahmed hessuin
import numpy as np
import cv2
from utils.utils import get_yolo_boxes
from utils.bbox import config_boxes
from keras.models import load_model as load_model_1
from keras.models import load_model as load_model_2
from keras.models import load_model as load_model_3
from utils import log_config
from utils   import  matching
import transactionToVerilog
from keras.models import load_model as load_model_4
from keras.models import load_model as load_model_5
from utils import image_operations
from utils import object_file
from  utils import  xml_creator
import image_preprocess

#============================= warning remover =========================================#
import warnings
from tensorflow.python.util import deprecation
deprecation._PRINT_DEPRECATION_WARNINGS = False

import tensorflow as tf
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

warnings.filterwarnings('ignore')
tf.get_logger().setLevel('INFO')

try:
    from tensorflow.python.util import module_wrapper as deprecation
except ImportError:
    from tensorflow.python.util import deprecation_wrapper as deprecation
deprecation._PER_MODULE_WARNING_LIMIT = 0
#======================================================================================================================#
def set_inputpath_and_image(image,input_path):
    '''
    description : set the input path in object file and the image in object file for future use
    :param image: input image, np array
    :param input_path: input path, text (str)
    :return: void
    '''
    object_file.image = image.copy()  # set the image
    object_file.image_copy= image.copy()
    object_file.input_path=input_path # set the image path
#======================================================================================================================#
def reset_object_file():
    '''
    description : this function for predict function to reset the object parameter for multi input image
    :return: void
    '''
    object_file.all_objects_as_dic={"/": [], "0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [],"arrow head": [], "state condition": [], "loop back arrow": [], "state": [], "straight arrow": [],"curved arrow": []}
    object_file.object_id = 0
#======================================================================================================================#
def first_step_config():
    '''
    description : first step configuration , loading the infer models
    :return: void
    '''
    ###############################
    #   Load the model
    ###############################
    os.environ['CUDA_VISIBLE_DEVICES'] = "0" # use the gpu bus

    # ============================== use infer model ===========================#

    # =================================load infer model =============================#
    object_file.model_1 = load_model_1("weights/state_condition_and_slash.h5")  # use the infer model(see train file) with saved weights
    object_file.model_2 = load_model_2("weights/state_loop_back.h5")  # use the infer model(see train file) with saved weights0
    object_file.model_3 = load_model_3("weights/arrow_head.h5")  # use the infer model(see train file) with saved weights
    object_file.model_4 = load_model_4("weights/arrows.h5")  # use the infer model(see train file) with saved weights
    object_file.model_5 = load_model_5("weights/inclined.h5")
#==================================================== main ============================================================#
def _main_(input_path_x,infer_model,infer_model_2,infer_model_3,infer_model_4,infer_model_5):
    '''
    description : main function for predict the anchors on the image using the infer models and anchors of yolo v3 for this labels


    :param input_path_x:the input path of the image , text (str)
    :param infer_model: infer model 1, .h5
    :param infer_model_2:infer model 2, .h5
    :param infer_model_3:infer model 3, .h5
    :param infer_model_4:infer model 4, .h5
    :return:void
    '''
    input_path   = input_path_x # get the input path from the args
    ###############################
    #   Set some parameter
    ###############################
    net_h, net_w = 416, 416 # a multiple of 32, the smaller the faster
    obj_thresh, nms_thresh = 0.90, .3  #obj_thresh = .5 mean if less than 50% sure ignore it, nms_thresh =.3 means if 30 % IOU for 2 boxes; merge them


    #===========================================================================#
    ###############################
    #   Predict bounding boxes 
    ###############################
    #============================================ for video ===========================================================#

    #==================================================================================================================#
    #============================================ for image ===========================================================#
    if True: # do detection on an image or a set of images
        image_paths = []
        #==================================== image path ==============================================================#
        if os.path.isdir(input_path): 
            for inp_file in os.listdir(input_path): # get the input image
                image_paths += [input_path + inp_file] # get the input image
        else:
            image_paths += [input_path] # relative address

        image_paths = [inp_file for inp_file in image_paths if (inp_file[-4:] in ['.jpg', '.png', 'JPEG'])]#image format
        #==============================================================================================================#


        ############################# anchors intialiazation ############################################
        model_1_anchors=[4,13, 5,14, 6,12, 6,16, 20,25, 22,21, 27,15, 31,25, 35,17]                     #
        model_2_anchors=[26,35, 26,54, 28,36, 34,62, 35,46, 38,23, 43,80, 51,58, 58,90]                 #
        model_3_anchors=[55,69, 75,234, 133,240, 136,129, 142,363, 203,290, 228,184, 285,359, 341,260]  #
        #model_4_anchors=[6, 88, 9, 53, 11, 168, 44, 9, 49, 77, 66, 15, 80, 67, 97, 26, 153, 11]        #
        model_4_anchors=[7,65, 11,159, 36,9, 49,77, 50,15, 65,8, 78,15, 107,27, 161,11]                 #
        model_5_anchors=[18,47, 64,70, 71,71, 74,13, 74,52, 75,26, 76,79, 80,45, 105,103]               #
        #################################################################################################

        ################################## labels intialiazation ######################################
        model_1_label=["/","state condition"]                                                         #
        model_2_label=["loop back arrow","state"]                                                     #
        model_3_label=["arrow head"]                                                                  #
        model_4_label=["curved arrow","straight arrow"]                                               #
        model_5_label=["straight arrow"]
        ###############################################################################################

        ############################################ the main loop ################################################################
        for image_path in image_paths:

            image = cv2.imread(image_path)# load the image path
            image=image_preprocess.start_pre(image,condition=object_file.hand_written)
            image = cv2.resize(image,(1600,1200))

            ########################################## predict the bounding boxes ##################################################
            ######################################### predict box for infer model_1 ################################################
            boxes = get_yolo_boxes(infer_model, [image], net_h, net_w, model_1_anchors, obj_thresh, nms_thresh)[0]      #
                                                                                                                                   #
            ######################################### predict box for infer model_2 ################################################
            boxes_2=get_yolo_boxes(infer_model_2, [image], net_h, net_w, model_2_anchors, obj_thresh, nms_thresh)[0]  #
                                                                                                                                   #
            ######################################### predict box for infer model_3 ################################################
            boxes_3 =get_yolo_boxes(infer_model_3, [image], net_h, net_w, model_3_anchors, obj_thresh, nms_thresh)[0] #
                                                                                                                                   #
            ######################################### predict box for infer model_4 ################################################
            boxes_4 =get_yolo_boxes(infer_model_4, [image], net_h, net_w, model_4_anchors, obj_thresh, nms_thresh)[0] #
                                                                                                                                   #
            ########################################################################################################################
            boxes_5 =get_yolo_boxes(infer_model_5, [image], net_h, net_w, model_5_anchors, obj_thresh, nms_thresh)[0] #
                                                                                                                                   #
            ########################################################################################################################

            ######################## draw boxes after predict ####################
            ######################################################################
            # draw bounding boxes on the image using labels model 1              #
            config_boxes(image, boxes, model_1_label, obj_thresh)      #
                                                                                 #
            # draw bounding boxes on the image using labels model 2              #
            config_boxes(image, boxes_2, model_2_label, obj_thresh)  #
                                                                                 #
            # draw bounding boxes on the image using labels model 3              #
            config_boxes(image, boxes_3, model_3_label, obj_thresh)  #
                                                                                 #
            # draw bounding boxes on the image using labels model 4              #
            config_boxes(image, boxes_4, model_4_label, obj_thresh)  #
                                                                                 #
            # draw bounding boxes on the image using labels model 5              #
            config_boxes(image, boxes_5, model_5_label, obj_thresh)  #
                                                                                 #
            ######################################################################
            ######################################################################


            #=====================set the exported path================================================#
            set_inputpath_and_image(image,image_path)#get the input image path as array removing the image name.type
            #=====================================================================#
#======================================================================================================================#
def predict_main(input_path):
    '''
    description : this function is main function, the GUI call it and it's predict the anchors and draw on the image
    :param input_path: the image input path, text(str)
    :return: string "predict"
    '''
    image_path = input_path
    _main_(image_path,object_file.model_1,object_file.model_2,object_file.model_3,object_file.model_4,object_file.model_5) # call the main
    #=====================================================================#
    image_operations.update_image()
    #---------------------------------------------------------------------#
    return log_config.start_of_log()+"predict done"+log_config.end_of_log()
#======================================================================================================================#
if __name__ == '__main__':
    reset_object_file()
    first_step_config()

    print(log_config.start_of_log(),log_config.start_up_log())
    print(predict_main("test.png"))
    xml_creator.xml_output_path("test.xml")
    image_operations.set_output_path("predicted.png")
    image_operations.export_image()
    matching.connect_anchors()
    passed, text, img =matching.connect_transactions()
    print(text)
    transactionToVerilog.transactionToVerilog("Moudel_0",object_file.transaction)

