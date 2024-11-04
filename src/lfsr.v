`default_nettype none

module lfsr( 
    input [0:0] clk, 
    input [0:0] en_i,
    input [0:0] reset_i,
    input  [0:0] feedback, // feedback calculations will be done in top mod
    //input [7:0] d_i, // input bits
    output [7:0] q_o
);



wire[7:0] d_i ; 
assign d_i[0] = feedback;
assign d_i[7:1] = q_r[6:0];

reg [7:0] q_r;



dff dff0( .clk(clk) , .d_i(d_i[0]) , .en_i(en_i) , .reset_i(reset_i), .q_o(q_r[0]));
dff dff1( .clk(clk) , .d_i(d_i[1]) , .en_i(en_i) , .reset_i(reset_i), .q_o(q_r[1]));
dff dff2( .clk(clk) , .d_i(d_i[2]) , .en_i(en_i) , .reset_i(reset_i), .q_o(q_r[2]));
dff dff3( .clk(clk) , .d_i(d_i[3]) , .en_i(en_i) , .reset_i(reset_i), .q_o(q_r[3]));
dff dff4( .clk(clk) , .d_i(d_i[4]) , .en_i(en_i) , .reset_i(reset_i), .q_o(q_r[4]));
dff dff5( .clk(clk) , .d_i(d_i[5]) , .en_i(en_i) , .reset_i(reset_i), .q_o(q_r[5]));
dff dff6( .clk(clk) , .d_i(d_i[6]) , .en_i(en_i) , .reset_i(reset_i), .q_o(q_r[6]));
dff dff7( .clk(clk) , .d_i(d_i[7]) , .en_i(en_i) , .reset_i(reset_i), .q_o(q_r[7]));


assign q_o = q_r; 

endmodule