#!/bin/python3

import sys
import base64

if(len(sys.argv) != 2):
    print('''usage: %s <flag>''' % sys.argv[0])
    exit(1)

input = str(sys.argv[1])

tmp = '''Yeah, it's pretty clear, I ain't no size two
But I can shake it, shake it, like I'm supposed to do
'Cause I got that boom boom that all the boys chase
And all the right junk in all the right places
I see the magazines working that Photoshop
We know that shit ain't real, come on now, make it stop
If you got beauty beauty just raise 'em up
'Cause every inch of you is perfect from the bottom to the top

Yeah, my momma she told me don't worry about your size
She says, boys like a little more booty to hold at night
(That booty, booty, uh, that booty booty)
You know I won't be no stick-figure, silicone Barbie doll
So, if that's what's you're into then go ahead, move along and take your flag:
%s

- m1ckey
''' % input

tmp = tmp.encode()
#print('original: ' + tmp.decode())

tmp = base64.b64encode(tmp)
#print('base64: ' + tmp.decode())

tmp = base64.b32encode(tmp)
#print('base32: ' + tmp.decode())

hex = ''
for c in tmp:
    hex += '{:02x} '.format(c)
#print('hex: ' + hex)
tmp = hex.encode()

# too hard xD
# tmp = str(int.from_bytes(tmp, "big")).encode()
# print('decimal: ' + tmp.decode())

oct = ''
for c in tmp:
    oct += '{:03o} '.format(c)
#print('octal: ' + oct)
tmp = oct.encode()

bin = ''
for c in tmp:
    bin += '{:08b} '.format(c)
#print('binary: ' + bin)
tmp = bin.encode()

print(bin)
