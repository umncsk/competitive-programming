w,h,x,y = map(int, input().split())

if x >= (w / 2):
    wx = (w - x) * h
else:
    wx = (x - w) * h

if y >= (h / 2):
    hy = (h - y) * w
else:
    hy = (y - h) * w

is_some = 0
if wx == hy:
    is_some = 1

print(max(wx,hy), is_some)