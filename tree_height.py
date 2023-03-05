import sys
import threading
import numpy


def compute_height(n, parents):
    sakne = None
    f = [[]for i in range(n)]
    for k in range(n):
        if parents[k] == -1:
          sakne = k 
        else:
          f[parents[k]].append(k)



# Write this function
    def max_height(o):
        augstums = 1 
        if not f[o]:
            return augstums
        else:
            for child in f[o]:
                augstums = max(augstums, max_height(child))
            return augstums + 1
    return max_height(sakne)
# Your code here

def main():
    atbilde = input("F vai I?")
    if "I" in atbilde:
       n = int(input())
       parents = list(map(int,input().split()))
    elif "F" in atbilde:
         failanos = input()
         file = './test/' + failanos
         if "a" not in failanos:
             try: 
                 with open(file) as file1:
                    n = int(file1.readline())
                    parents = list(map(int, file1.readline().split()))
             except Exception as kluda:
                 print("kluda:", str(kluda))
                 return
         else:
             print("nepareizs nosaukums")
             return

    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
