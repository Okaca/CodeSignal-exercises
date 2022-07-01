"""
Given a string, output its longest prefix which contains only digits.

Example

For inputString = "123aa1", the output should be
solution(inputString) = "123".

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
3 ≤ inputString.length ≤ 100.

[output] string
"""

def solution(inputString):
    if ' ' in inputString:
        return ''
    a = re.findall('[0-9]*', inputString)
    try:
        return a[0]
    except IndexError:
        return ''  
