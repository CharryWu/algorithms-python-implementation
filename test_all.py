import os
import subprocess
import pytest

root_dir = os.getcwd()

processes = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    if '.' in dirpath:
        continue
    for filename in filenames:
        if filename.endswith(".py") and os.path.join(root_dir, filename) != __file__:
            filepath = os.path.join(dirpath, filename)
            processes.append(subprocess.run(["python3", filepath]))


@pytest.mark.parametrize('proc_result', processes)
def test_execute(proc_result):
    if proc_result.returncode != 0:
        print(proc_result.stdout, proc_result.stderr)
    assert proc_result.returncode == 0

