import math
import modulefinder

num = str
H = 1
e=1
l=1
o=1
Space = 1
W = 1
r =1
d = 1
Hello = 1
World = 1

num = math.pi / math.pi

while num != 1:
    num = num + 1
else:
    num = 1
    H = 'H'

while num != 2:
    num = num + 1
else:
    num = 1
    e = 'e'

while num != 3:
    num = num + 1
else:
    num = 1
    l = 'l'

while num != 4:
    num = num + 1
else:
    num = 1
    o = 'o'

while num != 5:
    num = num + 1
else:
    num = 1
    Space = ' '

while num != 6:
    num = num + 1
else:
    num = 1
    W='W'

while num != 7:
    num = num + 1
else:
    num = 1
    r = 'r'


while num != 8:
    num = num + 1
else:
    num = 1
    d = "d"

Hello = H
if Hello == H:
    Hello = H + e
else:
    Hello = 'He'

if Hello == H + e:
    Hello = H + e + l
else:
    Hello = 'Hel'

if Hello == H + e + l:
    Hello = H + e + l + l
else:
    Hello = 'Hell'

if Hello == H + e + l + l:
    Hello = H + e + l + l + o
else:
    Hello = "Hello"

if Hello == H + e + l + l + o:
    World = W
else:
    Hello = "Hello"

if World == W:
    World = W + o
else:
    World = 'Wo'

if World == W + o:
    World = W + o + r
else:
    World = 'Wor'

if World == W + o + r:
    World = W + o + r + l
else:
    World = 'Worl'

if World == W + o + r + l:
    World = W + o + r + l + d
else:
    World = 'World'

tripled_pi = math.pi * 3
pi = math.pi / -math.pi
cos_pi = math.cos(tripled_pi)

if cos_pi == -1:
    Hello_World = Hello + World
else:
    Hello_World = 'Hello World'

if pi == -1:
    if Hello_World == "HelloWorld":
        Hello = H + e + l + l + o + Space
    else:
        Hello = H + e + l + l + o + Space
else:
    Hello_World = Hello + ' ' + World

Hello_World = Hello + World

print(Hello_World)