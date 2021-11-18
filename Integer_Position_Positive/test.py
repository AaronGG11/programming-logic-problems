# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

'''
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].


'''

def solution(A):
    A.sort()

    min = 0
    result = None

    for i in range(0, len(A)):
        if i == 0 and i != len(A) - 1:
            continue
        elif i == len(A) - 1:
            if A[i] <= 0:
                result = 1
            else:
                result = A[i] + 1
        else:
            if A[i] <= 0:
                continue
            elif A[i] == A[i+1]:
                continue
            elif A[i]+1 == A[i+1]:
                continue
            else:
                result = A[i] + 1
                break
    
    return result

A = [1, 2, 3]
print(solution(A))