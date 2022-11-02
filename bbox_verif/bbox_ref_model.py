#See LICENSE.iitm for license details
'''

Author   : Santhosh Pavan
Email id : santhosh@mindgrovetech.in
Details  : This file consists reference model which is used in verifying the bbox design (DUT).

--------------------------------------------------------------------------------------------------
'''
'''
TODO:
Task Description: Add logic for all instructions. One instruction is implemented as an example. 
                  Note - The value of instr (ANDN) is a temp value, it needed to be changed according to spec.

Note - if instr has single operand, take rs1 as an operand
'''

#Reference model
def bbox_rm(instr, rs1, rs2, XLEN):
    print(type(instr),type(rs1),type(rs2))
    if instr == 1:
        res = rs1 & ~rs2
        valid = '1'
    ## logic for all other instr starts 

    elif instr == 2:
        res = (rs1 & ~(1 << (rs2 & (XLEN - 1))))
        valid = '1'

    elif instr == 3:
        res = (rs1 & ~(1 << (instr[25:20] & (XLEN - 1))))
        valid = '1'

    elif instr == 5:
        res = (rs1 >> (rs2 & (XLEN - 1))) & 1
        valid = '1'
    
    elif instr == 6:
        res = (rs1 >> (instr[25:20] & (XLEN - 1))) & 1
        valid = '1'

    elif instr == 7:
        res = (rs1 ^ (1 << (rs2 & (XLEN - 1))))
        valid = '1'

    elif instr == 8:
        res = (rs1 ^ (1 << (instr[25:20] & (XLEN - 1))))
        valid = '1'

    elif instr == 9:
        res = (rs1 | (1 << (rs2 & (XLEN - 1))))
        valid = '1'

    elif instr == 10:
        res = (rs1 | (1 << (instr[25:20] & (XLEN - 1))))
        valid = '1'

    elif instr == 33:
        byteval = rs1 % 256
        if(byteval < 128):
            res = byteval
            valid = '1'
        else:
            res = (2**(XLEN) - 256) + byteval
            valid = '1'

    elif instr == 34:
        byteval = rs1 % (2**16)
        if(byteval < 2**15):
            res = byteval
            valid = '1'
        else:
            res = (2**(XLEN) - 2**16) + byteval
            valid = '1'

    elif instr == 42:
        res = 2**(XLEN) - 1 - (rs1 ^ rs2)
        valid = '1'

    elif instr == 43:
        res = rs1 % (2**16)
        valid = '1'
    ## logic for all other instr ends
    else:
        res = 0
        valid = '0'

    if XLEN == 32:
        result = '{:032b}'.format(res)
    elif XLEN == 64:
        result = '{:064b}'.format(res)

    return valid+result

