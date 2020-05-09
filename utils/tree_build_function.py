'''
@author ahmed hessuin
description : build an xml tree file
'''
import xml.etree.cElementTree as ET
#======================================================================================================================#
def build_a_tree(anno_tag,data):
    '''
    description : building the xml tree with tags from the data
    :param anno_tag: start up tag fixed input
    :param data: transaction , list of dictionary
    :return:
    '''
    # for every object

    object = ET.SubElement(anno_tag, "transaction")

    # sub elements

    # ========================================================#

    #state id
    ET.SubElement(object, "src").text = data["src_id"]
    ET.SubElement(object, "dst").text = data["dst_id"]
    ET.SubElement(object, "input").text = data["input"]
    ET.SubElement(object, "output").text = data["output"]
#======================================================================================================================#
