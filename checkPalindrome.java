/*
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.
Input/Output

[execution time limit] 3 seconds (java)

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.
*/

boolean solution(String inputString) {
    int length = inputString.length();
    String reverse = "";
    for (int i = length-1; i >= 0; i--){
        reverse = reverse + inputString.charAt(i);
    }
    return reverse.equals(inputString);
}
