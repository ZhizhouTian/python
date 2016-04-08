from __future__ import print_function
import os

codebase_dir = "/home/zhizhoutian/workspace/sprdroid6.0_trunk_16a/"
subdirs = ["frameworks", "bionic", "external", "libcore", "system"];

outfilp = open(codebase_dir+"out/cscope.file", 'w+')

for subdir in subdirs:
    for root, dirs, files in os.walk(codebase_dir + subdir):
        for f in files:
            if f.endswith(".c") or f.endswith(".h") or f.endswith(".cpp"):
                print(os.path.join(root, f), file=outfilp)
