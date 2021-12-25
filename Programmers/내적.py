def solution(a, b):
    dot_product = [a[i] * b[i] for i in  range(len(a)) ]

    return sum(dot_product)


# Test Case
a = [1,2,3,4]
b = [-3,-1,0,2]

a1 = [-1,0,1]
b1 = [1,0,-1]

print(solution(a, b))
print(solution(a1, b1))