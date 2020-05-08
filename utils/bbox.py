'''
@author sara khaked
'''
#commented by sara khaled 
import numpy as np
from utils import object_file #my files
from utils import anchor_sub_file
#======================================================================================================================#
class BoundBox:
    #the bound box class
    def __init__(self, xmin, ymin, xmax, ymax, c = None, classes = None):
        self.xmin = xmin#xmin
        self.ymin = ymin#ymin
        self.xmax = xmax#xmax
        self.ymax = ymax#ymax
        
        self.c       = c#defult = none
        self.classes = classes#classes

        self.label = -1#label =-1
        self.score = -1#label =-1

    def get_label(self):
        if self.label == -1:#if there is no label
            self.label = np.argmax(self.classes)#get argmax of classes
        
        return self.label#return the label
    
    def get_score(self):
        if self.score == -1:#if the score =-1
            self.score = self.classes[self.get_label()]#get the classes[label]
            
        return self.score      #return the score
#============================================== interval overlap ======================================================#
def _interval_overlap(interval_a, interval_b):
    x1, x2 = interval_a # we have interval a
    x3, x4 = interval_b # we have interval b


    #interval a = x
    #interval b = o


    #  x3         x4         x1               x2   --------> case 1

    #  x3         [x1         x4]             x2   --------> case 2
    #  x3         [x1         x2]             x4   --------> case 2

    #  x1          x2        x3               x4   --------> case 3

    #  x1         [x3        x2]               x4  --------> case 4
    #  x1         [x3        x4]               x2  --------> case 4
    #


    #to make sure if we have overlap or no
    if x3 < x1: # case 1 , case 2
        if x4 < x1:#case 1
            return 0 #case 1 no overlap
        else:
            return min(x2,x4) - x1 #case 2 get the overlap [   ]
    else:# case 3 , case 4
        if x2 < x3:#case 3
             return 0#no overlap
        else:#case 4
            return min(x2,x4) - x3 #overlap [       ]
#======================================================================================================================#
#===========================================intersection over union ===================================================#
def bbox_iou(box1, box2):
    '''
    description : getting to2 boxes define if they are overlapped or no, core function in predict the anchors
    :param box1: box1, bound box class
    :param box2: box2, bound box class
    :return: the intersection over union, float
    '''
    intersect_w = _interval_overlap([box1.xmin, box1.xmax], [box2.xmin, box2.xmax])#get the intersected W
    intersect_h = _interval_overlap([box1.ymin, box1.ymax], [box2.ymin, box2.ymax])#get the intersected H
                    #--------------------------------------------------------------#
    intersect = intersect_w * intersect_h# intersected area
                    #--------------------------------------------------------------#
    w1, h1 = box1.xmax-box1.xmin, box1.ymax-box1.ymin # w1 , h1
    w2, h2 = box2.xmax-box2.xmin, box2.ymax-box2.ymin # w2 , h2
    
    union = w1*h1 + w2*h2 - intersect # the total area common (union)

    if intersect==0:#if intersected ==0 is a special condition we made to solve issue in the code done by ahmed hessuin
        return 0#retun 0
    return float(intersect) / union # return the intersected area over the union area
#======================================================================================================================#
#===========================================get label and accuracy as string ==========================================#
def cut_word_to_label_accuracy(string):
    '''
    description : geting string and cut it into name and accuracy
    :param string: input string , text(str)
    :return: name(str),accuracy(str)
    '''
    string=str(string)#focr cast the input as string
    string=string.split()#split the string based on the space
    label="" #empty label

    for i in range(len(string)-1):#for the range of the string except the last element
        if i==0:#first loop
            label=string[i]#append first element in the list to the label, example ->["arrow","head","85%"]
        else:
            label=label+" "+string[i]# append every string to the label name

    accuracy=string[-1]#accuracy is the last element in string list, example ->["arrow","head","85%"]
    accuracy=accuracy[0:len(accuracy)-1]#accuract with out the "%"

    return label,accuracy #return the label and the accuracy
#============================================== draw boxes ============================================================#
def config_boxes(image, boxes, labels, obj_thresh, quiet=True):
    '''
    description :  adding the predicated anchors to all_object_as_dic based on the anchor label.

    :param image: input image, np.array
    :param boxes: anchors, anchor
    :param labels: anchor label, text(str)
    :param obj_thresh: threshold if less than this threshold ignore this anchor, float
    :param quiet: optional, boolean
    :return: returning the input image, np.array
    '''
    # draw the box with cv2 function rectangle
    for box in boxes:
        label_str = ''
        label = -1
        for i in range(len(labels)):
            if box.classes[i] > obj_thresh:
                if label_str != '': label_str += ', '
                label_str += (labels[i] + ' ' + str(round(box.get_score()*100, 2)) + '%')
                label = i
            if not quiet: print(label_str)
                
        if label >= 0:
            label_str,accuracy= cut_word_to_label_accuracy(label_str)

            if (label_str)==("state") :
                #waiting error indicate
                pass
            elif (label_str)==("/") :
                #waiting error indicate
                pass
            elif (label_str)==("loop back arrow"):
               #error indicate
                if box.xmax-box.xmin<30:
                    continue
            elif (label_str)==("state condition") :
                #error indicate
                if box.xmax-box.xmin<19:
                    continue

            elif (label_str)==("arrow head"):
                #waiting error indicate
                pass

            elif (label_str) == ("straight arrow") or (label_str) == ("curved arrow"):
                #waiting error indicate
                pass

            else :
                print("fetal error")





            object_file.all_objects_as_dic[str(label_str)].append(
                object_file.DC.Data(str(label_str),
                                    str(box.xmin), str(box.ymin),
                                    str(box.xmax), str(box.ymax),
                                    str(accuracy),object_file.object_id))  # insert the anchor in the dictionary

            object_file.object_id=object_file.object_id+1


            if str(label_str)=="state condition":
                anchor_sub_file.get_inputs_outputs_slash_for_state_condition(image[box.ymin:box.ymax,box.xmin:box.xmax],box.xmin,box.ymin,"state condition")

            if str(label_str)=="state":
                anchor_sub_file.get_inputs_outputs_slash_for_state_condition(
                    image[box.ymin:box.ymax, box.xmin:box.xmax], box.xmin, box.ymin,"state")

    return image
#======================================================================================================================#
