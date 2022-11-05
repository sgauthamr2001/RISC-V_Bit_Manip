function Bit#(XLEN) fn_clmul(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return (rs2*rs1)[63:0];
endfunction
