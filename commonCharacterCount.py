"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string s1

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s1.length < 15.

[input] string s2

A string consisting of lowercase English letters.

Guaranteed constraints:
1 ≤ s2.length < 15.

[output] integer
"""

def solution(s1, s2):
    #My solution with runtime error
    """occurrance = 0
    temp = []
    for i in range(len(s1)):
        for j in range(len(s1)+1):
            if i < j:
                substring = s1[i:j]
                temp.append(substring)
    
    temp = numpy.unique(temp)
    print(temp)
    for item in temp:
        if item in s2:
            occurrance += 1
    return occurrance"""
    
    #Best solution
    count = 0
    commons = set(s1) & set(s2)
    for i in commons:
        count += min(s1.count(i), s2.count(i))
    return count
