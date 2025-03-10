'''A string is said to be symmetrical  if both the halves of the string are the same and a string is said to be a palindrome string 
if one half of the string is the reverse of the other half or if a string appears the same when read forward or backward.
'''
#check for palindrome 
import palindrome_module as p

input_str_p1 = "khokho"
input_str_p2 = "radar"
print(p.if_palindrome(input_str_p1))
print(p.if_palindrome(input_str_p2))


#check for symmetrical string
def if_symmetrical(input_str):
    half_len = int(len(input_str)/2)

    first_half = input_str[0:half_len]
    if (len(input_str) % 2 == 0):
        second_half = input_str[half_len:len(input_str)]
    else:
        second_half = input_str[half_len+1:len(input_str)]

    if (first_half == second_half):
        print(f"{input_str} string is symmetrical")
        return True
    return False


input_str1 = "abcab"
input_str2 = "madam"
print(if_symmetrical(input_str_p1))
print(if_symmetrical(input_str1))
print(if_symmetrical(input_str2))