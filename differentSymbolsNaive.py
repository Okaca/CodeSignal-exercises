"""
Given a string, find the number of different characters in it.

Example

For s = "cabca", the output should be
solution(s) = 3.

There are 3 different characters a, b and c.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ s.length ≤ 1000.

[output] integer
"""

def solution(s):
    chars = numpy.zeros(28, dtype = int)
    a = ord('a')
    for i in s:
        chars[ord(i)-a] += 1
    
    return sum([x>0 for x in chars])
