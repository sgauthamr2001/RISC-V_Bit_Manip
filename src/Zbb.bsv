function Bit#(XLEN) fn_andn(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs1 & ~rs2;
endfunction

function Bit#(XLEN) fn_clz(Bit#(XLEN) rs1); 
  return zeroExtend(countZerosMSB(rs1));
endfunction 

`ifdef RV64
  function Bit#(XLEN) fn_clzw(Bit#(XLEN) rs1);
    return zeroExtend(countZerosMSB(rs1[31:0])); 
  endfunction 
`endif

function Bit#(XLEN) fn_cpop(Bit#(XLEN) rs1);
  return zeroExtend(countOnes(rs1));
endfunction 

`ifdef RV64 
  function Bit#(XLEN) fn_cpopw(Bit#(XLEN) rs1);
    return zeroExtend(countOnes(rs1[31:0]));
  endfunction
`endif

function Bit#(XLEN) fn_ctz(Bit#(XLEN) rs1); 
  return zeroExtend(countZerosLSB(rs1));
endfunction 

`ifdef RV64 
  function Bit#(XLEN) fn_ctz(Bit#(XLEN) rs1); 
    return zeroExtend(countZerosLSB(rs1[31:0]));
  endfunction 
`endif 

function Bit#(XLEN) fn_max(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Int#(XLEN) element1 = unpack(rs1);
  Int#(XLEN) element2 = unpack(rs2);
  return pack(max(element1, element2)); 
endfunction

function Bit#(XLEN) fn_maxu(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  UInt#(XLEN) element1 = unpack(rs1);
  UInt#(XLEN) element2 = unpack(rs2);
  return pack(max(element1, element2)); 
endfunction

function Bit#(XLEN) fn_min(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Int#(XLEN) element1 = unpack(rs1);
  Int#(XLEN) element2 = unpack(rs2);
  return pack(min(element1, element2));
endfunction

function Bit#(XLEN) fn_minu(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  UInt#(XLEN) element1 = unpack(rs1);
  UInt#(XLEN) element2 = unpack(rs2); 
  return pack(min(element1, element2));
endfunction

function Bit#(XLEN) fn_orcb(Bit#(XLEN) rs1); 
  Bit#(XLEN) result = 32'h00000000; 
  for(int i = 0; i < valueOf(XLEN); i = i + 8) begin 
    if(rs1[i+7:i] == 8'b00000000)
      result[i+7:i] = 8'b00000000; 
    else
      result[i+7:i] = 8'b11111111; 
  end 
  return result;
endfunction 

function Bit#(XLEN) fn_orn(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs1 | ~rs2;
endfunction

function Bit#(XLEN) fn_rev8(Bit#(XLEN);
  Bit#(XLEN) result = 32'h00000000; 
  Int#(32) j = valueOf(XLEN); 
  j = j - 1; 
  for(int i = 0; i + 8 < valueOf(XLEN); i = i + 8) begin 
    result[i:i+7] = rs1[j-7:j];
    j = j - 8; 
  end 
  return result; 
endfunction 

function Bit#(XLEN) fn_rol(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Int#(32) shamt; 
  if(valueOf(XLEN) == 32)
    shamt = unpack(rs2[4:0]); 
  else
    shamt = unpack(rs2[5:0]); 

  result = (rs1 << shamt) | (rs1 >> (valueOf(XLEN) - shamt)); 
  return result; 
endfunction

`ifdef RV64 
  function Bit#(XLEN) fn_rolw(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
    Int#(32) shamt = unpack(rs2[4:0]); 
    Int#(64) op1 = zeroExtend(rs1[31:0]); 
    result = (op1 << shamt) | (op1 >> (32 - shamt)); 
    return signExtend(result[31:0]); 
  endfunction
`endif 

function Bit#(XLEN) fn_ror(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Int#(32) shamt; 
  if(valueOf(XLEN) == 32)
    shamt = unpack(rs2[4:0]); 
  else
    shamt = unpack(rs2[5:0]); 

  result = (rs1 >> shamt) | (rs1 << (valueOf(XLEN) - shamt)); 
  return result; 
endfunction

function Bit#(XLEN) fn_rori(Bit#(32) instr, Bit#(XLEN) rs1);
  Int#(32) shamt; 
  if(valueOf(XLEN) == 32)
    shamt = unpack(instr[24:20]); 
  else
    shamt = unpack(instr[25:20]); 

  result = (rs1 >> shamt) | (rs1 << (valueOf(XLEN) - shamt)); 
  return result; 
endfunction

`ifdef RV64 
  function Bit#(XLEN) fn_roriw(Bit#(32) instr, Bit#(XLEN) rs1);
    Int#(32) shamt = unpack(instr[24:20]); 
    Int#(64) op1 = zeroExtend(rs1[31:0]); 
    result = (op1 >> shamt) | (op1 << (32 - shamt)); 
    return signExtend(result[31:0]); 
  endfunction

  function Bit#(XLEN) fn_rorw(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
    Int#(32) shamt = unpack(rs2[4:0]); 
    Int#(64) op1 = zeroExtend(rs1[31:0]); 
    result = (op1 >> shamt) | (op1 << (32 - shamt)); 
    return signExtend(result[31:0]); 
  endfunction
`endif 