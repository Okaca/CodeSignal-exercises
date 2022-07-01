"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

A ticket number represented as a positive integer with an even number of digits.

Guaranteed constraints:
10 ≤ n < 106.

[output] boolean

true if n is a lucky ticket number, false otherwise.
"""

def solution(n):
    result = []
    while n != 0:
        n, d = divmod(n, 10)
        result.append(int(d))
    
    print(result)
    l_sum = 0
    r_sum = 0
    for i in range(int(len(result)/2)):
        l_sum += result[i]
        r_sum += result[-1-i]
    
    if r_sum == l_sum:
        return True
    else:
        return False
