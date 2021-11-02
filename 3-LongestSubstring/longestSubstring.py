"""
A function to find the longest substring without repeating characters.
Leetcode question #3

Parameters
----------
s: str
    The string

Sample Output
-------------
"abcabcbb" => 3

Time Complexity
---------------
O(N) - Passes though the string once

Space Complexity
----------------
O(N) - Worst case, no repeating characters, created substring
       will be same size as original input

Explanation
-----------
Initialize empty substring and set maxLength to zero.
For each character in the string
    If the character is not in the substring
        Add the character to the substring and set maxLength to 
        max(maxLength, length of substring).
    Else (the character is in the substring)
        Split the substring where the character appears
        and append it to the end of the substring.
"""

def lengthOfLongestsubstringstring(s):
    maxLength = 0
    substring = ''
    try:
        for char in s:
            if char not in substring:
                substring += char
                maxLength = max(maxLength, len(substring))
            else:
                splitIndex = substring.index(char)
                substring = substring[splitIndex+1:] + char
        return maxLength
    except TypeError:
        print("Oops, something went wrong!")
