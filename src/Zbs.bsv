// Single Bit Instructions
// Author : Bachotti Sai Krishna Shanmukh EE19B009 IIT Madras
// index i: Value of index comes from lsb log2(XLEN) bits of rs2
// For immediate type instructions, shamt = instr[25:20]

function Bit#(XLEN) fn_bclr(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  // BCLR clears the bit present in ith position in rs1 to 0
  // Pseudo Code:
  // index = rs2 & (XLEN - 1);
  // rd = rs1 & ~(1 << (index));
  Bit#(XLEN) one = 1;       // logical one bit is set
  return rs1 & ~(one << (rs2 & fromInteger(valueOf(XLEN) - valueOf(1))));
  // valueOf converts numeric type to Integer type
  // fromInteger converts Integer type to Bit type
endfunction

function Bit#(XLEN) fn_bclri(Bit#(XLEN) rs1, Bit#(32) instr);
  // BCLRI clears the bit present in ith position in rs1 to 0 (Immediate type)
  // Value of i comes from lsb log2(XLEN) bits of shamt
  // Pseudo Code:
  // index = shamt & (XLEN - 1);
  // rd = rs1 & ~(1 << (index));
  Bit#(XLEN) one = 1; 
  return rs1 & ~(one << (instr[25:20] & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

function Bit#(XLEN) fn_bext(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  // BEXT extracts the bit present in ith position of rs1 
  // Pseudo Code:
  // index = rs2 & (XLEN - 1);
  // rd = (rs1 >> index) & 1;
  Bit#(XLEN) one = 1;
  return (rs1 >> (rs2 & fromInteger(valueOf(XLEN) - valueOf(1)))) & one;
endfunction

function Bit#(XLEN) fn_bexti(Bit#(XLEN) rs1, Bit#(32) instr);
  // BEXTI extracts the bit present in ith position in rs1 (Immediate type)
  // Pseudo Code:
  // index = shamt & (XLEN - 1);
  // rd = (rs1 >> index) & 1;
  Bit#(XLEN) one = 1;
  return (rs1 >> (instr[25:20] & fromInteger(valueOf(XLEN) - valueOf(1)))) & one;
endfunction

function Bit#(XLEN) fn_binv(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  // BINV inverts the bit present in ith position in rs1
  // Pseudo Code:
  // index = rs2 & (XLEN - 1);
  // rd = rs1 ^ (1 << index);
  Bit#(XLEN) one = 1; 
  return rs1 ^ (one << (rs2 & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

function Bit#(XLEN) fn_binvi(Bit#(XLEN) rs1, Bit#(32) instr);
  // BINVI inverts the bit present in ith position in rs1 (Immediate type)
  // Pseudo Code:
  // index = shamt & (XLEN - 1);
  // rd = rs1 ^ (1 << index);
  Bit#(XLEN) one = 1; 
  return rs1 ^ (one << (instr[25:20] & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

function Bit#(XLEN) fn_bset(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  // BSET sets the bit present in ith position to 1
  // Pseudo Code:
  // index = rs2 & (XLEN - 1);
  // rd = rs1 & ~(1 << (index));
  Bit#(XLEN) one = 1; 
  return rs1 | (one << (rs2 & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

function Bit#(XLEN) fn_bseti(Bit#(XLEN) rs1, Bit#(32) instr);
  // BSETI sets the bit present in ith position to 1 (Immediate type)
  // Pseudo Code:
  // index = shamt & (XLEN - 1);
  // rd = rs1 & ~(1 << (index));
  Bit#(XLEN) one = 1; 
  return rs1 | (one << (instr[25:20] & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

