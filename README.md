# BitManip Extension project

This is forked repository of [BitManip Extension](https://gitlab.com/mindgrove1/shakti/bboxStudents). The original README.md is made avaialble [here.](https://gitlab.com/sgauthamr2001/bbox/-/blob/master/README_source.md)


### Bit-Manipulation Extensions

<div align="justify"> The bit manipulation extension comprises of several extensions to the conventional RISC-V architecture, which enables to reduce the code size (each instruction needs to be written using several RV32/64 instructions), also provide improvement on terms of performance and energy. Bit manipulation involves performing operations like shifting, counting etc. on the bits to obtain information or transform them to some apllication usable format. A wide range of applications are benefitted including error control codes, data compression to address generation for memory accesses. Through this project the RISC-V Bit Manipulation Extension (both RV32/64) has been implemented in Bluespec System Verilog and verified using Python3 (cocotb) in accordance to the specification document. There are four sets of extensions freezed by RISC-V international which have been implemented and they include:  </div>

- Zba, Extensions to accelerate address transalation for accessing basic array types.
- Zbb, Extnesions to perform basic bit manipulation operations like logical with negate, counting, rotate etc. 
- Zbc, Extensions to perform carry-less multiplication.
- Zbs, Extensions to perform single-bit operations like bit clear, set etc. 

### The repo structure is as follows:
- bbox.bsv - The top module of the design. Has the interface definition and module definition which calls the BitManip calculation.
- Makefile - Has make commands to generate_verilog and simulate.
- src/ - The directory where the files which the student should edit are present here. The files present are
	- compute.bsv - The top function which selects between the functions implemented for the spec depending on the instruction.
	- bbox.defines - The function which has the macro definition used to select between the instructions.
	- bbox_types.bsv - The structures, enum, bsc macors are defined here.
	- Zba.bsv, Zbb.bsv, Zbc.bsv, Zbs.bsv - Implements the functions to perform respective bit manipulations. 
- bbox_verif/ - The directory where the scripts required for running the cocotb tests are present. The files present are:
	- test_bbox.py - This file consists cocotb testbench for bbox dut. For more info, check Task description provided in this file, as well as the addition of custom tests. 
	- bbox_ref_model.py - This file consists reference model which used in verifying the design (DUT). For more info, check Task description provided in this file. 
- docs/ - The directory where the bitmanip spec pdf, instructions for Tool Setup and some FAQs are present. 

### Interfacing 

<div align="justify"> The inputs and outputs to the design under test are shown as below. In the actual hardware the instruction is passed with appropriate opcodes. To account for the same the structure has been incorporated in 'src/bbox.defines' where the instruction is encoded based on the operation to be performed. Based on the decoded instruction, a result is computed using 'src/compute.bsv' which invokes the corresponding Bluespec extension function. The result is returned to bbox.bsv. In the Python test bench, since the register contents are being passed along side, these parts of the insrtuction shall be passed as 0. The whole instrucion is generated based on the required opcode, along with embedding the shamt value passed by user to get a 32-bit instruction for testing purposes. The func_gen call in the 'src/test_bbox.py' serves this purpose of generating the instruction. This instruction is also passed to 'bbox_verif/bbox_ref_model.py', which gives out the result computed in Python and same is compared with result obtained through Bluespec for functional correctness. </div>

| Name | I/O | Size |
| --- | --- | --- |
| bbox_out | O | 65/33|
| CLK | I  | 1  |
| RST_N | I | 1 |
| instr | I | 32 |
| rs1 | I | 64/32 |
| rs2 | I | 64/32 | 


### Steps to run:
Make sure you have installed all the required tools as mentioned in docs/Tool_setup.pdf and the python environment is activated.

1. To just generate the verilog
```bash
$ make generate_verilog
```
2. To simulate. NOTE: Does both generate_verilog and simulate.
```bash
$ make simulate
```
3. To clean the build.
```bash
$ make clean_build
```

**_NOTE:_** Change BSCDEFINES macro in Makefile to RV64/RV32 according to use. 

### More info for Verification

```bash
1. First-time run - $ make simulate
   Subsequent runs - $ make clean_build
   		     $ make simulate
```
```bash
2. To check waveforms, - Once simulation completes, dump.vcd is created in bbox/
    $ gtkwave dump.vcd
```    
```bash    
3. GTKWave installation - 
	$ sudo apt update
	$ sudo apt install gtkwave
```    

### Evaluation Criteria:
- Design code (bsv) has to be documented with proper comments and design intent
- Every team member should check-in their code contribution using their own GitLab id for individual evaluation
- Verification code (python) has to be documented with proper comments providing the test case explanation
- A final Report.md should be updated providing the steps to run the tests and the instructions implemented along with test run report.
