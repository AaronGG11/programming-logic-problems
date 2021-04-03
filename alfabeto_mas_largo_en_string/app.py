def lengthOfLongestSubstring(s):
    checklist = {}
    starting_index_of_current_substring = 0
    finishing_index_of_longest_substring = 0
    length_of_longest_substring = 0

    for i, v in enumerate(s):
        if v in checklist:
            starting_index_of_current_substring = max(starting_index_of_current_substring, checklist[v] + 1)
        
        checklist[v] = i
        length_of_longest_substring = max(length_of_longest_substring, i - starting_index_of_current_substring + 1)
        
    return length_of_longest_substring

## Main
result = {}

for string in ["abcbdbbdsdfng"]:
    result[string] = lengthOfLongestSubstring(string)

for i in result:
    print(result)
