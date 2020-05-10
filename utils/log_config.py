'''
@author ahmed hessuin
this file for log configuration
like get time and the format.
'''
from datetime import datetime
#======================================================================================================================#
def start_of_log():
    '''
    description : get the current time and return it as string in format of H : M : S  :
    :return: void
    '''
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return  "["+current_time+"]" +" : "
#======================================================================================================================#
def end_of_log():
    '''
    description : add new line
    :return: void
    '''
    return "\n"
#======================================================================================================================#
def start_up_log():
    '''
    description : start up msg
    :return: tip and start up msg
    '''
    msg="welcome, please follow the tips for this program\n" \
        "1)load the image with button load image.\n" \
        "2)after getting the image press predict and please wait till finish loading.\n" \
        "3)if there is object ( arrow , state ...)not detected, please add it with add anchor\n" \
        "4)if there is object falsely detected, please remove it with remove anchor\n" \
        "5)push button check\n" \
        "6)if there is an error msg, please fix the error indicated on the image,most\nlikely to be an anchor not connected with another one (state condition anchor must have common area\nwith the arrows)\n" \
        "7)if there is no error msg, please check state names and the conditions\n" \
        "8)well, finally push button get verilog file\n" \
        "9)fell free to load new image again and use the GUI again\n" \
        "GOOD LUCK\n"

    return msg
#======================================================================================================================#