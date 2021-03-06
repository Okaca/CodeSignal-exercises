"""
Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
solution(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.
"""

def solution(sequence):
    #Best and working solution
    def is_increasing(lst):
        for idx in range(len(lst)-1):
            if lst[idx] >= lst[idx + 1]:
                return False
        return True

    for idx in range(len(sequence) - 1):
        if sequence[idx] >= sequence[idx + 1]:
            fixable = is_increasing([*sequence[:idx], *sequence[idx+1:]]) or is_increasing([*sequence[:idx+1], *sequence[idx+2:]])
            if not fixable:
                return False

    return True
    
    #my solution
    """res = all(i < j for i, j in zip(sequence, sequence[1:]))
    
    if res:
        return True
    else:
        for x in range(len(sequence)):
            test_list = sequence[0:x] + sequence[(x+1):]
            result = all(i < j for i, j in zip(test_list, test_list[1:]))
            if result:
                return True
        return False"""
            
