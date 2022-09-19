from pathlib import Path
from sys import path

script_dir = Path(path[0])

journal_path = script_dir.parent / 'Python224.csv'

text = journal_path.read_text(encoding='utf-8')

