"""
A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc. Note that letter a has no previous letter.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be solution(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be solution(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be solution(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string of lowercase English letters.

Guaranteed constraints:
3 ≤ inputString.length ≤ 50.

[output] boolean

Return true if the string is beautiful, false otherwise.
"""


def solution(inputString):   
    
    alp_count = [0]*26
    newStr = sorted(inputString)
    order = ord('a')
    index_ref = order + 1
    charsum = 0
    for i in newStr:
        if ord(i) == order:
            charsum += 1
        else:
            order += 1
            alp_count[ord(i)-index_ref] = charsum
            charsum = 1
    if charsum != 0:
        alp_count[ord(i)-index_ref+1] = charsum
    
    x=[inputString.count(i) for i in string.ascii_lowercase]
    print(string.ascii_lowercase)
            
    return alp_count == sorted(alp_count, reverse=True)
