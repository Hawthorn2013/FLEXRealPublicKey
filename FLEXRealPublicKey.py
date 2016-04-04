import os
import sys

if len(sys.argv) != 3:
    print('Param count error!')
    sys.exit(1)

def get_VENDORNAME_c(n):
    VENDORNAME = sys.argv[2]
    n = n % len(VENDORNAME)
    return ord(VENDORNAME[n])

print(sys.argv[1])
len_pubkey = len(sys.argv[1])
if len_pubkey % 2 != 0:
    print('Public key is even!')
    sys.exit(1)
pubkey_real = ""
print('len_pubkey=' + str(len_pubkey))
i = 0
j = 0
while i < len_pubkey:
    origin_i = int("0x" + (sys.argv[1])[i:i+2], 16)
    print('origin_s=' + (sys.argv[1])[i:i+2])
    VENDORNAME_c_i = get_VENDORNAME_c(j)
    print('VENDORNAME_c_i=' + str(VENDORNAME_c_i))
    if j % 2 == 0:
        real_i = origin_i - VENDORNAME_c_i
        real_i = real_i + 256
        real_i = real_i % 256
        print('Y2')
    elif j % 3 == 0:
        real_i = origin_i ^ VENDORNAME_c_i
        print('Y3')
    else:
        real_i = origin_i + VENDORNAME_c_i
        real_i = real_i % 256
        print('YO')
    real_s = '%02X'%(real_i,)
    print('real_s=' + str(real_s))
    pubkey_real = pubkey_real + real_s
    j = j + 1
    i = i + 2
print('pubkey_real=' + pubkey_real)