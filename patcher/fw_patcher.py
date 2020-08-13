#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Amazfit Bip Firmware Patcher (fw_patcher)

import sys
from pathlib import Path

FW_START_ADDRESS = 0x8008000

def main(argv):
    if len(argv) < 2:
        print('fw_patcher v0.1 by x27')
        print('usage: <fw_file> <patch_file_0> ...<patch_file_n>')
        sys.exit(2)

    with open(argv[0],'rb') as content:
        fw = bytearray(content.read())
        content.close()

    bytesPatched = 0
    for patch in argv[1:]:
        f = open(patch,'r')
        line_count = 0;
        for line in f.readlines():
            line_count = line_count + 1
            arr = line.split('#')
            if len(arr[0].strip()) == 0:
                continue
            arr = arr[0].split()
            if len(arr) != 3:
                print('err [wrong arg count] -> '+patch+':'+str(line_count),'->',line.rstrip())
                sys.exit(-1)
            address = int(arr[0],16)
            if address < FW_START_ADDRESS or address > len(fw) + FW_START_ADDRESS:
                print('err [address out range] -> '+patch+':'+str(line_count),'->',line.rstrip())
                sys.exit(-1)
            before = bytes.fromhex(arr[1])
            after = bytes.fromhex(arr[2])
            if len(before) != len(after):
                print('err [check and patch data size mismatch] -> '+patch+':'+str(line_count),'->',line.rstrip())
                sys.exit(-1)
            offset = address - FW_START_ADDRESS
            for i in range(len(before)):
                if fw[offset+i] != before[i]:
                    print('err [fw and check data mismatch] -> '+patch+':'+str(line_count),'->',line.rstrip())
                    sys.exit(-1)
                if fw[offset+i] == after[i]:
                    continue
                fw[offset+i] = after[i]
                bytesPatched = bytesPatched + 1
    
    if bytesPatched == 0:
        print('no patch data found')                
    else:
        filename = Path(argv[0]).stem+'_patched'+Path(argv[0]).suffix
        with open(filename,'wb') as content:
            content.write(fw)
        content.close()
        print('created',filename)        
        print('applied patches:',bytesPatched,'bytes')

if __name__ == "__main__":
    main(sys.argv[1:])