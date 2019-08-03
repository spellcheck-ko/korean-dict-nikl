#!/usr/bin/python3

import os
import sys
import zipfile

def do_extract(filename, outdir):
    zf = zipfile.ZipFile(filename)
    members = zf.namelist()
    members.sort()
    for member, i in zip(members, range(0, len(members))):
        outfilename = member.split('_')[1]
        s = zf.open(member).read().decode('UTF-8')
        with open(os.path.join(outdir, outfilename), 'w') as fp:
            fp.write(s)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: %s filename.zip' % sys.argv[0])
        sys.exit(1)
    filename = sys.argv[1]
    outdir = '.'
    do_extract(filename, outdir)
