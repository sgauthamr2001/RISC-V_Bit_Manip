//See LICENSE.iitm for license details
/*

Author : Mouna Krishna
Email id : mounakrishna@mindgrovetech.in
Details: The top function which calls the required function depending 
         on the instruction.

--------------------------------------------------------------------------------------------------
*/

/****** Imports *******/
`include "bbox.defines"
import bbox_types :: *;
`include "Zba.bsv"
`include "Zbb.bsv"
`include "Zbc.bsv"
`include "Zbs.bsv"
/*********************/


/*doc: function: The top function where depending on the instruction the 
  required function is called, get the result and return it.
  The input argument and return type should not be changed. 
  Other than this, all the other code can be changed as per needs.

  As an example the instruction ANDN of the Zbb group has been implemented.
  NOTE: The value of ANDN in bbox.defines is a temp value, it needed to be 
  changed according to spec.
  The complete Zbb group and all the other groups is expected to be implemented 
  and verified.
*/
function BBoxOutput fn_compute(BBoxInput inp);
  Bit#(XLEN) result;
  Bool valid;
  case(inp.instr) matches
    `ifdef RV64
      `ADDUW: begin
        result = fn_adduw(inp.rs1, inp.rs2);
        valid = True;
      end
    `endif
    `ANDN: begin
      result = fn_andn(inp.rs1, inp.rs2);
      valid = True;
    end
    `BCLR: begin
      result = fn_bclr(inp.rs1, inp.rs2);
      valid = True;
    end
    `BEXT: begin
      result = fn_bext(inp.rs1, inp.rs2);
      valid = True;
    end
    `BINV: begin
      result = fn_binv(inp.rs1, inp.rs2);
      valid = True;
    end
    `BSET: begin
      result = fn_bset(inp.rs1, inp.rs2);
      valid = True;
    end

    `BCLRI: begin
      `ifdef RV32
        if(inp.instr[25] == 1'b0) begin
          result = fn_bclri(inp.rs1, inp.instr);
          valid = True;
        end
        else begin
          result = 0;
          valid = 0;
        end
      `endif
      `ifdef RV64
        result = fn_bclri(inp.rs1, inp.instr);
        valid = True;
      `endif
    end

    `BEXTI: begin
      `ifdef RV32
        if(inp.instr[25] == 1'b0) begin
          result = fn_bexti(inp.rs1, inp.instr);
          valid = True;
        end
        else begin
          result = 0;
          valid = False;
        end
      `endif
      `ifdef RV64
        result = fn_bexti(inp.rs1, inp.instr);
        valid = True;
      `endif
    end

    `BINVI: begin
      `ifdef RV32
        if(inp.instr[25] == 1'b0) begin
          result = fn_binvi(inp.rs1, inp.instr);
          valid = True;
        end
        else begin
          result = 0;
          valid = 0;
        end
      `endif
      `ifdef RV64
        result = fn_binvi(inp.rs1, inp.instr);
        valid = True;
      `endif
    end

    `BSETI: begin
      `ifdef RV32
        if(inp.instr[25] == 1'b0) begin
          result = fn_bseti(inp.rs1, inp.instr);
          valid = True;
        end
        else begin
          result = 0;
          valid = 0;
        end
      `endif
      `ifdef RV64
        result = fn_bseti(inp.rs1, inp.instr);
        valid = True;
      `endif
    end

    `CLMUL : begin
      result = fn_clmul(inp.rs1, inp.rs2);
      valid = True;
    end
    `CLMULH : begin
      result = fn_clmulh(inp.rs1, inp.rs2);
      valid = True;
    end
    
    `CLMULR : begin
      result = fn_clmulr(inp.rs1, inp.rs2);
      valid = True;
    end
    
    `CLZ : begin
      result = fn_clz(inp.rs1);
      valid = True;
    end

    `CLZW : begin
      `ifdef RV64
        result = fn_clzw(inp.rs1);
        valid = True;
      `endif
    end

    `CPOP : begin
      result = fn_cpop(inp.rs1);
      valid = True;
    end

    `CPOPW : begin
      `ifdef RV64
        result = fn_cpopw(inp.rs1);
        valid = True;
      `endif
    end

    `CTZ : begin
      result = fn_ctz(inp.rs1);
      valid = True;
    end

    `CTZW : begin
      `ifdef RV64
        result = fn_ctzw(inp.rs1);
        valid = True;
      `endif
    end

    `MAX : begin
      result = fn_max(inp.rs1, inp.rs2);
      valid = True;
    end

    `MAXU : begin
      result = fn_maxu(inp.rs1, inp.rs2);
      valid = True;
    end

    `MIN : begin
      result = fn_min(inp.rs1, inp.rs2);
      valid = True;
    end

    `MINU : begin
      result = fn_minu(inp.rs1, inp.rs2);
      valid = True;
    end

    `ORCB : begin
      result = fn_orcb(inp.rs1);
      valid = True;
    end

    `ORN : begin
      result = fn_orn(inp.rs1, inp.rs2);
      valid = True;
    end

    `REV8: begin
      if(inp.instr[25] == 0) begin
        `ifdef RV32
          result = fn_rev8(inp.rs1);
          valid = True;
        `endif
      end
      if(inp.instr[25] == 1) begin
        `ifdef RV64
          result = fn_rev8(inp.rs1);
          valid = True;
        `endif
      end
      else begin
        result = 0;
        valid = False;
      end
    end

    `ROL: begin
      result = fn_rol(inp.rs1, inp.rs2);
      valid = True;
    end

    `ROLW : begin
      `ifdef RV64
        result = fn_rolw(inp.rs1, inp.rs2);
        valid = True;
      `endif
    end

    `ROR: begin
      result = fn_ror(inp.rs1, inp.rs2);
      valid = True;
    end

    `RORI: begin
      `ifdef RV32
        if(inp.instr[25] == 1'b0) begin
          result = fn_rori(inp.rs1, inp.instr);
          valid = True;
        end
        else begin
          result = 0;
          valid = 0;
        end
      `endif
      `ifdef RV64
        result = fn_rori(inp.rs1, inp.instr);
        valid = True;
      `endif
    end

    `RORIW : begin
      `ifdef RV64
        result = fn_roriw(inp.rs1, inp.instr);
        valid = True;
      `endif
    end

    `RORW : begin
      `ifdef RV64
        result = fn_rorw(inp.rs1, inp.rs2);
        valid = True;
      `endif
    end


    `SEXTB : begin
      result = fn_sextb(inp.rs1);
      valid = True;
    end


    `SEXTH : begin
      result = fn_sexth(inp.rs1);
      valid = True;
    end

    `SH1ADD : begin
      result = fn_sh1add(inp.rs1, inp.rs2);
      valid = True;
    end

    `SH1ADDUW : begin
      `ifdef RV64
        result = fn_sh1adduw(inp.rs1, inp.rs2);
        valid = True;
      `endif
    end

    `SH2ADD : begin
      result = fn_sh2add(inp.rs1, inp.rs2);
      valid = True;
    end

    `SH2ADDUW : begin
      `ifdef RV64
        result = fn_sh2adduw(inp.rs1, inp.rs2);
        valid = True;
      `endif
    end

    `SH3ADD : begin
      result = fn_sh3add(inp.rs1, inp.rs2);
      valid = True;
    end

    `SH3ADDUW : begin
      `ifdef RV64
        result = fn_sh3adduw(inp.rs1, inp.rs2);
        valid = True;
      `endif
    end

    `SLLIUW : begin
      `ifdef RV64
        result = fn_slliuw(inp.rs1, inp.instr);
        valid = True;
      `endif
    end
    
    `XNOR : begin
      result = fn_xnor(inp.rs1,inp.rs2);
      valid = True;
    end

    `ZEXTH : begin
      result = fn_zexth(inp.rs1);
      valid = True;
    end
    
    default: begin
      result = 0;
      valid = False;
    end
  endcase
  return BBoxOutput{valid: valid, data: result};
endfunction
