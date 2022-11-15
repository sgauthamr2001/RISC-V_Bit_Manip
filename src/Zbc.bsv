function Bit#(XLEN) fn_clmul(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Bit#(XLEN) result = 0; 
  Bit#(XLEN) cond;
  for(Integer i = 0; i < valueOf(XLEN); i = i + 1) begin 
    cond = (rs2 >> i) & fromInteger(valueOf(1));
    if(cond[0] == 1)
      result = result ^ (rs1 << i);
  end 
  return result;
endfunction

function Bit#(XLEN) fn_clmulh(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Bit#(XLEN) result = 0;
  Bit#(XLEN) cond; 
  for(Integer i = 1; i < valueOf(XLEN); i = i + 1) begin 
    cond = (rs2 >> i) & fromInteger(valueOf(1)); 
    if(cond[0] == 1)
      result = result ^ (rs1 >> (valueOf(XLEN) - i));
  end 
  return result;
endfunction

function Bit#(XLEN) fn_clmulr(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Bit#(XLEN) result = 0; 
  for(Integer i = 0; i < valueOf(XLEN); i = i + 1) begin 
    if(((rs2 >> i) & fromInteger(valueOf(1))) != fromInteger(valueOf(0)))
      result = result ^ (rs1 >> (valueOf(XLEN) - i - valueOf(1)));
  end 
  return result;
endfunction
