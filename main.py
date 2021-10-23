import math

num = str
H = str
e=str
l=str
o=str
Space = str
W = str
r =str
d = str
Hello = str
World = str

H = math.tau / math.tau
e = math.e/ math.e
l = math.pi / math.pi
o = math.pi / math.pi
Space = math.pi / math.pi
W = math.pi / math.pi
r = math.pi / math.pi
d = math.pi / math.pi
Hello = math.pi / math.pi
World = math.pi / math.pi
num = math.pi / math.pi

while H != 1 and num != 1:
    H = H + 1
    num = num + 1
else:
    num = 1
    H = 'H'

while e != 2 and num != 1:
    e = e + 1
    num = num + 1
else:
    num = 1
    e = 'e'

while l != 3 and num != 1:
    l = l + 1
    num = num + 1
else:
    num = 1
    l = 'l'

while o != 4 and num != 1:
    o = o + 1
    num = num + 1
else:
    num = 1
    o = 'o'

while Space != 5 and num != 1:
    Space = Space + 1
    num = num + 1
else:
    num = 1
    Space = ' '

while W != 6 and num != 1:
    W = W + 1
    num = num + 1
else:
    num = 1
    W='W'

while r != 7 and num != 1:
    r = r + 1
    num = num + 1
else:
    num = 1
    r = 'r'

while d != 8 and num != 1:
    d = d + 1
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