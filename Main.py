def edit_distance(str1, str2, len1, len2):
    #if length of the first string is 0 return length of second string
    if len1 == 0:
        return len2
    # if length of second strong is 0 return length of first string
    if len2 == 0:
        return len1
    # if the last character of the strings is the same, compare the rest of the substring 
    if str1[len1-1] == str2[len2-1]:
        return edit_distance(str1, str2, len1-1, len2-1)
    # compare insert, remove, and replace funtions, use the minimum of the three
    return 1 + min(edit_distance(str1, str2, len1, len2-1), edit_distance(str1, str2, len1-1, len2), edit_distance(str1, str2, len1-1, len2-1))
str1 = "winner"
str2 = "weiner"
print("Edit distance for strings weiner and winner: ")
print(edit_distance(str1, str2, len(str1), len(str2)))   
str1 = "never"
str2 = "forever"
print("Edit distance for strings never and forever: ")
print(edit_distance(str1, str2, len(str1), len(str2)))
str1 = "no"
str2 = "no"
print("Edit distance for strings no and no: ")
print(edit_distance(str1, str2, len(str1), len(str2)))