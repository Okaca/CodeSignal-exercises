"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string inputArray

A non-empty array.

Guaranteed constraints:
1 ≤ inputArray.length ≤ 10,
1 ≤ inputArray[i].length ≤ 10.

[output] array.string

Array of the longest strings, stored in the same order as in the inputArray.
"""

def solution(inputArray):
    max_len = 0
    temp = []
    for item in inputArray:
        item_len = len(item)
        if item_len > max_len:
            max_len = item_len
    print(max_len)
    
    for item in inputArray:
        if len(item) == max_len:
            temp.append(item)
            
    return temp
