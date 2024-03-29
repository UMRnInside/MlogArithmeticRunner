# MlogArithmeticRunner
A Mindustry Logic emulator built for automated testing of compilers (like MlogEvo).

## Install
`pip install https://github.com/UMRnInside/MlogArithmeticRunner`
or

`pip install mlog_arithmetic_runner`

## Usage
```
$ python3 -m mlog_arithmetic_runner --help
usage: mlog_arithmetic_runner [-h] [--limit LIMIT] [--continue-if-past-the-end] [--ipt IPT]
                              [--memory-banks MEMORY_BANKS] [--memory-cells MEMORY_CELLS]
                              [--json-indent JSON_INDENT] [--json-dump-memory-blocks]

Reads some mlog code from stdin, runs it, and generates JSON report

optional arguments:
  -h, --help            show this help message and exit
  --limit LIMIT         Max instructions/cycles allowed, something like TimeLimit
  --continue-if-past-the-end
  --ipt IPT             Instructions per tick. 2 for micro-processor, 8 for logic-processor,
                        25 for hyper-processor
  --memory-banks MEMORY_BANKS
                        Memory bank count
  --memory-cells MEMORY_CELLS
                        Memory cell count
  --json-indent JSON_INDENT
                        JSON indent, set 0 to disable
  --json-dump-memory-blocks
                        dump all memory content in JSON report
```

## Supported Instructions
  * `set`
  * `jump`
  * `end`
  * All `op`s since Mindustry V7 Beta (beta 140), except `op noise`
  * `read` and `write` memory cells and banks
  * `getlink` to get memory blocks (cells/banks)
  * `set @counter` or `op @counter` as unconditional jumps


## Features
  * `@tick` and `@time` increases with processor runs
  * Stop emulation once some instruction jumps to itself
  * (Optional, Default) Stop emulation once `@counter` past the end
  * (Optional) Dump memory cells and banks
  * Dump variables into JSON report


## Limitations
  * Does NOT have `@this` yet, so do `@thisx` and `@thisy`
  * No comment in mlog code
  * (not sure)

## Python Usage
```python
from mlog_arithmetic_runner import MlogProcessor
processor = MlogProcessor(ipt=2, memory_cells=0, memory_banks=0)
code = """\
set a 90
op sin b a 0
"""
processor.assemble_code(code)
processor.run_with_limit(1000)
# When comparing 2 float-point numbers, remember there could be float precision errors.
# Use abs(a-b) < 1e-6 instead of a == b
print("a =", processor.get_variable("a"))
print("b =", processor.get_variable("b"))
```

## JSON Report Sample
```
set a 1
set a 2
set b @tick
set c @time
```
This generates:
```json
{
    "cycles": 4,
    "success": true,
    "reason": "",
    "variables": {
        "a": 2.0,
        "b": 1,
        "c": 0.016666666666666666
    },
    "memory_blocks": {}
}
```