import enum


#################### Start of Node Creation code #################################

class conn_node_types(enum.Enum):
    Source = 0
    Destination = 1
    LoopBack = 2

class Node:
    """ This Class represents a particular state
        the states connected to it and
        the state inputs and outputs (State conditions)
    """

    ################# Start of Base Methods #################

    def __init__(self , stateID=0 ,connected_nodes = [] , connected_nodes_type = [] ,state_conditions = [] ,output_list = []):
        self.state_id = stateID
        self.connected_nodes = [] 
        self.connected_nodes_type = [] 
        self.state_conditions = [] 
        self.output_list = []
        
    ################# End of Base Methods #################
#################### End of Node Creation code #################################
