function Bit#(XLEN) fn_andn(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs1 & ~rs2;
endfunction

function Bit#(XLEN) fn_sextb(Bit#(XLEN) rs1);
  return signExtend(rs1[7:0]);
endfunction

function Bit#(XLEN) fn_sexth(Bit#(XLEN) rs1);
  return signExtend(rs1[15:0]);
endfunction

function Bit#(XLEN) fn_xnor(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return ~(rs1 ^ rs2);
endfunction

function Bit#(XLEN) fn_zexth(Bit#(XLEN) rs1);
  return zeroExtend(rs1[15:0]);
endfunction