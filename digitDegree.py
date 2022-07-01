"""
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
solution(n) = 0;
For n = 100, the output should be
solution(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
5 ≤ n ≤ 109.

[output] integer
"""

def solution(n):
    sum = 0
    degree = 0
    for i in str(n):
        sum += int(i)
    if n//10 == 0:
        return degree
    degree += 1
    while sum//10 !=0:
        degree += 1
        temp = 0
        for i in str(sum):
            temp += int(i)
        sum = temp
    return degree
