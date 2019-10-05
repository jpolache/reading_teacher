'''
Write a function that when given a number >= 0, returns an Array of ascending length subarrays.

pyramid(0) => [ ]
pyramid(1) => [  [1]  ]
pyramid(2) => [  [1],  [1, 1]  ]
pyramid(3) => [  [1],  [1, 1],  [1, 1, 1]  ]
Note: the subarrays should be filled with 1s
'''

def pyramid(n):
    op = []
    inner = []
    for _ in range(n):
        inner.append(1)
        op.append(inner[:])
    return op
    
    #[inner.append(1); op.append(inner[:]) for n in range(n)]
    
print(pyramid(0)) #, [])
print(pyramid(1)) #, [[1]])
print(pyramid(2)) #, [[1], [1, 1]])
print(pyramid(3)) #, [[1], [1, 1], [1, 1, 1]])   

'''

def pyramid(n):
    return [[1]*x for x in range(1, n+1)]
    
pyramid(0), [])
pyramid(1), [[1]])
pyramid(2), [[1], [1, 1]])
pyramid(3), [[1], [1, 1], [1, 1, 1]])
'''
