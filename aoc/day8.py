#!/usr/bin/env python3
"""
Day 8: Handheld Halting

https://adventofcode.com/2020/day/8
"""

from dataclasses import dataclass, field
from typing import Set, Optional

@dataclass
class Instruction:
    op: str
    param: int

    def flip(self):
        if   self.op == "nop":
            self.op = "jmp"
        elif self.op == "jmp":
            self.op = "nop"

@dataclass
class ProgramState:
    counter: int = 0
    acc: int = 0
    visited: Set[int] = field(default_factory=set)


def load_input(filename: str) -> [Instruction]:
    def parse_line(line: str) -> Instruction:
        op, param = line.strip().split()
        return Instruction(op, int(param))

    with open(filename) as f:
        return list(map(parse_line, f))

def execute_instruction(program: [Instruction], state: ProgramState) -> ProgramState:
    OPERATORS = {
        "acc": lambda state, param: ProgramState(
            state.counter+1,
            state.acc+param,
            state.visited | set([state.counter])
        ),
        "jmp": lambda state, param: ProgramState(
            state.counter+param,
            state.acc,
            state.visited | set([state.counter])
        ),
        "nop": lambda state, param: ProgramState(
            state.counter+1,
            state.acc,
            state.visited | set([state.counter])
        ),
    }
    instruction = program[state.counter]
    return OPERATORS[instruction.op](state, instruction.param)

def run(program: [Instruction], state=None) -> ProgramState:
    state = state or ProgramState()

    while state.counter not in state.visited and state.counter < len(program):
        state = execute_instruction(program, state)

    terminates = state.counter >= len(program)
    return terminates, state

def repair_and_run(program: [Instruction]) -> Optional[ProgramState]:
    program_copy = program[:]
    for instruction in program_copy:
        instruction.flip()
        terminates, state = run(program)
        if terminates:
            return state
        instruction.flip()

    return None


if __name__ == "__main__":
    program = load_input("inputs/day8")
    print("Part 1:", run(program)[1].acc)
    print("Part 2:", repair_and_run(program).acc)
