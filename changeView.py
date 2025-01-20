
for line in open('land/py_9.ini', encoding='utf-8'):
    if not line.startswith("VIEW_RECT="):
        continue
    print(line)
    x,y,w,h = line[len("VIEW_RECT="):].split(',')
    x = int(x)
    y = int(y)
    w = int(w)
    h = int(h)
    print(x,y,w,h)
    x = x * 1280/720
    