######## Imports ########
import sys
import xml.etree.ElementTree as et
from node import *
import argparse

######## Command line command definition ########
parser = argparse.ArgumentParser(description='Enter File Path.')
parser.add_argument('--path', nargs='?', default='a.xml')
filename = parser.parse_args().path

######## XML file reading ########
tree = et.parse(filename)
root = tree.getroot()

######## Global Variables ########
states = []
number_in_out=0


########################## Start of conversion (XML --> Verilog) ##########################

######## Traverse each tag in a transaction to create a Node object (which represents a state) ########
for transaction in root:
    tempSrc=0
    tempDst=0
    stateCndtn = []
    srcExist=False
    dstExist=False

    for indx , child in enumerate(transaction):
        flag=False
        if child.tag == 'src':
            srcExist=True
            for index , state in enumerate(states):
                if state.state_id == child.text:
                    tempSrc=index
                    flag = True
                    break
            if flag == False:
                tempSrc = len(states)
                states.append(Node(child.text))
                
        if child.tag == 'dst':
            dstExist=True
            for index , state in enumerate(states):
                if state.state_id == child.text:
                    tempDst=index
                    flag = True
                    break
            if flag == False:
                tempDst = len(states)
                states.append(Node(child.text))
            
        if srcExist and dstExist:
            srcExist=False
            dstExist=False
            if tempDst == tempSrc:
                states[tempSrc].connected_nodes.append(
                states[tempSrc].state_id)
                states[tempSrc].connected_nodes_type.append(
                conn_node_types.LoopBack)
                
            else:
                states[tempSrc].connected_nodes.append(states[tempDst].state_id)
                states[tempSrc].connected_nodes_type.append(conn_node_types.Destination)
                
                states[tempDst].connected_nodes.append(states[tempSrc].state_id)
                states[tempDst].connected_nodes_type.append(conn_node_types.Source)
            
        
        if child.tag == 'input':
            stateCndtn.append((child.text , transaction[indx+1].text))
        if child.tag == 'output':
            pass

    number_in_out = len(stateCndtn)
    states[tempSrc].state_conditions.append(stateCndtn)
    if not tempDst == tempSrc:
        states[tempDst].state_conditions.append(stateCndtn)   
           

########################## Output verilog file template ##########################


output_file ='module '+filename.replace('.xml' , '') + '( clk , '
for i in range(0,number_in_out):
    output_file = output_file + 'IN_'+ str(i) +' , '

for i in range(0,number_in_out):
    output_file = output_file + 'OUT_'+ str(i) +' , '

output_file = output_file.rstrip(' , ')
output_file = output_file + ');\n'
output_file = output_file + 'parameter\n'
i=0

for state in states:
    output_file = output_file + ' \tstate_'+state.state_id +' = '+ str(i) + ' ,\n '
    i=i+1

output_file = output_file.rstrip(' ,\n ')
output_file = output_file + ' ;\n'
output_file = output_file + 'input\n\tclk,\n'

for i in range(0,number_in_out):
    output_file = output_file + '\tIN_'+ str(i) +' ,\n '

output_file = output_file.rstrip(' ,\n ')
output_file = output_file + ' ;\n'
output_file = output_file + 'output reg\n'

for i in range(0,number_in_out):
    output_file = output_file + '\tOUT_'+ str(i) +' ,\n '

output_file = output_file.rstrip(' ,\n ')
output_file = output_file + ' ;\n'
output_file = output_file + ' reg state;\n'
output_file = output_file + '\n initial\t state = state_' + str(states[0].state_id)+';\n'
output_file = output_file + '\n always@ (posedge clk)\n'
output_file = output_file + '\n case(state)\n'


for state in states:
    output_file = output_file + '\tstate_'+str(state.state_id)+':\n'
    output_file = output_file + '\tbegin\n'
    for index , dest in enumerate(state.connected_nodes):
        if not state.connected_nodes_type[index] == conn_node_types.Source:
            output_file = output_file + '\t\tif('
            i=0
            for inp in state.state_conditions[index]:
                output_file = output_file + 'IN_' + str(i) + "== 1'b" +str(inp[0]) + ' && '
                i=i+1 
            output_file = output_file.rstrip(' && ')
            output_file = output_file + ')\n'
            output_file = output_file + '\t\tbegin\n'
            i=0
            for outp in state.state_conditions[index]:
                output_file = output_file + '\t\t\tOUT_'+ str(i)+' = ' + str(outp[1])+' ;\n'
                i=i+1
            output_file = output_file + '\t\t\tstate = state_'+str(dest)+';\n'
            output_file = output_file + '\t\tend\n'
    output_file = output_file + '\tend\n\n'
output_file = output_file + ' endcase\nendmodule\n'


verilogfile = open(filename.replace(".xml" , ".v") , 'w')
verilogfile.write(output_file)

