
'''
File Description: This file consists reference model which used in verifying the design

TODO:
Task Description: Add logic for all instructions. One instruction is implemented as an example. 
                  Note - The value of ANDN in bbox.defines is a temp value, it needed to be changed according to spec.

Note - if instr has single operand, take rs1 as an operand
'''

#Reference model
def bbox_rm(instr, rs1, rs2, XLEN):
    
    if instr == 1:
        res = rs1 & ~rs2
        valid = '1'
    ## logic for all other instr starts 

    ##elif instr == 2:






    ## logic for all other instr ends
    else:
        res = 0
        valid = '0'

    if XLEN == 32:
        result = '{:032b}'.format(res)
    elif XLEN == 64:
        result = '{:064b}'.format(res)

    return valid+result

