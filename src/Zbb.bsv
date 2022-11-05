function Bit#(XLEN) fn_andn(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs1 & ~rs2;
endfunction

function Bit#(XLEN) fn_clz(Bit#(XLEN) rs1); 
  return pack(zeroExtend(countZerosMSB(rs1)));
endfunction 

`ifdef RV64
  function Bit#(XLEN) fn_clzw(Bit#(XLEN) rs1);
    return pack(zeroExtend(countZerosMSB(rs1[31:0]))); 
  endfunction 
`endif

function Bit#(XLEN) fn_cpop(Bit#(XLEN) rs1);
  return pack(zeroExtend(countOnes(rs1)));
endfunction 

`ifdef RV64 
  function Bit#(XLEN) fn_cpopw(Bit#(XLEN) rs1);
    return pack(zeroExtend(countOnes(rs1[31:0])));
  endfunction
`endif

function Bit#(XLEN) fn_ctz(Bit#(XLEN) rs1); 
  return pack(zeroExtend(countZerosLSB(rs1)));
endfunction 

`ifdef RV64 
  function Bit#(XLEN) fn_ctzw(Bit#(XLEN) rs1); 
    return pack(zeroExtend(countZerosLSB(rs1[31:0])));
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
  Bit#(XLEN) result = 0; 
  for(Integer i = 0; i < valueOf(XLEN); i = i + 8) begin 
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

function Bit#(XLEN) fn_rev8(Bit#(XLEN) rs1);
  Bit#(XLEN) result = 0; 
  Bit#(8) temp_byte; 
  Integer j = valueOf(XLEN) - 1;
  for(Integer i = 0; i < valueOf(XLEN); i = i + 8) begin 
    temp_byte = rs1[j:j-7];
    result[i+7:i] = temp_byte;
    j = j - 8; 
  end 
  return result; 
endfunction 

function Bit#(XLEN) fn_rol(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Bit#(XLEN) result;
  UInt#(8) shamt; 
  if(valueOf(XLEN) == 32)
    shamt = unpack(zeroExtend(rs2[4:0])); 
  else
    shamt = unpack(zeroExtend(rs2[5:0])); 
  result = (rs1 << shamt) | (rs1 >> (fromInteger(valueOf(XLEN)) - shamt)); 
  return result; 
endfunction

`ifdef RV64 
  function Bit#(XLEN) fn_rolw(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
    Bit#(XLEN) result;
    Bit#(32) op1 = rs1[31:0];
    UInt#(6) shamt = unpack(zeroExtend(rs2[4:0])); 
    result = signExtend((op1 << shamt) | (op1 >> (fromInteger(valueOf(32)) - shamt))); 
    return result;
  endfunction
`endif 

function Bit#(XLEN) fn_ror(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  Bit#(XLEN) result;
  UInt#(8) shamt; 
  if(valueOf(XLEN) == 32)
    shamt = unpack(zeroExtend(rs2[4:0])); 
  else
    shamt = unpack(zeroExtend(rs2[5:0])); 
  result = (rs1 >> shamt) | (rs1 << (fromInteger(valueOf(XLEN)) - shamt)); 
  return result; 
endfunction

function Bit#(XLEN) fn_rori(Bit#(32) instr, Bit#(XLEN) rs1);
  Bit#(XLEN) result;
  UInt#(8) shamt; 
  if(valueOf(XLEN) == 32)
    shamt = unpack(zeroExtend(instr[24:20])); 
  else
    shamt = unpack(zeroExtend(instr[25:20])); 
  result = (rs1 >> shamt) | (rs1 << (fromInteger(valueOf(XLEN)) - shamt)); 
  return result; 
endfunction

`ifdef RV64 
  function Bit#(XLEN) fn_roriw(Bit#(32) instr, Bit#(XLEN) rs1);
    Bit#(XLEN) result;
    UInt#(6) shamt = unpack(zeroExtend(instr[24:20])); 
    Bit#(32) op1 = rs1[31:0]; 
    result = signExtend((op1 >> shamt) | (op1 << (fromInteger(valueOf(32)) - shamt))); 
    return result; 
  endfunction

  function Bit#(XLEN) fn_rorw(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
    Bit#(XLEN) result;
    UInt#(6) shamt = unpack(zeroExtend(rs2[4:0])); 
    Bit#(32) op1 = rs1[31:0]; 
    result = signExtend((op1 >> shamt) | (op1 << (fromInteger(valueOf(32)) - shamt))); 
    return result;
  endfunction
`endif 

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
