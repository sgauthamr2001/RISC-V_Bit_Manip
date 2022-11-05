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
def bindigits(n, bits):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

def sign_extend(value, bits):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

#Reference model
def bbox_rm(instr, rs1, rs2, XLEN):
    print(type(instr),type(rs1),type(rs2))
    if instr == 1:
        res = rs2 + (rs1&(2**32 - 1))
        valid = '1'
    
    elif instr == 2:
        res = rs1 & ~rs2
        valid = '1'

    ## logic for all other instr starts 

    elif instr == 14:
        res = 0
        while ((rs1 & (1 << (XLEN - 1))) == 0):
            rs1 = (rs1 << 1)
            res += 1
        valid = '1'

    elif instr  == 15: 
        res = 0
        while ((rs1 & (1 << 31)) == 0):
            rs1 = (rs1 << 1)
            res += 1
        valid = '1'

    elif instr == 16:
        res = 0
        i = 0
        while(i < XLEN):
            i += 1
            if((rs1 & 1) == 1): res += 1    
            rs1 = rs1 >> 1
        valid = '1'
    
    elif instr == 17: 
        res = 0 
        i = 0
        while(i < 32):
            i += 1
            if((rs1 & 1) == 1): res += 1      
            rs1 = rs1 >> 1
        valid = '1'

    elif instr == 18: 
        res = 0
        i = 0
        for i in range(XLEN):
            if((rs1 & 1) == 1): break
            else: res += 1
            rs1 = rs1 >> 1     
        valid = '1'

    elif instr == 19:
        res = 0
        i = 0
        for i in range(32):
            if((rs1 & 1) == 1): break
            else: res += 1
            rs1 = rs1 >> 1     
        valid = '1'

    elif instr == 20: 
        if(rs1 > rs2):
            res = rs1 
        else: 
            res = rs2 
        valid = '1'

    elif instr == 21: 
        if(rs1 > rs2):
            res = rs1 
        else: 
            res = rs2 
        valid = '1'

    elif instr == 22: 
        if(rs1 < rs2):
            res = rs1 
        else: 
            res = rs2 
        valid = '1'

    elif instr == 23: 
        if(rs1 < rs2):
            res = rs1 
        else: 
            res = rs2 
        valid = '1'

    elif instr == 24: 
        res = 0
        for i in range(int(XLEN/8)):
            if(rs1 & 255 != 0): 
                res += 255 << (8 * i)
            rs1 = rs1 >> 8
        valid = '1'

    elif instr == 25: 
        res = rs1 | ~rs2
        valid = '1'
        
    elif instr == 26: 
        res = 0 
        num_bytes = int(XLEN/8)
        for i in range(num_bytes):
            res += (rs1 & 255) << (8 * (num_bytes - i - 1))
            rs1 = rs1 >> 8 
        valid = '1'

    elif instr == 27: 
        res = 0 
        if(XLEN == 32): 
            shamt = rs2 & 31
        else: 
            shamt = rs2 & 63

        res = (rs1 << shamt) | ((rs1) >> (XLEN - shamt))
        valid = '1'

    elif instr == 28: 
        shamt = rs2 & 31
        rs1 = rs1 & (4294967295)
        res = (rs1 << shamt) | ((rs1) >> (32 - shamt))
        res = res & (4294967295)
        res = sign_extend(res, 32)
        valid = '1'

    elif instr == 29: 
        res = 0 
        if(XLEN == 32): 
            shamt = rs2 & 31
        else: 
            shamt = rs2 & 63

        res = (rs1 >> shamt) | ((rs1) << (XLEN - shamt))
        valid = '1'

    elif instr == 30: 
        pass 

    elif instr == 31: 
        pass 
    
    elif instr == 32: 
        shamt = rs2 & 31
        rs1 = rs1 & (4294967295)
        res = (rs1 >> shamt) | ((rs1) << (32 - shamt))
        res = res & (4294967295)
        res = sign_extend(res, 32)
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
        result = bindigits(res, 32)
    elif XLEN == 64:
        result = bindigits(res, 64)

    return valid+result

