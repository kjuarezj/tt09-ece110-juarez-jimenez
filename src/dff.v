`default_nettype none

module dff #(parameter [0:0] reset_val_p = 1'b0) 
    (input [0:0] clk,
    input [0:0] en_i,
    input [0:0] d_in,
    input [0:0] reset_i,
    output[0:0] q_o
);

//internal reg
reg [0:0] q_r;



always @(posedge clk)(
    if (reset_i) begin
        q_r <= reset_val_p; 
    end else if (en_i) begin // can also just switch it to a basic else instead of en_i 
        q_r <= d_in;
    end
);




assign q_o = q_r;
endmodule