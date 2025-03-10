1. Extracting number from a string 
You will be provided a string str in which you have to find all the numbers and print them.

Note: In Python, you need to import re module to use regex

Example:

Input: 
str = asdasd123asmdasdk34234kfdsd34sdfk5
Output: 
123 34234 34 5


2. Password validation with regex
You will be provided a string str which you have to validate.

The validation rules are as follows:

The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
In any other case the string is not valid.
Example:

Input: 
str = asdsab@!@234
Output: 
True


3.Find the type of IP address
Given an IP address as input, write a Python program to find the type of IP address i.e. either IPv4 or IPv6. 
If the given is neither of them then print neither.

Input: 192.0.2.126
Output: IPv4

Input: 3001:0da8:75a3:0000:0000:8a2e:0370:7334
Output: IPv6

Input: 36.12.08.20.52
Output: Neither



4. Find Indices of Overlapping Substrings
To count the number of overlapping sub-strings in Python we can use the Re module. To get the indices we will use the re.finditer() method. 
But it returns the count of non-overlapping indices only.

Examples:

Input: String: “geeksforgeeksforgeeks” ; Pattern: “geeksforgeeks” 
Output: [0, 8] 


5. Extract Strings between HTML Tags
Given a String and HTML tag, extract all the strings between the specified tag.

Input : ‘<h1>Gfg</h1> is <h1>Best</h1> I love <h1>Reading CS</h1>’  , tag = “h1” 
Output : [‘Gfg’, ‘Best’, ‘Reading CS’] 


6. Check if String Contain Only Defined Characters using Regex
Input: ‘657’ let us say regular expression contains the following characters- (‘78653’)
Output: Valid

Input: ‘7606’ let us say regular expression contains the following characters-
(‘102’) 
Output: Invalid


7. Find files having a particular extension using RegEx
Search “.xml” pattern in files' list.

