#!/usr/bin/env python3
import sys

# Uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    N, K = map(int, input().strip().split())

    ans = False

    if K != 1:
        tmp = K * (K + 1) // 2  # Sum of first K natural numbers
        if tmp == N:
            ans = True
        elif tmp < N:
            last_element = N - (tmp - K)
            if last_element > K:
                ans = True
            else:
                ans = False
        else:
            ans = False
    else:
        ans = True

    if ans:
        print("YES")
    else:
        print("NO")

sys.stdout.close()
