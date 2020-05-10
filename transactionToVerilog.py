import sys
from node import *
from utils import object_file
from utils import log_config
def transactionToVerilog(moduleName="Module_0", listOfTransactions=[]):
    if object_file.valid_verilog:
        # listOfTransactions element[0]={"src_id":value , "dst_id":value , "input":value , "output": value}
        states = []

        for transaction in listOfTransactions:
            tempSrc = 0
            tempDst = 0
            srcExist = False
            dstExist = False

            for index, state in enumerate(states):
                if state.state_id == transaction["src_id"]:
                    tempSrc = index
                    srcExist = True
                    break
            if srcExist == False:
                tempSrc = len(states)
                states.append(Node(transaction["src_id"]))

            for index, state in enumerate(states):
                if state.state_id == transaction["dst_id"]:
                    tempDst = index
                    dstExist = True
                    break
            if dstExist == False:
                tempDst = len(states)
                states.append(Node(transaction["dst_id"]))

            stateCndtn = (transaction["input"], transaction["output"])

            states[tempSrc].state_conditions.append(stateCndtn)
            states[tempSrc].connected_nodes.append(states[tempDst].state_id)

            if tempDst == tempSrc:
                states[tempSrc].connected_nodes_type.append(conn_node_types.LoopBack)

            else:
                states[tempSrc].connected_nodes_type.append(conn_node_types.Destination)

                states[tempDst].state_conditions.append(stateCndtn)
                states[tempDst].connected_nodes.append(states[tempSrc].state_id)
                states[tempDst].connected_nodes_type.append(conn_node_types.Source)

        ##########################Output verilog file########################

        output_file = 'module ' + moduleName + '( clk , INPUT , OUTPUT );\n'
        output_file = output_file + 'parameter\n'
        i = 0
        for state in states:
            output_file = output_file + ' \tstate_' + state.state_id + ' = ' + str(i) + ' ,\n '
            i = i + 1
        output_file = output_file.rstrip(' ,\n ')
        output_file = output_file + ' ;\n'
        output_file = output_file + 'input\n\tclk;\ninput '

        if not len(states[0].state_conditions[0][0]) == 1:
            output_file = output_file + '[' + str(len(states[0].state_conditions[0][0]) - 1) + ':0]'
        output_file = output_file + 'INPUT;\n'

        output_file = output_file + 'output reg\t'
        if not len(states[0].state_conditions[0][1]) == 1:
            output_file = output_file + '[' + str(len(states[0].state_conditions[0][1]) - 1) + ':0]'
        output_file = output_file + ' OUTPUT;'

        output_file = output_file + ' reg state;\n'
        output_file = output_file + '\n initial\t state = state_' + str(states[0].state_id) + ';\n'
        output_file = output_file + '\n always@ (posedge clk)\n'
        output_file = output_file + '\n case(state)\n'
        for state in states:
            output_file = output_file + '\tstate_' + str(state.state_id) + ':\n'
            output_file = output_file + '\tbegin\n'
            for index, dest in enumerate(state.connected_nodes):
                if not state.connected_nodes_type[index] == conn_node_types.Source:
                    output_file = output_file + '\t\tif(INPUT == '
                    output_file = output_file + str(len(state.state_conditions[index][0])) + "'b" + str(state.state_conditions[index][0])
                    output_file = output_file + ')\n'
                    output_file = output_file + '\t\tbegin\n'
                    output_file = output_file + '\t\t\tOUTPUT = ' + str(len(state.state_conditions[index][1])) + "'b" + str(state.state_conditions[index][1])
                    output_file = output_file + ";\n\t\t\tstate = state_" + str(dest) + ';\n'
                    output_file = output_file + '\t\tend\n'
            output_file = output_file + '\tend\n\n'
        output_file = output_file + ' endcase\nendmodule\n'

        output_file_v=open('Verilog_code.v',"w")
        output_file_v.write(output_file)
        output_file_v.close()
        return log_config.start_of_log()+"verilog code exported"+log_config.end_of_log()

    else:
        return log_config.start_of_log()+"error please check again before generating the verilog code"+log_config.end_of_log()

