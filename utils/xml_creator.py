'''
@author ahmed hessuin
description : file for xml creation
'''
import xml.etree.cElementTree as ET
from utils import tree_build_function as TR
from utils import object_file
from utils import  image_operations
import cv2
#======================================================================================================================#
def create_the_tree():
    '''
    description : this function build the xml file with annotation as head.
    using all_object_as_dic as it's source list
    :return: void
    '''
    #create annotation
    annotation = ET.Element("annotation")
    #=================================================#
    for transaction in object_file.transaction:
        TR.build_a_tree(annotation,transaction)
    #=================================================#
    tree = ET.ElementTree(annotation) # end the annotation
    tree.write(object_file.output_path_xml)#export the xml file based on the xml output path
#======================================================================================================================#
def xml_output_path(new_xml_path):
    '''
    description : set the xml output path
    :param new_xml_path: set the xml output path, string
    :return: void
    '''
    object_file.output_path_xml=new_xml_path
#======================================================================================================================#
