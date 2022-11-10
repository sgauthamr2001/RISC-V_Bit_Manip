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

    istr = bindigits(instr, 32)
    #istr = istr[::-1]

    ip1 = istr[0:7]
    ip2 = istr[7:12]
    ip3 = istr[12:17]
    ip4 = istr[17:20]
    ip5 = istr[20:25]
    ip6 = istr[25:32]

    print("IP1: ",ip1)
    print("IP4: ",ip4)
    print("IP6: ",ip6)

    # 1, adduw
    if ((ip1 == '0000100') & (ip4 == '000') & (ip6 == '0111011')):
        print("Testing instruction adduw")
        res = rs2 + (rs1&(2**32 - 1))
        valid = '1'
    
    # 2, andn
    elif ((ip1 == '0100000') & (ip4 == '111') & (ip6 == '0110011')):
        print("Testing instruction andn")
        res = rs1 & ~rs2
        valid = '1'

    # 3, blcr
    elif ((ip1 == '0100100') & (ip4 == '001') & (ip6 == '0110011')):
        res = (rs1 & ~(1 << (rs2 & (XLEN - 1))))
        valid = '1'

    # 4, bclri
    elif ((ip1[:-1] == '000010') & (ip4 == '000') & (ip6 == '0110011')):
        if(XLEN == 32 & ip1[-1] == 0):
            shamt = int(ip2, 2)
            res = (rs1 & ~(1 << (shamt & (XLEN - 1))))
            valid = '1'
        if(XLEN == 64): 
            shamt = int(ip1[-1] + ip2, 2)
            res = (rs1 & ~(1 << (shamt & (XLEN - 1))))
            valid = '1'

    # 5, bext
    elif ((ip1 == '0100100') & (ip4 == '101') & (ip6 == '0110011')):
        res = (rs1 >> (rs2 & (XLEN - 1))) & 1
        valid = '1'
    
    # 6, bexti
    elif ((ip1[:-1] == '010010') & (ip4 == '101') & (ip6 == '0010011')):
        if(XLEN == 32 & ip1[-1] == 0):
            shamt = int(ip2, 2)
            res = (rs1 >> (shamt & (XLEN - 1))) & 1
            valid = '1'
        if(XLEN == 64): 
            shamt = int(ip1[-1] + ip2, 2)
            res = (rs1 >> (shamt & (XLEN - 1))) & 1
            valid = '1'

    # 7, binv
    elif ((ip1 == '0110100') & (ip4 == '001') & (ip6 == '0110011')):
        res = (rs1 ^ (1 << (rs2 & (XLEN - 1))))
        valid = '1'

    # 8, binvi
    elif ((ip1[:-1] == '011010') & (ip4 == '001') & (ip6 == '0010011')):
        if(XLEN == 32 & ip1[-1] == 0):
            shamt = int(ip2, 2)
            res = (rs1 ^ (1 << (shamt & (XLEN - 1))))
            valid = '1'
        if(XLEN == 64):
            shamt = int(ip1[-1] + ip2, 2)
            res = (rs1 ^ (1 << (shamt & (XLEN - 1))))
            valid = '1'

    # 9, bset
    elif ((ip1 == '0010100') & (ip4 == '001') & (ip6 == '0110011')):
        res = (rs1 | (1 << (rs2 & (XLEN - 1))))
        valid = '1'
    
    # 10, bseti
    elif ((ip1[:-1] == '001010') & (ip4 == '001') & (ip6 == '0010011')):
        if(XLEN == 32 & ip1[-1] == 0):
            shamt = int(ip2, 2)
            res = (rs1 | (1 << (shamt & (XLEN - 1))))
            valid = '1'
        if(XLEN == 64):
            shamt = int(ip1[-1] + ip2, 2)
            res = (rs1 | (1 << (shamt & (XLEN - 1))))
            valid = '1'
    
    # 11, clmul
    elif ((ip1 == '0000101') & (ip4 == '001') & (ip6 == '0110011')):
        res = 0
        print("CLMUL Testing\n")
        for i in range(XLEN+1):
            cond = (rs2 // (2**i)) % 2
            if(cond):
                res = res ^ (rs1 * (2**i))
        valid = '1'

    # 12, clmulh
    elif ((ip1 == '0000101') & (ip4 == '011') & (ip6 == '0110011')):
        pass

    # 13, clmulr
    elif ((ip1 == '0000101') & (ip4 == '010') & (ip6 == '0110011')):
        pass

    # 14, clz
    elif ((ip1 == '0110000') & (ip4 == '001') & (ip6 == '0010011') & (ip2 == '00000')):
        res = 0
        while ((rs1 & (1 << (XLEN - 1))) == 0):
            rs1 = (rs1 << 1)
            res += 1
        valid = '1'

    # 15, clzw
    elif ((ip1 == '0110000') & (ip4 == '001') & (ip6 == '0011011') & (ip2 == '00000')):
        if(XLEN == 64):
            res = 0
            while ((rs1 & (1 << 31)) == 0):
                rs1 = (rs1 << 1)
                res += 1
            valid = '1'

    # 16, cpop
    elif ((ip1 == '0110000') & (ip4 == '001') & (ip6 == '0010011') & (ip2 == '00010')):    
        res = 0
        i = 0
        while(i < XLEN):
            i += 1
            if((rs1 & 1) == 1): res += 1    
            rs1 = rs1 >> 1
        valid = '1'
    
    # 17, cpopw
    elif ((ip1 == '0110000') & (ip4 == '001') & (ip6 == '0011011') & (ip2 == '00010')): 
        if(XLEN == 64):
            res = 0 
            i = 0
            while(i < 32):
                i += 1
                if((rs1 & 1) == 1): res += 1      
                rs1 = rs1 >> 1
            valid = '1'

    # 18, ctz
    elif ((ip1 == '0110000') & (ip4 == '001') & (ip6 == '0010011') & (ip2 == '00001')): 

        res = 0
        i = 0
        for i in range(XLEN):
            if((rs1 & 1) == 1): break
            else: res += 1
            rs1 = rs1 >> 1     
        valid = '1'

    # 19, ctzw
    elif ((ip1 == '0110000') & (ip4 == '001') & (ip6 == '0011011') & (ip2 == '00001')):
        if(XLEN == 64):
            res = 0
            i = 0
            for i in range(32):
                if((rs1 & 1) == 1): break
                else: res += 1
                rs1 = rs1 >> 1     
            valid = '1'

    # 20, max 
    elif ((ip1 == '0000101') & (ip4 == '110') & (ip6 == '0110011')):
        if(rs1 > rs2):
            res = rs1 
        else: 
            res = rs2 
        valid = '1'
    
    # 21, maxu
    elif ((ip1 == '0000101') & (ip4 == '111') & (ip6 == '0110011')):
        if(rs1 > rs2):
            res = rs1 
        else: 
            res = rs2 
        valid = '1'
    
    # 22, min
    elif ((ip1 == '0000101') & (ip4 == '100') & (ip6 == '0110011')):
        if(rs1 < rs2):
            res = rs1 
        else: 
            res = rs2 
        valid = '1'

    # 23, minu
    elif ((ip1 == '0000101') & (ip4 == '101') & (ip6 == '0110011')):
        if(rs1 < rs2):
            res = rs1 
        else: 
            res = rs2 
        valid = '1'

    # 24, orcb
    elif ((ip1 == '0010100') & (ip4 == '101') & (ip6 == '0010011') & (ip2 == '00111')):
        res = 0
        for i in range(int(XLEN/8)):
            if(rs1 & 255 != 0): 
                res += 255 << (8 * i)
            rs1 = rs1 >> 8
        valid = '1'

    # 25, orn
    elif ((ip1 == '0100000') & (ip4 == '110') & (ip6 == '0110011')):
        res = rs1 | ~rs2
        valid = '1'

    # 26, rev8
    elif ((ip1[:-1] == '011010') & (ip4 == '101') & (ip6 == '0010011') & (ip2 == '11000')): 
        if(XLEN == 32 & ip1[-1] == 0): 
            res = 0 
            num_bytes = int(XLEN/8)
            for i in range(num_bytes):
                res += (rs1 & 255) << (8 * (num_bytes - i - 1))
                rs1 = rs1 >> 8 
            valid = '1'
        if(XLEN == 64 & ip1[-1] == 1): 
            res = 0 
            num_bytes = int(XLEN/8)
            for i in range(num_bytes):
                res += (rs1 & 255) << (8 * (num_bytes - i - 1))
                rs1 = rs1 >> 8 
            valid = '1'

    # 27, rol
    elif ((ip1 == '0110000') & (ip4 == '001') & (ip6 == '0110011')):
        res = 0 
        if(XLEN == 32): 
            shamt = rs2 & 31
        else: 
            shamt = rs2 & 63

        res = (rs1 << shamt) | ((rs1) >> (XLEN - shamt))
        valid = '1'

    # 28, rolw
    elif ((ip1 == '0110000') & (ip4 == '001') & (ip6 == '0111011')):
        if(XLEN == 64):
            shamt = rs2 & 31
            rs1 = rs1 & (4294967295)
            res = (rs1 << shamt) | ((rs1) >> (32 - shamt))
            res = res & (4294967295)
            res = sign_extend(res, 32)
            valid = '1'

    # 29, ror
    elif ((ip1 == '0110000') & (ip4 == '101') & (ip6 == '0110011')): 
        res = 0 
        if(XLEN == 32): 
            shamt = rs2 & 31
        else: 
            shamt = rs2 & 63

        res = (rs1 >> shamt) | ((rs1) << (XLEN - shamt))
        valid = '1'

    # 30, rori
    elif  ((ip1 == '011000') & (ip4 == '101') & (ip6 == '0010011')): 
        if(XLEN == 32 & ip1[-1] == 0):
            shamt = int(ip2, 2)
            res = (rs1 >> shamt) | ((rs1) << (XLEN - shamt))
            valid = '1'
        if(XLEN == 64):
            shamt = int(ip1[-1] + ip2, 2)
            res = (rs1 >> shamt) | ((rs1) << (XLEN - shamt))
            valid = '1'

    # 31, roriw
    elif ((ip1 == '0110000') & (ip4 == '101') & (ip6 == '0011011')): 
        if(XLEN == 64):
            shamt = int(ip2, 2)
            rs1 = rs1 & (4294967295)
            res = (rs1 >> shamt) | ((rs1) << (32 - shamt))
            res = res & (4294967295)
            res = sign_extend(res, 32)
            valid = '1'

    # 32, rorw
    elif ((ip1 == '0110000') & (ip4 == '101') & (ip6 == '0111011')): 
        if(XLEN == 64):
            shamt = rs2 & 31
            rs1 = rs1 & (4294967295)
            res = (rs1 >> shamt) | ((rs1) << (32 - shamt))
            res = res & (4294967295)
            res = sign_extend(res, 32)
            valid = '1'

    # 33, sext.b 
    elif ((ip1 == '0110000') & (ip4 == '001') & (ip6 == '0010011') & (ip2 == '00100')):
        byteval = rs1 % 256
        if(byteval < 128):
            res = byteval
            valid = '1'
        else:
            res = (2**(XLEN) - 256) + byteval
            valid = '1'

    # 34, sext.h 
    elif ((ip1 == '0110000') & (ip4 == '001') & (ip6 == '0010011') & (ip2 == '00101')):
        byteval = rs1 % (2**16)
        if(byteval < 2**15):
            res = byteval
            valid = '1'
        else:
            res = (2**(XLEN) - 2**16) + byteval
            valid = '1'


    # 35, sh1add
    elif ((ip1 == '0010000') & (ip4 == '010') & (ip6 == '0110011')): 
        res = (rs2 + rs1*2)&(2**64-1)
        valid = '1'

    # 36, sh1add.uw 
    elif ((ip1 == '0010000') & (ip4 == '010') & (ip6 == '0111011')): 
        if(XLEN == 64):
            res = (rs2 + (rs1&(2**32 - 1))*2)&(2**64-1)
            valid = '1'

    # 37, sh2add 
    elif ((ip1 == '0010000') & (ip4 == '100') & (ip6 == '0110011')): 
        res = (rs2 + rs1*4)&(2**64-1)
        valid = '1'

    # 38, sh2add.uw 
    elif ((ip1 == '0010000') & (ip4 == '100') & (ip6 == '0111011')): 
        if(XLEN == 64):
            res = (rs2 + (rs1&(2**32 - 1))*4)&(2**64-1)
            valid = '1'

    # 39, sh3add
    elif ((ip1 == '0010000') & (ip4 == '110') & (ip6 == '0110011')): 
        res = (rs2 + rs1*8)&(2**64-1)
        valid = '1'

    # 40, sh3add.uw
    elif ((ip1 == '0010000') & (ip4 == '110') & (ip6 == '0111011')): 
        if(XLEN == 64):
            res = (rs2 + (rs1&(2**32 - 1))*8)&(2**64-1)
            valid = '1'

    # 41, slli.uw
    elif ((ip1[:-1] == '000010') & (ip4 == '001') & (ip6 == '0011011')): 
        if(XLEN == 64):
            shamt = int(ip1[-1] + ip2, 2)
            rs1 = rs1 & (4294967295)
            rs1 = rs1 << shamt 

    # 42, xnor
    elif ((ip1 == '0100000') & (ip4 == '100') & (ip6 == '0110011')): 
        res = 2**(XLEN) - 1 - (rs1 ^ rs2)
        valid = '1'

    # 43, zext.h
    elif ((ip1 == '0000100') & (ip4 == '100') & (ip2 == '00000')):
        if(XLEN == 32 & ip6 == '0110011'):  
            res = rs1 % (2**16)
            valid = '1'
        if(XLEN == 64 & ip6 == '0111011'):
            res = rs1 % (2**16)
            valid = '1'

    ## logic for all other instr ends
    else:
        print("Default Case\n")
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

