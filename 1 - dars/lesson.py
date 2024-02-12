x = [1, 2, 3, "Python"]
d = iter(x)
try:
    while True:
        print(next(d))
except StopIteration:
    print("Stop iteration xatoligini qaytardi✖")
