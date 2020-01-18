#!/usr/bin/env python3

import os
import subprocess
import sys


def run():
    argv = sys.argv
    index_encoding = argv.index('--encoding') if '--encoding' in argv else -1
    if index_encoding != -1:
        os.environ['PYTHONIOENCODING'] = argv[index_encoding+1]
        del argv[index_encoding:index_encoding+2]

    yamllint_exe = 'yamllint'

    if 'PATHEXT' in os.environ:
        exts = os.environ['PATHEXT'].split(os.pathsep)
        possible_exe_names = tuple(
            yamllint_exe + ext.lower() for ext in exts
        ) + (yamllint_exe,)
    else:
        possible_exe_names = (yamllint_exe,)

    for path in os.environ.get('PATH', '').split(os.pathsep):
        for possible_exe_name in possible_exe_names:
            joined = os.path.join(path, possible_exe_name)
            if os.path.isfile(joined) and os.access(joined, os.X_OK):
                yamllint_exe = joined

    files = []
    args = []

    for x in argv[1:]:
        if os.path.isfile(x):
            files += [x]
        else:
            args += [f"\"{x}\""]

    args = ' '.join(args)

    for f in files:
        subprocess.call(['echo', f])
        sys.exit(subprocess.call(
            f"{yamllint_exe} - {args} < \"{f}\"", shell=True))


if __name__ == '__main__':
    run()
