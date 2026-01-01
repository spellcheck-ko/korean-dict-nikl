#!/usr/bin/python3

import os
import sys
import zipfile

def do_extract(filename, outdir):
    zf = zipfile.ZipFile(filename)
    members = zf.namelist()
    members.sort()
    for member, i in zip(members, range(0, len(members))):
        # 1_5000_20251219.xml, 2_5000_20251219.xml, ...
        assert(len(member.split('_')) == 3)
        number = int(member.split('_')[0])
        outfilename = f"{number:03}.xml"
        print(f"Writing {member} -> {outfilename}...")
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
