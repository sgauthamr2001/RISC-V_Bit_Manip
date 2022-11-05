function Bit#(XLEN) fn_bclr(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  //index = rs2 & (XLEN - 1);
  //rd = rs1 & ~(1 << (index));
  Bit#(XLEN) one = 1; 
  return rs1 & ~(one << (rs2 & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

function Bit#(XLEN) fn_bclri(Bit#(XLEN) rs1, Bit#(32) instr);
  //index = rs2 & (XLEN - 1);
  //rd = rs1 & ~(1 << (index));
  Bit#(XLEN) one = 1; 
  return rs1 & ~(one << (instr[25:20] & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

function Bit#(XLEN) fn_bext(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  //index = rs2 & (XLEN - 1);
  Bit#(XLEN) one = 1;
  return (rs1 >> (rs2 & fromInteger(valueOf(XLEN) - valueOf(1)))) & one;
endfunction

function Bit#(XLEN) fn_bexti(Bit#(XLEN) rs1, Bit#(32) instr);
  //index = rs2 & (XLEN - 1);
  Bit#(XLEN) one = 1;
  return (rs1 >> (instr[25:20] & fromInteger(valueOf(XLEN) - valueOf(1)))) & one;
endfunction

function Bit#(XLEN) fn_binv(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  //index = rs2 & (XLEN - 1);
  Bit#(XLEN) one = 1; 
  return rs1 ^ (one << (rs2 & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

function Bit#(XLEN) fn_binvi(Bit#(XLEN) rs1, Bit#(32) instr);
  //index = rs2 & (XLEN - 1);
  Bit#(XLEN) one = 1; 
  return rs1 ^ (one << (instr[25:20] & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

function Bit#(XLEN) fn_bset(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  //index = rs2 & (XLEN - 1);
  //rd = rs1 & ~(1 << (index));
  Bit#(XLEN) one = 1; 
  return rs1 | (one << (rs2 & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

function Bit#(XLEN) fn_bseti(Bit#(XLEN) rs1, Bit#(32) instr);
  //index = rs2 & (XLEN - 1);
  //rd = rs1 & ~(1 << (index));
  Bit#(XLEN) one = 1; 
  return rs1 | (one << (instr[25:20] & fromInteger(valueOf(XLEN) - valueOf(1))));
endfunction

