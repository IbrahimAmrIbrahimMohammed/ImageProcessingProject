'''
@author ahmed hessuin
description : this file for matching and connecting the anchors together to get the transactions write
'''
from utils import object_file
from utils import log_config
from utils import image_operations
import cv2

#======================================================================================================================#
def add_state_id(element):
    '''
    description : add a state id as element to the dictionary
    :param element: element of type Data
    :return: void
    '''
    object_file.all_objects_as_dic['9'].append(element)
#======================================================================================================================#
def interval_overlap(first_element_coordinate_min,first_element_coordinate_max,
                     second_element_coordinate_min,second_element_coordinate_max):
    '''
    description : this check if there is an intersection between 2 intervals as x1,x2 is the first interval and x3,x4 is
    the second interval
    :param first_element_coordinate_min: the first interval min value, type(int)
    :param first_element_coordinate_max: the first interval max value, type(int)
    :param second_element_coordinate_min: the second interval min value, type(int)
    :param second_element_coordinate_max: the second interval max value, type(int)
    :return: 1 if there is an intersection, 0 if there is no intersection ,type(int)
    '''
    x1=first_element_coordinate_min
    x2 = first_element_coordinate_max  # we have interval a
    x3=second_element_coordinate_min
    x4 = second_element_coordinate_max  # we have interval b

    # first interval     [        ]
    # second interval    (        )

    # [x3         x4]       (x1               x2)   --------> case 1

    # [x3         (x1         x4]             x2)   --------> case 2
    # [x3         (x1         x2)             x4]   --------> case 2

    # (x1          x2)      [x3                x4]  --------> case 3

    # (x1         [x3        x2)               x4]  --------> case 4
    # (x1         [x3        x4]               x2)  --------> case 4
    #

    # to make sure if we have overlap or no
    if x3 < x1:  # case 1 , case 2
        if x4 < x1:  # case 1
            return 0  # case 1 no overlap
        else:
            return min(x2, x4) - x1  # case 2 get the overlap [   ]
    else:  # case 3 , case 4
        if x2 < x3:  # case 3
            return 0  # no overlap
        else:  # case 4
            return min(x2, x4) - x3  # overlap [       ]

#======================================================================================================================#
def area_of_intersection(first_element,second_element):

    interval_overlap_in_x=interval_overlap(first_element.get_xmin(),first_element.get_xmax(),
                                           second_element.get_xmin(),second_element.get_xmax())
    interval_overlap_in_y=interval_overlap(first_element.get_ymin(),first_element.get_ymax(),
                                           second_element.get_ymin(),second_element.get_ymax())

    intersection_area=interval_overlap_in_x * interval_overlap_in_y
    return intersection_area

#======#
def connect_arrow_head_with_one_arrow(arrow_head):
    min_area=-1
    previous_element=None
    for element in arrow_head.get_connected_anchor():

        if element.get_name()!="state":
            #curved arrow, straight arrow, loop back arrow, incline
            intersection_between_arrow_head_and_arrow=area_of_intersection(arrow_head,element)
            if intersection_between_arrow_head_and_arrow > min_area:
                min_area=intersection_between_arrow_head_and_arrow #keep this arrow and update min
                if previous_element==None:
                    previous_element=element
                else:
                    arrow_head.get_connected_anchor().remove(previous_element)  # remove this element from the connected elements
                    previous_element=element


            else:
                arrow_head.get_connected_anchor().remove(element) #remove this element from the connected elements

#=====#
def get_state_from_arrow_head(arrow_head):
    for element in arrow_head.get_connected_anchor():
        if element.get_name()=="state":
            return element

#=======#
def clean_inclined_line(arrow_head,inclined_arrow):
    the_state_in_the_arrow_head=get_state_from_arrow_head(arrow_head)

    for element in inclined_arrow.get_connected_anchor():
        if element.get_name()=="state":#if it's a state
            if element != the_state_in_the_arrow_head:  # if not the core state
                interval_overlap_in_x = interval_overlap(element.get_xmin(), element.get_xmax(),
                                                         the_state_in_the_arrow_head.get_xmin(),
                                                         the_state_in_the_arrow_head.get_xmax())
                interval_overlap_in_y = interval_overlap(element.get_ymin(), element.get_ymax(),
                                                         the_state_in_the_arrow_head.get_ymin(),
                                                         the_state_in_the_arrow_head.get_ymax())

                if interval_overlap_in_y ==0  and interval_overlap_in_x==0:#this is the src state
                    keep_this_state=1
                else:
                    inclined_arrow.get_connected_anchor().remove(element)# remove this state



#======#
def connect_anchors():
    '''
    description : this function search which anchor inside the other
    using the dictionary in all object
    the "/" search which "state condition", it's inside
    the "state condition" search which "arrow", it's connected with
    the "arrow: search which "state", it's connected with
    the "arrow head" search which "state", "loop back arrow" and "arrow", it's connected with
    then every anchor get the id and the address of all connected anchors, based on the decision described above.
    the small object searching in the big object, and adding the small object to connected list of big object unless
    it's an arrow head.
    :return: void
    '''

    for key in object_file.all_objects_as_dic.keys():
        for element in object_file.all_objects_as_dic[key]:
            element.get_connected_anchor().clear()

    for key in object_file.all_objects_as_dic.keys():
        second_key = []
        # ===============set the second key=======================#
        if key == "/":
            second_key.append("state condition")

        elif key == "state condition":
            second_key.append("loop back arrow")
            second_key.append("straight arrow")
            second_key.append("curved arrow")

        elif key == "straight arrow" or key == "curved arrow":
            second_key.append("state")
            # second_key.append("state condition")

        elif key == "arrow head":
            second_key.append("state")
            second_key.append("straight arrow")
            second_key.append("curved arrow")
            second_key.append("loop back arrow")

        elif key == "0" or key == "1" or key == "2" or key == "3" or key == "4" or key == "5" \
                or key == "6" or key == "7" or key == "8" or key == "9":
            second_key.append("state")
            second_key.append("state condition")

        # ===================================================#
        for element in object_file.all_objects_as_dic[key]:  # for every anchor in the key in the dictionary,for example  ->id=1, name= "/" .... if key ="/"
            # start search on the target key (second_key)
            for second_key_ in second_key:  # for every second_key for example ->"state condition" if key = "/"
                for second_element in object_file.all_objects_as_dic[second_key_]:  # for every anchor in the second_key ->name=state condition, xmin=x, ymin =y, id =z ...
                    # ============================= matching loop ======================================#
                    # the second element is the second_key element, in this example the state condition

                    #check overlap in x and overlap in y
                    overlap_in_x=interval_overlap(element.get_xmin(),element.get_xmax(),
                                                  second_element.get_xmin(),second_element.get_xmax())

                    overlap_in_y = interval_overlap(element.get_ymin(), element.get_ymax(),
                                                    second_element.get_ymin(),second_element.get_ymax())
                    connected_area=overlap_in_x*overlap_in_y
                    if connected_area>0:

                        element.set_connected_id(
                            second_element.get_id())  # add the id of the big anchor as connected in the small anchor
                        element.set_connected_anchor(
                            second_element)  # add this anchor as data type(data) in the list of connected anchors
                        if key == "arrow head" or key == "state":
                            #don't append the second element, thus lines will never see that head arrow is connected to it
                            #key==state, will never happen as state never search but used it to make sure what keys are
                            #neglected from the second element append
                            continue
                        else:
                            second_element.set_connected_id(
                                element.get_id())  # add the id of the small anchor as connected in the big anchor
                            second_element.set_connected_anchor(
                                element)  # add this anchor as data type(data) in the list of connected anchors

                        # ===================================================================================#
            if key=="arrow head":
                connect_arrow_head_with_one_arrow(element) # if it's an arrow head, clear it
#======================================================================================================================#
def sort_anchors(anchors):
    '''
    description : sort anchors based on x_min
    :param anchors: list of anchors, type: list(DATA}
    :return: anchors: list of anchors, type: list(DATA}
    '''

    def sort_function(x):
        '''
        description : this function is key for sorted function
        :param x: element in list, type: DATA
        :return: x.min_x, type: int
        '''
        return x.get_xmin()

    sorted_anchors= sorted(anchors,key=sort_function )
    return  sorted_anchors
#======================================================================================================================#
def get_src_element(dst_id, list_of_anchors):
    '''
    description : function get the src anchor (the src state)
    most likely to be called from the arrow, list of anchors -> the connected state with this arrow anchor
    :param dst_id: the id of the dst sate, int
    :param list_of_anchors: list of all connected anchors with this arrow, Data
    :return: the src state for this dst state, Data
    example: arrow id=5, connected with state id =1 and state id=2
    dst state id=1,
    search in the for loop to get the state which doesn't have state id = 1 (search for state 2 )
    '''
    for element in list_of_anchors:  # for loop inside every anchor in the list of anchors
        if element.get_id() == dst_id:  # if the id of connected state with this line equal to the dst state
            continue  # ignore it, we need the other connected state
        else:  # else we are at the another state
            if element.get_name()=="state":
                return element  # return this state as src state
#======================================================================================================================#
def get_state_id(state):
    '''
    description : get the state id from the user image example -> state ( 12 ) this function will return [1,2] as
    this state id or state( 12 )->[2,1] as it's not sorted in this function. see sort anchors for soring
    :param state: anchor with label name 'state', type:Data
    :return: state_id, a list containing the state id as string elements, example->[1,2,3] or [1,3,2] is for state id 123
    '''
    state_id=[]
    for element in state.get_connected_anchor():#in every element in connected list of input state
        if element.get_name()=="0" or element.get_name()=="1" or element.get_name()=="2" or element.get_name()=="3" or \
                element.get_name() == "4" or element.get_name()=="5" or element.get_name()=="6" or element.get_name()=="7" \
                 or element.get_name() == "8" or element.get_name()=="9" or element.get_name()[0]=="g":#element.get_name()[0]=="g", if the first charchter of the string is g
            state_id.append(element)# if the connected anchor name is 0 1 2 3 4 5 6 7 8 9 , get it and append in the state_id list

    return state_id
#======================================================================================================================#
def get_state_condition_input_output(state_condition):
    '''
    description : get the input out of state condition , example-> 10/11 this function will get [1,0,/,1,1] or [1,1,0,/,1]
    as the condition of this transaction by checking every connected element to this state condition with name 1,2,3,4,5,6,8,9,0,/
    , note that it's not sorted in this function, for sort check sort_anchors
    :param state_condition: anchor with name 'state condition', type: DATA
    :return:list of connected element with name as in description, type= list(DATA)
    '''
    state_condition_input_output = []
    for element in state_condition.get_connected_anchor():
        if element.get_name() == "0" or element.get_name() == "1" or element.get_name() == "2" or element.get_name() == "3" or \
                element.get_name() == "4" or element.get_name() == "5" or element.get_name() == "6" or element.get_name() == "7" \
                or element.get_name() == "8" or element.get_name() == "9" or element.get_name() == "/":
            state_condition_input_output.append(element)

    return state_condition_input_output
#======================================================================================================================#
def get_state_condition(arrow):
    '''
    description : get the state condition of arrow by searching in connected anchors of this arrow for anchor named
    "state condition" and return it
    :param arrow: anchor arrow, type : DATA
    :return: element, the state condition, type : DATA
    '''
    for element in arrow.get_connected_anchor():
        if element.get_name()=="state condition":
            return element
#======================================================================================================================#
def get_input_get_output(elements):
    '''
    description : get the input and output of state condition as string, by taking elements(anchors) sorted on
    it's x_min, example->[1,0,/,1,1], searching for the "/" then any element after the "/" is output, before it in input
    :param elements: sorted on x_min list of anchors, type : list(DATA)
    :return: string of input, string of output
    '''
    the_slash_x_min=-1

    input_str=""
    output_str=""

    for element in elements:#search for the "/"
        if element.get_name()=="/":
            the_slash_x_min=element.get_xmin()#get the x_min of the "/"
            break

    for element in elements:# in every element inside the state condition
        if element.get_xmin()<the_slash_x_min:#if this element x_min < the "/" x_min , then this is input
            input_str=input_str+element.get_name()# append this bit in the right, keeping the ordere of big wise bit

        if element.get_xmin() > the_slash_x_min:#if this element x_min > the "/" x_min , then this is output
            output_str = output_str + element.get_name()# append this bit in the right, keeping the ordere of big wise bit

    return input_str,output_str
#======================================================================================================================#
def get_state_id_as_string(elements):
    '''
    description : transfer  list of id anchors of state into string with respect ot it's order from left to right
    :param elements: list of elements ,list(Data)
    :return: string of the id, String
    '''

    state_id=""

    for element in elements:
        state_id=state_id+element.get_name()

    return state_id
#======================================================================================================================#
def generate_state_id_dumy(string,element):
    '''
    description : this function take the string of the id and it's state element and generate an element of type Data
    then append the state in it's connected anchors and append this id to the state connected anchors, the generated id
    must be inside the state with respect to it's center
    :param string: the id name, String
    :param element: the anchor state of this id, Data
    :return: the id as an element, Data
    '''
    element_x_center = (element.get_xmin() + element.get_xmax()) /2
    element_y_center = (element.get_ymin() + element.get_ymax()) / 2
    element_width  = (element.get_xmax()-element.get_xmin())
    element_height = (element.get_ymax() - element.get_ymin())
    width_ratio=10/100
    height_ratio = 10 / 100
    new_element_xmin=element_x_center-width_ratio*element_width
    new_element_xmax=element_x_center+width_ratio*element_width
    new_element_ymin=element_y_center-height_ratio*element_height
    new_element_ymax=element_y_center+height_ratio*element_height

    out_element=object_file.DC.Data(string,new_element_xmin,new_element_ymin,new_element_xmax,new_element_ymax,"99",object_file.object_id)

    out_element.get_connected_anchor().append(element)# add this element to the generated id element connected list
    element.get_connected_anchor().append(out_element)# add the generated id to the state's connected list

    object_file.object_id=object_file.object_id+1 # increment object id by 1
    return out_element
#======================================================================================================================#
def error_checking(src_element,dst_element,con_element,src_element_id,dst_element_id,con_element_input_output):
    '''
    description : check for errors in the transaction, like if there was no src or dst or transaction condition
    :param src_element: the src element, Data
    :param dst_element: the dst element, Data
    :param con_element: the state condition, Data
    :param src_element_id: the id of the src , String
    :param dst_element_id: the id of the dst , String
    :param con_element_input_output: the input and output condition ( 0 1 ) , Data
    :return: string "passed", or the error msg  also return 1 and -1 for success and fail, return the image hight_light, if there is an error
    '''
    error_msg = "the black anchors indicates where is the error\nit must have src_state, dst_state, condition.\n"
    high_light_errors_on_the_image = []
    dump_copy_of_the_image = object_file.image.copy()  # copy of the original image
    # check for error conditions
    src_test=-1
    dst_test=-1
    con_test=-1
    input_output_test=-1
    if src_element != None:
        src_element_id = sort_anchors(src_element_id)  # sort the list
        transaction_src_id = get_state_id_as_string(src_element_id)  # get the id as string
        high_light_errors_on_the_image.append({"xmin": src_element.get_xmin(), "xmax": src_element.get_xmax(),
                                               "ymin": src_element.get_ymin(), "ymax": src_element.get_ymax()})
        error_msg = error_msg + "it has src state id =  " + str(transaction_src_id) + "\n"
        src_test=1
    if dst_element != None:
        dst_element_id = sort_anchors(dst_element_id)
        transaction_dst_id = get_state_id_as_string(dst_element_id)
        error_msg = error_msg + "it has dst state id = " + str(transaction_dst_id) + "\n"
        high_light_errors_on_the_image.append({"xmin": dst_element.get_xmin(), "xmax": dst_element.get_xmax(),
                                               "ymin": dst_element.get_ymin(), "ymax": dst_element.get_ymax()})
        dst_test=1
    if con_element != None:
        con_element_input_output = sort_anchors(con_element_input_output)
        transaction_input, transaction_output = get_input_get_output(con_element_input_output)
        error_msg = error_msg + "it has condition = " + transaction_input + " / " + transaction_output + "\n"
        high_light_errors_on_the_image.append({"xmin": con_element.get_xmin(), "xmax": con_element.get_xmax(),
                                               "ymin": con_element.get_ymin(), "ymax": con_element.get_ymax()})
        con_test=1
        if transaction_input == "" or transaction_output == "":
            error_msg=error_msg + "it is missing input or output"+"\n"
        else:
            input_output_test=1




    if input_output_test ==-1 or src_test==-1 or dst_test==-1 or con_test==-1:
        for hightlight in high_light_errors_on_the_image:
            cv2.rectangle(img=dump_copy_of_the_image, pt1=(hightlight["xmin"], hightlight["ymin"]),

                          pt2=(hightlight["xmax"], hightlight["ymax"]),
                          color=[0, 0, 0], thickness=2
                          )
        return -1,error_msg ,dump_copy_of_the_image


    return 1,"passed",object_file.image
#======================================================================================================================#
def connect_transactions():
    '''
    description : this function match and find what is the src state , the dst state and the state condition for it.
    using arrow head as the only anchor that connect everything together (state with arrows), to find the src state
    and the line which is connected with this src state.
    from the arrow we find the state condition connected with it using get_state_condition_element function.
    if the arrow is loop back arrow the src state is the dst state.

    :return: a text of the current transaction or an error msg, string

    '''

    connected_transaction_as_string = "check transactions done :- \n" # the output text
    dump_id=0 # the dump id for a state without id
    object_file.transaction=[]# reset transaction before using this function
    object_file.valid_verilog = False
    changed=-1 # flag variable to determine update the image or no
    passed=-1 # the passing condition -1 failed, 1 success
    for element in object_file.all_objects_as_dic["arrow head"]: # for every arrow head, as it's the connecting element of the state and the line
        src_element = None
        dst_element = None
        con_element = None

        src_element_id=[]
        dst_element_id=[]
        con_element_input_output=[] # condition element inputs and outputs

        # search in state
        for x_element in element.get_connected_anchor():# for every element in the arrow head
            if x_element.get_name() == "state": # if this element is a state take it
                dst_element = x_element # this element is the dst element as the arrow connected with this state
                dst_element_id=get_state_id(dst_element) # get the state id as list of anchors
                break#break this loop

        for x_element in element.get_connected_anchor():# for every element in the arrow head
            if x_element.get_name() != "state": # if this element not a state, thus it's an straight arrow or loop back arrow or any kind of arrow
                if x_element.get_name() == "loop back arrow":#if it's loop back arrow
                    src_element = dst_element # the src element is the dst element
                    con_element = get_state_condition(x_element) # get the state condition for this arrow
                else:# if it's not an loop back arrow
                    src_element = get_src_element(dst_element.get_id(), x_element.get_connected_anchor())# get the src element as the another satet of this arrow
                    con_element = get_state_condition(x_element)# get the state condition for this arrow

                if src_element!=None :# if the src element  not None, we found a src state
                    src_element_id=get_state_id(src_element) # get the src state id as list of anchors

                if con_element !=None:# if the state condition not None, we found a state condition for this arrow
                    con_element_input_output = get_state_condition_input_output(con_element)# get the input and output as a list of anchors




        passed,error_msg,highlight_image=error_checking(src_element,dst_element,con_element,src_element_id,dst_element_id,con_element_input_output)#check for error
        if passed==-1:#not passed
            return passed,log_config.start_of_log()+(error_msg)+log_config.end_of_log(),highlight_image

        else:
            #passed
            con_element_input_output=sort_anchors(con_element_input_output)# sort the anchors of the input and output from left to right
            src_element_id=sort_anchors(src_element_id)#sort the anchors of the src state id from left to right
            dst_element_id=sort_anchors(dst_element_id)#sort the anchors of the dst state id from left to right


            transaction_input,transaction_output=get_input_get_output(con_element_input_output)#get the input and the output of the state from the anchors as string
            transaction_src_id=get_state_id_as_string(src_element_id)#get the src state id as string
            transaction_dst_id=get_state_id_as_string(dst_element_id)#get the dst state id as string

            #============================== another non fatel error checking ==============================================#
            if transaction_src_id=="" and transaction_dst_id!="": # if the src state id string is empty, but we have dst state id as string
                # if the state has no id generate one for it
                transaction_src_id="g_"+str(dump_id)# generating the id with tag g_ as string
                dump_id = dump_id + 1 # increment the dummy id
                gen_element_src_id=generate_state_id_dumy(transaction_src_id,src_element)# generate the id as element
                add_state_id(gen_element_src_id)# append this element in the dictionary
                changed=1# mark we changed on the image
                #=============================================================#
            if transaction_dst_id=="" and transaction_src_id!="":# if the dst state id string is empty, but we have src state id as string
                # if the state has no id generate one for it
                transaction_dst_id="g_"+str(dump_id)# generating the id with tag g_ as string
                dump_id = dump_id + 1# increment the dummy id
                gen_element_dst_id=generate_state_id_dumy(transaction_dst_id,dst_element)# generate the id as element
                add_state_id(gen_element_dst_id)#append this element in the dictionary
                changed=1# mark we changed on the image
                #=============================================================#
            if transaction_src_id=="" and transaction_dst_id=="":# if we didn't find a src id elements or dst id elements
                transaction_src_id="g_"+str(dump_id)# generate dump id as string 1
                dump_id = dump_id + 1#update the dump id
                transaction_dst_id = "g_" + str(dump_id)# generate dump id as string 2
                dump_id = dump_id + 1#update the dump id

                if src_element.get_xmin()== dst_element.get_xmin() and src_element.get_ymin()==dst_element.get_ymin():# if the src state and the dst state have the same xmin and ymin,thus this is the same condition
                    gen_element_src_id = generate_state_id_dumy(transaction_src_id, src_element)#just add one id
                    transaction_dst_id =transaction_src_id  # the dst id is the src id
                    add_state_id(gen_element_src_id)#add this id as an element
                    dump_id=dump_id-1#remove the extra dump id as not used

                else:# the two states are diffrent, not the same state
                    gen_element_src_id = generate_state_id_dumy(transaction_src_id, src_element)#generate the first id element
                    gen_element_dst_id = generate_state_id_dumy(transaction_dst_id, dst_element)#generate the second id element
                    add_state_id(gen_element_src_id)#add this element
                    add_state_id(gen_element_dst_id)#add this element
                changed=1 # mark that, we changed in the image
            #==============================================================================================================#

            if changed == 1:  # if we changed the image
                image_operations.update_image()  # update the image this for error pop up widget


            # we made it!!!, just add this transaction
            object_file.transaction.append({"src_id":"state_"+(transaction_src_id),
                                "dst_id":"state_"+(transaction_dst_id),
                                "input":str(transaction_input),
                                "output":str(transaction_output)})


            #add this transaction to the output msg
            connected_transaction_as_string= connected_transaction_as_string+"src state : "+(transaction_src_id)+", dst state : "+(transaction_dst_id)+",input : " +str(transaction_input)+ ", output : "+str(transaction_output)+"\n"


    #---------------------------------------------------------------------------#
    # we passed in every transaction #
    if changed == 1:#if we changed the image
        image_operations.update_image()#update the image

    object_file.valid_verilog=True #we can generate verilog code

    return passed,log_config.start_of_log()+connected_transaction_as_string+log_config.end_of_log(),object_file.image
#======================================================================================================================#




