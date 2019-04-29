import time

p = 0
print("Podaj do ilu ma odliczać stoper")
s = int(input())


t = time.time()
time.sleep(1)
k = time.time()

while True:
    t = time.time()
    time.sleep(1)
    k = time.time()
    if s > p:
        p +=1
        print("{} sekunda".format(p))

    if s == p:
        break
