# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles , RisingEdge

@cocotb.test()
async def test_with_seed_0x01(dut):
    """test 1: lfsr w seed 0x01"""

    dut._log.info("starting lfsr test 1 with seed 0x01")
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.ui_in.value = 0x01  # set seed
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    for cycle in range(20):
        await RisingEdge(dut.clk)
        dut._log.info(f"cycle {cycle}: uo_out = {dut.uo_out.value}")

@cocotb.test()
async def test_with_seed_0xA3(dut):
    """test 2: lfsr with seed 0xA3"""
    dut._log.info("starting lfsr test 2 with seed 0xA3")
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.ui_in.value = 0xA3  # set seed
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    for cycle in range(20):
        await RisingEdge(dut.clk)
        dut._log.info(f"cycle {cycle}: uo_out = {dut.uo_out.value}")

@cocotb.test()
async def test_with_seed_0xFF(dut):
    """test lfsr with seed 0xFF"""
    dut._log.info("starting lfsr test 3 with seed 0xFF")
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.ui_in.value = 0xFF  # set seed
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    for cycle in range(20):
        await RisingEdge(dut.clk)
        dut._log.info(f"cycle {cycle}: uo_out = {dut.uo_out.value}")


@cocotb.test()
async def test_with_seed_0x3F(dut):
    """test lfsr with seed 0x3F"""
    dut._log.info("starting lfsr test 4 with seed 0x3F")
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.ui_in.value = 0x3F  # set seed
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    for cycle in range(20):
        await RisingEdge(dut.clk)
        dut._log.info(f"cycle {cycle}: uo_out = {dut.uo_out.value}")

@cocotb.test()
async def test_with_seed_0xC7(dut):
    """test lfsr with seed 0xC7"""
    dut._log.info("starting lfsr test 3 with seed 0xC7")
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    dut.ui_in.value = 0xC7  # set seed
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk, 1)

    for cycle in range(20):
        await RisingEdge(dut.clk)
        dut._log.info(f"cycle {cycle}: uo_out = {dut.uo_out.value}")