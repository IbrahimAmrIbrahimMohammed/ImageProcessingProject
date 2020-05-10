'''
@author ahmed hessuin
description : this file contain all classes used in another files
'''
#======================================================================================================================#
class Data:
    '''
    .data class data type
    .it's a data type for predicated anchor box on image
    :parameter name: type string of the label's name
    :parameter xmin: type int
    :parameter xmax: type int
    :parameter ymin: type int
    :parameter ymax: type int
    :parameter accuracy : the accuracy of the label predict
    :parameter id : every anchor get special id
    :parameter connected_id : list of all connected anchor id's

    '''
    def __init__(self,name,xmin,ymin,xmax,ymax,accuracy,ID=-1):
        self.name=name
        self.xmin=xmin
        self.xmax=xmax
        self.ymin=ymin
        self.ymax=ymax
        self.accuracy=accuracy
        self.id=ID
        self.connected_id=[]
        self.connected_anchor=[]



    def get_xmin(self):
        '''
        description : get the xmin as int
        :return: xmin
        '''
        return int(self.xmin)

    def get_xmax(self):
        '''
        description : get the xmax as int
        :return: xmax
        '''
        return int(self.xmax)

    def get_ymin(self):
        '''
        description : get the ymin as int
        :return: ymin
        '''
        return int(self.ymin)

    def get_ymax(self):
        '''
        description : get the ymax as int
        :return: ymax
        '''
        return int(self.ymax)

    def get_label(self):
        '''
        description : return the name of the anchor
        :return: name
        '''
        return str(self.name)

    def set_id(self,ID):
        '''
        description : set the id of the anchor
        :param ID: id number, type(int)
        :return: void
        '''
        self.id=ID

    def get_id(self):
        '''
        description : return the id of the anchor
        :return: anchor id, type (int)
        '''
        return self.id

    def set_connected_id(self,id):
        '''
        description : append an id of connected anchor
        :param id: connected anchor id , (int)
        :return: void
        '''
        self.connected_id.append(id)

    def set_connected_anchor(self,anchor):
        self.connected_anchor.append(anchor)

    def get_connected_anchor(self):
        return self.connected_anchor

    def get_name(self):
        return self.name

    def get_connected_id(self):
        return self.connected_id
#======================================================================================================================#
class Transaction:
    '''
    this class contain the transaction between two states
    '''
    def __init__(self):
        self.src=int()
        self.dist= int()
        self.output= str()
        self.input= str()


    def set_src(self,src):
        self.src=src

    def set_dist(self,dist):
        self.dist=dist

    def set_input(self,input):
        self.input=input

    def set_output(self,output):
        self.output=output
#======================================================================================================================#
