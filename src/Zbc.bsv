function Bit#(XLEN) fn_clmul(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Bit#(XLEN) rd = 0;
  for(Integer i=0;i<valueOf(XLEN);i=i+1) begin 
  	if((rs2>>i)&1) rd = rd^(rs1<<i);
  	end
  return rd;
endfunction

function Bit#(XLEN) fn_clmulh(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Bit#(XLEN) rd = 0;
  for(Integer i=1;i<valueOf(XLEN);i=i+1) begin 
  	if((rs2>>i)&1) rd = rd^(rs1>>(valueOf(XLEN)-i));
  	end
  return rd;
endfunction

function Bit#(XLEN) fn_clmulr(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Bit#(XLEN) rd = 0;
  for(Integer i=0;i<(valueOf(XLEN)-1);i=i+1) begin 
  	if((rs2>>i)&1) rd = rd^(rs1>>(valueOf(XLEN)-i-1));
  	end
  return rd;
endfunction
