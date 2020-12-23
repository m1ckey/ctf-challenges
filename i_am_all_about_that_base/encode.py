#!/usr/bin/env python3

import sys
import base64

if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} <flag>')
    exit(1)

flag = str(sys.argv[1])

txt = f'''Yeah, it's pretty clear, I ain't no size two
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
{flag}

- m1ckey
'''

txt = txt.encode()
txt = base64.b64encode(txt)
txt = base64.b32encode(txt)
txt = (' '.join([f'{c:02x}' for c in txt])).encode()
txt = (' '.join([f'{c:03d}' for c in txt])).encode()
txt = (' '.join([f'{c:03o}' for c in txt])).encode()
txt = (' '.join([f'{c:08b}' for c in txt])).encode()

print(txt.decode())
