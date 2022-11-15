#See LICENSE.iitm for license details
'''

Author   : Santhosh Pavan
Email id : santhosha@mindgrovetech.in
Details  : This file consists cocotb testbench for bbox dut

--------------------------------------------------------------------------------------------------
'''
'''
TODO:
Task Description: Add list of instructions in Testfactory block. So that testbench generates tests for listed instructions. One instruction is implemented as an example. 
		  For multiple instructions, provided as comment (see after TestFactory(TB)). Please the use the same format.
                  Note - Comments are provided for TestFactory.
		  Note - The value of instr (ANDN) is a temp value, it needed to be changed according to spec.

Note - Here testbench assumes below verilog port names are generated by bluespec compiler. Please implement the bluespec design with below port names.

 DUT Ports:
 Name                         I/O  size 
 bbox_out                       O    65/33
 CLK                            I     1 
 RST_N                          I     1 
 instr                          I    32
 rs1                            I    64/32
 rs2                            I    64/32
   (instr, rs1, rs2) -> bbox_out
'''


import string
import random
import cocotb
import logging as _log
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.regression import TestFactory

from bbox_ref_model import bbox_rm

def func_gen(instr_name, shamt='000000', base="RV64"):
    if instr_name == 'adduw':
        instr = '0000100' + '00000' + '00000' + '000' + '00000' + '0111011'
    elif instr_name == 'andn':
        instr = '0100000' + '00000' + '00000' + '111' + '00000' + '0110011'
    elif instr_name == 'bclr':
        instr = '0100100' + '00000' + '00000' + '001' + '00000' + '0110011'
    elif instr_name == 'bclri':
        instr = '010010' + shamt + '00000' + '001' + '00000' + '0010011'
    elif instr_name == 'bext':
        instr = '0100100' + '00000' + '00000' + '101' + '00000' + '0110011'
    elif instr_name == 'bexti': 
        instr = '010010' + shamt + '00000' + '101' + '00000' + '0010011'
    elif instr_name == 'binv': 
        instr = '0110100' + '00000' + '00000' + '001' + '00000' + '0110011'
    elif instr_name == 'binvi':
        instr = '011010' + shamt + '00000' + '001' + '00000' + '0010011'
    elif instr_name == 'bset':
        instr = '0010100' + '00000' + '00000' + '001' + '00000' + '0110011'
    elif instr_name == 'bseti': 
        instr = '001010' + shamt + '00000' + '001' + '00000' + '0010011'
    elif instr_name == 'clmul':
        instr = '0000101' + '00000' + '00000' + '001' + '00000' + '0110011'
    elif instr_name == 'clmulh': 
        instr = '0000101' + '00000' + '00000' + '011' + '00000' + '0110011'
    elif instr_name == 'clmulr':
        instr = '0000101' + '00000' + '00000' + '010' + '00000' + '0110011'
    elif instr_name == 'clz': 
        instr = '0110000' + '00000' + '00000' + '001' + '00000' + '0010011'
    elif instr_name == 'clzw': 
        instr = '0110000' + '00000' + '00000' + '001' + '00000' + '0011011'
    elif instr_name == 'cpop': 
        instr = '0110000' + '00010' + '00000' + '001' + '00000' + '0010011'
    elif instr_name == 'cpopw':
        instr = '0110000' + '00010' + '00000' + '001' + '00000' + '0011011'
    elif instr_name == 'ctz': 
        instr = '0110000' + '00001' + '00000' + '001' + '00000' + '0010011'
    elif instr_name == 'ctzw':
        instr = '0110000' + '00001' + '00000' + '001' + '00000' + '0011011'
    elif instr_name == 'max': 
        instr = '0000101' + '00000' + '00000' + '110' + '00000' + '0110011'
    elif instr_name == 'maxu':
        instr = '0000101' + '00000' + '00000' + '111' + '00000' + '0110011'
    elif instr_name == 'min':
        instr = '0000101' + '00000' + '00000' + '100' + '00000' + '0110011'
    elif instr_name == 'minu':
        instr = '0000101' + '00000' + '00000' + '101' + '00000' + '0110011'
    elif instr_name == 'orcb':
        instr = '001010000111' + '00000' + '101' + '00000' + '0010011'
    elif instr_name == 'orn':
        instr = '0100000' + '00000' + '00000' + '110' + '00000' + '0110011'
    elif instr_name == 'rev8': 
        if(base == 'RV32'): 
            instr = '011010011000' + '00000' + '101' + '00000' + '0010011'
        else:
            instr = '011010111000' + '00000' + '101' + '00000' + '0010011'
    elif instr_name == 'rol':
        instr = '0110000' + '00000' + '00000' + '001' + '00000' + '0110011'
    elif instr_name == 'rolw':
        instr = '0110000' + '00000' + '00000' + '001' + '00000' + '0111011'
    elif instr_name == 'ror':
        instr = '0110000' + '00000' + '00000' + '101' + '00000' + '0110011'
    elif instr_name == 'rori':
        instr = '011000' + shamt + '00000' + '101' + '00000' + '0010011'
    elif instr_name == 'roriw': 
        instr = '011000' + shamt + '00000' + '101' + '00000' + '0011011'
    elif instr_name == 'rorw': 
        instr = '0110000' + '00000' + '00000' + '101' + '00000' + '0111011'
    elif instr_name == 'sextb': 
        instr = '0110000' + '00100' + '00000' + '001' + '00000' + '0010011'
    elif instr_name == 'sexth':
        instr = '0110000' + '00101' + '00000' + '001' + '00000' + '0010011'
    elif instr_name == 'sh1add': 
        instr = '0010000' + '00000' + '00000' + '010' + '00000' + '0110011'     
    elif instr_name == 'sh1adduw': 
        instr = '0010000' + '00000' + '00000' + '010' + '00000' + '0111011'
    elif instr_name == 'sh2add': 
        instr = '0010000' + '00000' + '00000' + '100' + '00000' + '0110011'
    elif instr_name == 'sh2adduw': 
        instr = '0010000' + '00000' + '00000' + '100' + '00000' + '0111011'
    elif instr_name == 'sh3add': 
        instr = '0010000' + '00000' + '00000' + '110' + '00000' + '0110011'
    elif instr_name == 'sh3adduw':
        instr = '0010000' + '00000' + '00000' + '110' + '00000' + '0111011'
    elif instr_name == 'slliuw': 
        instr = '000010' + shamt + '00000' + '001' + '00000' + '0011011'
    elif instr_name == 'xnor': 
        instr = '0100000' + '00000' + '00000' + '100' + '00000' + '0110011'
    elif instr_name == 'zexth': 
        if (base == 'RV32'):
            instr = '0000100' + '00000' + '00000' + '100' + '00000' + '0110011'
        else:
            instr = '0000100' + '00000' + '00000' + '100' + '00000' + '0111011'
    else:
        instr = '1111111' + '11111' + '11111' + '111' + '11111' + '1111111'
        print("Please check the instruction.")

    instr = int(instr, 2)
    return instr 


#generates clock and reset
async def initial_setup(dut):
	cocotb.start_soon(Clock(dut.CLK, 1, units='ns').start())
        
	dut.RST_N.value = 0
	await RisingEdge(dut.CLK)
	dut.RST_N.value = 1


#drives input data to dut
async def input_driver(dut, instr, rs1, rs2, single_opd):
    await RisingEdge(dut.CLK)
    dut.instr.value = instr
    dut.rs1.value = rs1
    dut._log.info("---------------- DUT Input Info -----------------------")
    if single_opd == 1:
        await RisingEdge(dut.CLK)
        dut._log.info("instr = %s  rs1 = %s ",hex(dut.instr.value), hex(dut.rs1.value))

    else :
        dut.rs2.value = rs2
        await RisingEdge(dut.CLK)
        dut._log.info("instr = %s  rs1 = %s rs2 = %s",hex(dut.instr.value), hex(dut.rs1.value), hex(dut.rs2.value))
    dut._log.info("-------------------------------------------------------")

#monitors dut output
async def output_monitor(dut):
    while True:
        await RisingEdge(dut.CLK)
        if(dut.bbox_out.value[0]): break

    dut_result = dut.bbox_out.value
    return dut_result

#compares output of dut and rm
async def scoreboard(dut, dut_result, rm_result):
    dut._log.info("------------ Compare DUT o/p & Ref Model o/p ----------")
    dut._log.info("Expected output  = %s", rm_result)
    dut._log.info("DUT output       = %s", dut_result)
    assert rm_result == str(dut_result),"Failed"
    dut._log.info("-------------------------------------------------------")

#Testbench
async def TB(dut, XLEN, instr, instr_name, single_opd, num_of_tests):
    await initial_setup(dut)
    dut._log.info("*******************************************************")
    dut._log.info("------------- Custom Test %r of RV%d starts --------------" %(instr_name,XLEN))
    ctests = []
    if (instr_name == 'bclr'):
        ctests.append((2**XLEN - 1,0))
        ctests.append((2**XLEN-1,XLEN-1))
        ctests.append((2**XLEN-1,XLEN))
        ctests.append((2**XLEN-1,XLEN+1))
        ctests.append((2**XLEN-1,XLEN//2))
    
    if (instr_name == 'bclri'):
        ctests.append((2**XLEN - 1,0))
        ctests.append((2,0))

    if (instr_name == 'bext'):
        ctests.append((2**XLEN - 1,0))
        ctests.append((2**XLEN-1,XLEN-1))
        ctests.append((2**XLEN-1,XLEN))
        ctests.append((2**XLEN-1,XLEN+1))
        ctests.append((2**XLEN-1,XLEN//2))

    if (instr_name == 'bexti'):
        ctests.append((2**XLEN - 1,0))
        ctests.append((4,0))

    if (instr_name == 'binv'):
        ctests.append((2**XLEN - 1,0))
        ctests.append((2**XLEN-1,XLEN-1))
        ctests.append((2**XLEN-1,XLEN))
        ctests.append((2**XLEN-1,XLEN+1))
        ctests.append((2**XLEN-1,XLEN//2))
    
    if (instr_name == 'binvi'):
        ctests.append((2**XLEN - 1,0))
        ctests.append((32,0))

    if (instr_name == 'bset'):
        ctests.append((2**XLEN - 17,4))
        ctests.append((0,XLEN-1))
        ctests.append((0,XLEN))
        ctests.append((0,XLEN+1))
        ctests.append((2**XLEN-1 - 2**(XLEN//2),XLEN//2))
        
    if (instr_name == 'bseti'):
        ctests.append((2**XLEN - 17,0))
        ctests.append((0,0))

    if (instr_name == 'sextb'):
        ctests.append((2**16 + 2**8 - 1, 0))
        ctests.append((2**18 + 2**7 - 1, 0))
        ctests.append((2**19 + 2**4,0))
        ctests.append((2**20 + 2**7,0))

    if (instr_name == 'sexth'):
        ctests.append((2**19 + 2**16 - 1, 0))
        ctests.append((2**20 + 2**15 - 1, 0))
        ctests.append((2**21 + 2**14, 0))
        ctests.append((2**22 + 2**15, 0))

    if (instr_name == 'xnor'):
        ctests.append((2**XLEN - 1, 0))
        ctests.append((2**XLEN - 1, 2**XLEN -1))
        ctests.append((2**(XLEN-1)-2, 2**(XLEN-1) + 1))
        ctests.append((0,0))

    if (instr_name == 'zexth'):
        ctests.append((2**16 - 1, 0))
        ctests.append((2**20 + 2**15 - 1, 0))
        ctests.append((2**22 + 2**14, 0))
        ctests.append((2**XLEN - 1, 0))

    if (instr_name == 'clmul'):
        ctests.append((2**XLEN - 1, 0))
        ctests.append((2**XLEN - 1, 2**XLEN - 1))
        ctests.append((2**(XLEN//2) - 1, 2**(XLEN//2) - 1))
        ctests.append(((2**XLEN - 1)//3, 2**XLEN - 1))

    if (instr_name == 'clmulh'):
        ctests.append((2**XLEN - 1, 0))
        ctests.append((2**XLEN - 1, 2**XLEN - 1))
        ctests.append((2**(XLEN//2) - 1, 2**(XLEN//2) - 1))
        ctests.append(((2**XLEN - 1)//3, 2**XLEN - 1))

    if (instr_name == 'clmulr'):
        ctests.append((2**XLEN - 1, 0))
        ctests.append((2**XLEN - 1, 2**XLEN - 1))
        ctests.append((2**(XLEN//2) - 1, 2**(XLEN//2) - 1))
        ctests.append(((2**XLEN - 1)//3, 2**XLEN - 1))

    if(instr_name == 'adduw'):
        ctests.append((2**32 - 1,0)) 
        ctests.append((2**32 - 1,1))
        ctests.append((2**32 - 1,2**64 - 1))
        ctests.append(((2**32-1) << 31,1))

    elif(instr_name == 'andn'):
        ctests.append((0,0))
        ctests.append((2**XLEN - 1,2**XLEN - 1))
        ctests.append((2**XLEN - 1,0))
        ctests.append((random.randint(0,(2**XLEN)-1),random.randint(0,(2**XLEN)-1)))

    elif(instr_name == 'clz'):
        ctests.append((2**XLEN-1,0))       
        ctests.append((2**(XLEN - 1),0))
        ctests.append((0,0))           
        val = '00000000000000000001010101010101'
        ctests.append((int(val,2),0))
    
    elif(instr_name == 'clzw'):
        ctests.append((0,0))          
        val = 2**(64) - 2**(32)
        ctests.append((val,0))
        val = 2**(64) - 2**(31)
        ctests.append((val,0))
        val = 2**(51) - 2**(32) + 2**(18) - 1
        ctests.append((val,0)) 

    elif(instr_name == 'cpop'):
        ctests.append((0,0))               
        ctests.append((2**(XLEN) - 1,0))  
        ctests.append((1,0))
        val = '01010101010101010101010101010101'
        ctests.append((int(val, 2),0))

    elif(instr_name == 'cpopw'):
        ctests.append((2**(64) - 2**(32),0))
        ctests.append((2**(64) - 2**(30),0))
        ctests.append((2**(64) - 1,0))
        ctests.append((0,0))

    elif(instr_name == 'ctz'):
        ctests.append((0,0))
        ctests.append((2**(XLEN) - 1,0))
        if(XLEN == 64):
            ctests.append((2**(64) - 2**(32),0)) 
        else:
            ctests.append((2**(32) - 2**(16),0))
        ctests.append((2**8,0))

    elif(instr_name == 'ctzw'):
        ctests.append((0,0))                
        ctests.append((2**(XLEN) - 1,0))
        ctests.append((2**(64) - 2**(35),0))
        ctests.append((2**(64) - 2**(28),0))  

    elif(instr_name == 'max'):
        ctests.append((-(2**(XLEN-1)),(2**(XLEN-1))-1))
        ctests.append((-1,200))
        ctests.append((-(2**(XLEN-1)),-1))
        ctests.append((-1,(2**(XLEN-1))-1))

    elif(instr_name == 'min'):
        ctests.append((-(2**(XLEN-1)),(2**(XLEN-1))-1))
        ctests.append((-1,200))
        ctests.append((-(2**(XLEN-1)),-1))
        ctests.append((-1,(2**(XLEN-1))-1))

    elif(instr_name == 'maxu'):
        ctests.append((0,(2**XLEN)-1))
        ctests.append((2**(XLEN-1),(2**XLEN)-1))
        ctests.append(((2**(XLEN-1)),1))
        ctests.append(((2**(XLEN-1)),(2**(XLEN-1))-1))

    elif(instr_name == 'minu'):
        ctests.append((0,(2**XLEN)-1))
        ctests.append((2**(XLEN-1),(2**XLEN)-1))
        ctests.append(((2**(XLEN-1)),1))
        ctests.append(((2**(XLEN-1)),(2**(XLEN-1))-1))

    elif(instr_name == 'orcb'):
        ctests.append((2**(XLEN-1) + 2**(XLEN - 17),48))    
        ctests.append((2**(XLEN-9) + 2**(XLEN - 25),35))
        if(XLEN == 64):
            # ctests.append(2**(64) - 1)
            ctests.append((2**(XLEN-33) + 2**(XLEN - 49),10))
            # ctests.append(2**(XLEN-41)+ 2**(XLEN - 57))
            ctests.append((0,0))
        else: 
            ctests.append((0,10))
            ctests.append((2**(32) - 1,10))

    elif(instr_name == 'orn'):
        ctests.append((0,2**(XLEN) - 2))       
        ctests.append((1,0))
        ctests.append((0,1))
        ctests.append((64,2**(XLEN) - 1))

    elif(instr_name == 'rev8'):
        ctests.append((0,0))       
        ctests.append((2**(XLEN) - 1,0))
        if(XLEN == 64):
            ctests.append((2**(64) - 2**(32),0))
        else:
            ctests.append((2**(32) - 2**(16),0))
        ctests.append((2**(32) - 2**(24),0))

    elif(instr_name == 'rol'):
        ctests.append((2**(XLEN-1) + 1,3))               
        ctests.append((2**(XLEN - 1),2**7 - 1))       # Checking if only log(XLEN) bits are being considered 

        if(XLEN == 64):
            val = '00111000011'
            ctests.append((2**(XLEN - 1),int(val,2)))
        else: 
            val = '00111100011'
            ctests.append((2**(XLEN - 1),int(val,2)))

        ctests.append((2**(XLEN - 1),0))

    elif(instr_name == 'rolw'):
        ctests.append((2**(33) - 2**(4),3))
        ctests.append((1,2**6-1))
        val = '00111100011'
        ctests.append((2**(31),int(val,2))) 
        ctests.append((2**(31),0))

    elif(instr_name == 'ror'):
        ctests.append((2**(XLEN-1) + 1,3))               
        ctests.append((2**(XLEN - 1),2**7 - 1))       # Checking if only log(XLEN) bits are being considered 

        if(XLEN == 64):
            val = '00111000011'
            ctests.append((2**(XLEN - 1),int(val,2)))
        else: 
            val = '00111100011'
            ctests.append((2**(XLEN - 1),int(val,2)))

        ctests.append((2**(XLEN - 1),0))

    elif(instr_name == 'rori'):
        ctests.append((2**(XLEN-1) + 1,3))
        ctests.append((2**(XLEN - 1),2**7 - 1)) # Checking if only log(XLEN) bits are being considered 
        ctests.append((2**(XLEN-1) + 2**(XLEN - 17),0))
        ctests.append((1,0))

    elif(instr_name == 'rorw'): 
        ctests.append((2**(33) - 2**(4),5)) 
        ctests.append((1,2**6 - 1))
        val = '00111100011'
        ctests.append((2**(33) - 2**(4),int(val,2)))
        ctests.append((2**(31),0))

    elif(instr_name == 'roriw'): 
        ctests.append((2**(45) - 2**(4),5))
        ctests.append((2**(32) - 2,6))
        ctests.append((2**(30) - 1,7))
        ctests.append((1,8))

    elif(instr_name == 'sh1add'):
        ctests.append((2**XLEN-1,2**XLEN-1))
        ctests.append((0,2**XLEN-1))
        ctests.append((2**XLEN-1,0))
        ctests.append((0,0))

    elif(instr_name == 'sh1adduw'):
        ctests.append((2**64-1,2**64-1))
        ctests.append((2**64-2**32,2**64-1))
        ctests.append((2**32-1,2**64-1))
        ctests.append((2**64-1,1))

    elif(instr_name == 'sh2add'):
        ctests.append((2**XLEN-1,2**XLEN-1))
        ctests.append((0,2**XLEN-1))
        ctests.append((2**XLEN-1,0))
        ctests.append((0,0))

    elif(instr_name == 'sh2adduw'):
        ctests.append((2**64-1,2**64-1))
        ctests.append((2**64-2**32,2**64-1))
        ctests.append((2**32-1, 2**64-1))
        ctests.append((2**64-1,1))
    
    elif(instr_name == 'sh3add'):
        ctests.append((2**XLEN-1,2**XLEN-1))
        ctests.append((0,2**XLEN-1))
        ctests.append((2**XLEN-1,0))
        ctests.append((0,0))

    elif(instr_name == 'sh3adduw'):
        ctests.append((2**64-1,2**64-1))
        ctests.append((2**64-2**32,2**64-1))
        ctests.append((2**32-1, 2**64-1))
        ctests.append((2**64-1,1))
    
    elif(instr_name == 'slliuw'):
        ctests.append((2**64-1,0))
        ctests.append((2**64-2**32,0))
        ctests.append((2**32-1,0))
        ctests.append((2**64-2**32+1))

    for test in ctests:
        rs1 = test[0]
        rs2 = test[1]
        rm_result = bbox_rm(instr, rs1, rs2, XLEN)
        await input_driver(dut, instr, rs1, rs2, single_opd)
        dut_result = await output_monitor(dut)
        await scoreboard(dut, dut_result, rm_result)
    dut._log.info("------------- Custom Test %r of RV%d ends ----------------" %(instr_name,XLEN))
    dut._log.info("*******************************************************")

    dut._log.info("------------- Random Test %r of RV%d starts --------------" %(instr_name,XLEN))
    dut._log.info("*******************************************************")
    for i in range (num_of_tests):
        #rs1 = random.randint(-(2**(XLEN-1)),(2**(XLEN-1))-1) 
        #rs2 = random.randint(-(2**(XLEN-1)),(2**(XLEN-1))-1) 
        rs1 = random.randint(0,(2**XLEN)-1) 
        rs2 = random.randint(0,(2**XLEN)-1)

        # if(i > 9):

        #     # Test vectors for add.uw 
        #     # 1) Checks zero extension of rs1
        #     rs1 = ctests[i - 10]
        #     rs2 = rs2_test[i - 10]

        rm_result = bbox_rm(instr, rs1, rs2, XLEN)
    
        await input_driver(dut, instr, rs1, rs2, single_opd)
        dut_result = await output_monitor(dut)
    
        await scoreboard(dut, dut_result, rm_result)	
    dut._log.info("*******************************************************")
    dut._log.info("------------- Random Test %r of RV%d ends ----------------" %(instr_name,XLEN))
    dut._log.info("*******************************************************")


# generates sets of tests based on the different permutations of the possible arguments to the test function
tf = TestFactory(TB)

base = 'RV32'
#To run tests for RV32, change base = 'RV32'

#generates tests for instructions of RV32
if base == 'RV32':
    tf.add_option('XLEN', [32])
    tf.add_option(('instr','instr_name','single_opd'), 
    [
        (func_gen('bclr', base = base),'bclr', 0),
        (func_gen('bclri',base = base, shamt='000010'),'bclri', 1),
        (func_gen('bclri',base = base, shamt='100010'),'bclri', 1), # RV32 prohibits this instr
        (func_gen('bext', base = base),'bext', 0),
        (func_gen('bexti',shamt='000001', base = base),'bexti', 1),
        (func_gen('bexti',shamt='100001', base = base),'bexti', 1), # RV32 prohibits this instr
        (func_gen('binv',base = base),'binv', 0),
        (func_gen('binvi',shamt='000101', base = base),'binvi', 1),
        (func_gen('binvi',shamt='100101', base = base),'binvi', 1), # RV32 prohibits this instr
        (func_gen('bset', base = base),'bset', 0),
        (func_gen('bseti',shamt='000100', base = base),'bseti', 1),
        (func_gen('bseti',shamt='100100', base = base),'bseti', 1), # RV32 prohibits this instr
        (func_gen('sextb', base = base),'sextb', 1),
        (func_gen('sexth', base = base),'sexth', 1),
        (func_gen('xnor', base = base),'xnor', 0),
        (func_gen('zexth',base=base),'zexth', 1),
        (func_gen('clmul', base = base),'clmul', 0),
        (func_gen('clmulh', base = base),'clmulh', 0),
        (func_gen('clmulr', base = base),'clmulr', 0),
        #(func_gen('adduw', base = base),'adduw', 0),
        (func_gen('andn', base = base), 'andn', 0),
        (func_gen('clz', base = base), 'clz', 1),
        # (func_gen('clzw', base = base), 'clzw', 1),
        (func_gen('cpop', base = base), 'cpop', 1),
        # (func_gen('cpopw', base = base), 'cpopw', 1),
        (func_gen('ctz', base = base), 'ctz', 1),
        # (func_gen('ctzw', base = base), 'ctzw', 1),
        (func_gen('max', base = base), 'max', 0),
        (func_gen('min', base = base), 'min', 0),
        # (func_gen('maxu', base = base), 'maxu', 0),     
        # (func_gen('minu', base = base), 'minu', 0),
        (func_gen('orcb', base = base), 'orcb', 1),
        (func_gen('orn', base = base), 'orn', 0),
        (func_gen('rev8', base=base), 'rev8', 1),
        (func_gen('rol', base = base), 'rol', 0),
        # (func_gen('rolw', base = base), 'rolw', 0),
        (func_gen('ror', base = base), 'ror', 0),
        (func_gen('rori', '111111', base = base), 'rori', 1),
        (func_gen('rori', '011111', base = base), 'rori', 1),
        (func_gen('rori', '000001', base = base), 'rori', 1),
        # (func_gen('rorw', base = base), 'rorw', 0),
        # (func_gen('roriw', '000001', base = base), 'roriw', 1),
        # (func_gen('roriw', '011111', base = base), 'roriw', 1),
        # (func_gen('roriw', '000101', base = base), 'roriw', 1),
        # (func_gen('roriw', '000000', base = base), 'roriw', 1),
        (func_gen('sh1add', base = base),'sh1add',0),
        # (func_gen('sh1adduw', base = base),'sh1adduw',0),
        (func_gen('sh2add', base = base),'sh2add',0),
        # (func_gen('sh2adduw', base = base),'sh2adduw',0),
        (func_gen('sh3add', base = base),'sh3add',0),
        #(func_gen('sh3adduw', base = base),'sh3adduw',0),
        # (func_gen('slliuw','000000', base = base),'slliuw',1),
        # (func_gen('slliuw','111111', base = base),'slliuw',1),
        # (func_gen('slliuw','100000', base = base),'slliuw',1),
        # (func_gen('slliuw','000101', base = base),'slliuw',1)
    ])
    #if instruction has single operand, provide single_opd = 1 (please see below line).
    ##To run multiple instr - tf.add_option(((('instr','instr_name','single_opd'), [(1, 'addn', 0),(2,'clz',1),(...)])

#generates tests for instructions of RV64
elif base == 'RV64':
    tf.add_option('XLEN', [64])
    tf.add_option(('instr','instr_name','single_opd'), 
    [
        (func_gen('bclr', base = base),'bclr', 0),
        (func_gen('bclri',base = base, shamt='000010'),'bclri', 1),
        (func_gen('bclri',base = base, shamt='100010'),'bclri', 1), # RV32 prohibits this instr
        (func_gen('bext', base = base),'bext', 0),
        (func_gen('bexti',shamt='000001', base = base),'bexti', 1),
        (func_gen('bexti',shamt='100001', base = base),'bexti', 1), # RV32 prohibits this instr
        (func_gen('binv',base = base),'binv', 0),
        (func_gen('binvi',shamt='000101', base = base),'binvi', 1),
        (func_gen('binvi',shamt='100101', base = base),'binvi', 1), # RV32 prohibits this instr
        (func_gen('bset', base = base),'bset', 0),
        (func_gen('bseti',shamt='000100', base = base),'bseti', 1),
        (func_gen('bseti',shamt='100100', base = base),'bseti', 1), # RV32 prohibits this instr
        (func_gen('sextb', base = base),'sextb', 1),
        (func_gen('sexth', base = base),'sexth', 1),
        (func_gen('xnor', base = base),'xnor', 0),
        (func_gen('zexth',base=base),'zexth', 1),
        (func_gen('clmul', base = base),'clmul', 0),
        (func_gen('clmulh', base = base),'clmulh', 0),
        (func_gen('clmulr', base = base),'clmulr', 0),
        (func_gen('adduw'),'adduw', 0),
        (func_gen('andn'), 'andn', 0),
        (func_gen('clz'), 'clz', 1),
        (func_gen('clzw'), 'clzw', 1),
        (func_gen('cpop'), 'cpop', 1),
        (func_gen('cpopw'), 'cpopw', 1),
        (func_gen('ctz'), 'ctz', 1),
        (func_gen('ctzw'), 'ctzw', 1),
        (func_gen('max'), 'max', 0),
        (func_gen('min'), 'min', 0),
        (func_gen('maxu'), 'maxu', 0),     
        (func_gen('minu'), 'minu', 0),
        (func_gen('orcb'), 'orcb', 1),
        (func_gen('orn'), 'orn', 0),
        (func_gen('rev8', base='RV64'), 'rev8', 1),
        (func_gen('rol'), 'rol', 0),
        (func_gen('rolw'), 'rolw', 0),
        (func_gen('ror'), 'ror', 0),
        (func_gen('rori', '111111'), 'rori', 1),
        (func_gen('rori', '011111'), 'rori', 1),
        (func_gen('rori', '000001'), 'rori', 1),
        (func_gen('rorw'), 'rorw', 0),
        (func_gen('roriw', '000001'), 'roriw', 1),
        (func_gen('roriw', '011111'), 'roriw', 1),
        (func_gen('roriw', '000101'), 'roriw', 1),
        (func_gen('roriw', '000000'), 'roriw', 1),
        (func_gen('sh1add'),'sh1add',0),
        (func_gen('sh1adduw'),'sh1adduw',0),
        (func_gen('sh2add'),'sh2add',0),
        (func_gen('sh2adduw'),'sh2adduw',0),
        (func_gen('sh3add'),'sh3add',0),
        (func_gen('sh3adduw'),'sh3adduw',0),
        (func_gen('slliuw','000000'),'slliuw',1),
        (func_gen('slliuw','111111'),'slliuw',1),
        (func_gen('slliuw','100000'),'slliuw',1),
        (func_gen('slliuw','000101'),'slliuw',1)
        # # (func_gen('yukta'),'yukta', 0),
        # (func_gen('yuktai',shamt='000010'),'yuktai', 1),
    ])
    #if instruction has single operand, provide single_opd = 1 (please see below line).
    ##To run multiple instr - tf.add_option(((('instr','instr_name','single_opd'), [(1, 'addn', 0),(2,'clz',1),(...)])

#for each instruction below line generates 10 test vectors, can change to different no.
tf.add_option('num_of_tests',[10])
tf.generate_tests()

