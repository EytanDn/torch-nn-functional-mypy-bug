# torch-nn-functional-mypy-bug
Minimal repo for reproducing bug
## description

When running mypy on a file that imports `torch.nn.functional` it fails when `torchvision` is installed.

## Environment info

- OS: Ubuntu 22.04.4
- miniconda: 24.5.0
- Python: `3.10`, `3.11`, `3.12`

## Script content

```python
# harmless.py
import torch
import torch.nn.functional

def harmless(x: torch.Tensor) -> torch.Tensor:
    return x
```

## Steps to reproduce

1. Create conda environment
```bash
conda create -n mypy python=3.11 -y
conda activate mypy
```
2. Install mypy and run sanity check
```bash
pip install mypy
mypy --follow-imports=skip harmless.py
```
result:
```bash
harmless.py:1: error: Cannot find implementation or library stub for module named "torch"  [import-not-found]
harmless.py:2: error: Cannot find implementation or library stub for module named "torch.nn.functional"  [import-not-found]
harmless.py:2: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
harmless.py:2: error: Cannot find implementation or library stub for module named "torch.nn"  [import-not-found]
Found 3 errors in 1 file (checked 1 source file)
```

3. install torch and run
```bash
pip install torch 
mypy --follow-imports=skip harmless.py
```
result: 
```bash
Success: no issues found in 1 source file
```

4. install torchvision and run
```bash
pip install torchvision
mypy --follow-imports=skip harmless.py
```

result:
```bash
Traceback (most recent call last):
  File "/home/eytan/miniconda3/envs/mypy/bin/mypy", line 8, in <module>
    sys.exit(console_entry())
             ^^^^^^^^^^^^^^^
  File "/home/eytan/miniconda3/envs/mypy/lib/python3.11/site-packages/mypy/__main__.py", line 15, in console_entry
    main()
  File "mypy/main.py", line 103, in main
  File "mypy/main.py", line 187, in run_build
  File "mypy/build.py", line 193, in build
  File "mypy/build.py", line 268, in _build
  File "mypy/build.py", line 2950, in dispatch
  File "mypy/build.py", line 3348, in process_graph
  File "mypy/build.py", line 3475, in process_stale_scc
  File "mypy/build.py", line 2507, in write_cache
  File "mypy/build.py", line 1568, in write_cache
  File "mypy/nodes.py", line 390, in serialize
  File "mypy/nodes.py", line 4012, in serialize
  File "mypy/nodes.py", line 3949, in serialize
  File "mypy/nodes.py", line 3374, in serialize
  File "mypy/types.py", line 671, in serialize
  File "mypy/types.py", line 2428, in serialize
  File "mypy/types.py", line 1451, in serialize
  File "mypy/types.py", line 671, in serialize
  File "mypy/types.py", line 3093, in serialize
AssertionError: Internal error: unresolved placeholder type None
```

### Addendum

#### pip freeze
- [python 3.10](pipfreeze/python310.txt)
- [python 3.11](pipfreeze/python311.txt)
- [python 3.12](pipfreeze/python312.txt)