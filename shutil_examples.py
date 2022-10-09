from pathlib import Path
from sys import path

from shutil import copy2, move


script_dir = Path(path[0])
test_file = script_dir / 'vcs.txt'

# copy2(test_file, script_dir / 'vcs_copy.txt')

move(test_file, script_dir / 'vcs_copy.txt')
