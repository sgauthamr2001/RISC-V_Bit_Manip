`ifdef RV64 
	function Bit#(XLEN) fn_add.uw(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
	  return rs2 & rs1[31:0];
	endfunction
`endif

function Bit#(XLEN) fn_sh1add(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs2 & rs1<<1;
endfunction

`ifdef RV64 
	function Bit#(XLEN) fn_sh1add.uw(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
	  return rs2 & rs1[31:0]<<1;
	endfunction
`endif

function Bit#(XLEN) fn_sh2add(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs2 & rs1<<2;
endfunction

`ifdef RV64 
	function Bit#(XLEN) fn_sh2add.uw(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
	  return rs2 & rs1[31:0]<<2;
	endfunction
`endif

function Bit#(XLEN) fn_sh3add(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs2 & rs1<<3;
endfunction

`ifdef RV64 
	function Bit#(XLEN) fn_sh3add.uw(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
	  return rs2 & rs1[31:0]<<3;
	endfunction
`endif

`ifdef RV64 
	function Bit#(XLEN) fn_slli.uw(Bit#(32) instr ,Bit#(XLEN) rs1, Bit#(XLEN) rs2);
	  return rs1[31:0]<<instr[25:20];
	endfunction
`endif
