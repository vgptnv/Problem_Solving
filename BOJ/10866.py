# Q. 10866
import sys

n = int(sys.stdin.readline())
deq = []
for _ in range(n):
    inp = sys.stdin.readline().split()
    command = inp.split()[0]
    if command == 'push_back':
        deq.append(int(inp[1]))
    elif command == 'push_front':
        deq = [int(inp[1])] + deq
    elif command == 'pop_front':
        if len(deq) == 0 : print(-1)
        else: print(deq.pop(0))
    elif command == 'pop_back':
        if len(deq) == 0 : print(-1)
        else: print(deq.pop(-1))
    elif command == 'size':
        print(len(deq))
    elif command == 'empty':
        if len(deq) == 0 : print(1)
        else: print(0)
    elif command == 'front':
        if len(deq) == 0 : print(-1)
        else: print(deq[0])
    elif command == 'back':
        if len(deq) == 0 : print(-1)
        else: print(deq[-1])