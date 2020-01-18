#!/usr/bin/env python3

import os
import subprocess
import sys

args = ' '.join([f"\"{x}\"" for x in sys.argv[1:-2]])
file_path = sys.argv[-1]

yamllint_exe = 'yamllint'

if 'PATHEXT' in os.environ:
    exts = os.environ['PATHEXT'].split(os.pathsep)
    possible_exe_names = tuple(
        'yamllint' + ext.lower() for ext in exts
    ) + ('yamllint',)
else:
    possible_exe_names = ('yamllint',)

for path in os.environ.get('PATH', '').split(os.pathsep):
    for possible_exe_name in possible_exe_names:
        joined = os.path.join(path, possible_exe_name)
        if os.path.isfile(joined) and os.access(joined, os.X_OK):
            yamllint_exe = joined

subprocess.call(f"echo {file_path}")
sys.exit(subprocess.call(
    f"{yamllint_exe} - {args} < \"{file_path}\"", shell=True))
