#!/usr/bin/env python3

"""
This document is created by magic at 2018/12/25
"""

def fab(n):

    result = {}
    result[0] = 0
    result[1] = 1
    
    for i in range(2, n+1):
        result[i] = result[i-1] + result[i-2]
    
    return result[n]


def mprint(n):
    if n <=0:
        return 
        
    print(n)
    mprint(n-1)


if __name__ == '__main__':
    # print(fab(100))
    mprint(100)

