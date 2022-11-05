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

    if instr == 1:
        res = rs2 + (rs1&(2**32 - 1))
        valid = '1'
    
    elif instr == 2:
        res = rs1 & ~rs2
        valid = '1'

    elif instr == 3:
        res = (rs1 & ~(1 << (rs2 & (XLEN - 1))))
        valid = '1'

    elif instr == 4:
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
    
    elif instr == 11:
        pass

    elif instr == 12:
        pass

    elif instr == 13:
        pass

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
    
    elif instr == 35:
        res = (rs2 + rs1*2)&(2**64-1)
        valid = '1'

    elif instr == 36:
        res = (rs2 + (rs1&(2**32 - 1))*2)&(2**64-1)
        valid = '1'

    elif instr == 37:
        res = (rs2 + rs1*4)&(2**64-1)
        valid = '1'

    elif instr == 38:
        res = (rs2 + (rs1&(2**32 - 1))*4)&(2**64-1)
        valid = '1'

    elif instr == 39:
        res = (rs2 + rs1*8)&(2**64-1)
        valid = '1'

    elif instr == 40:
        res = (rs2 + (rs1&(2**32 - 1))*8)&(2**64-1)
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

    """ 
    if XLEN == 32:
        result = '{:032b}'.format(res)
    elif XLEN == 64:
        result = '{:064b}'.format(res)
    """

    return valid+result

