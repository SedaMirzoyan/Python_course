import re

#extracting numbers from a string
def check_digit(input_str):
    digit = re.findall("\d", input_str)

    if (len(digit) != 0):
        print("String contains digits:", digit)
    else:
        print("String does not contain any digit")
    return digit


#password validation with regex
def validate_psswd(input_str):
    psswd_match = re.match(r"^[a-z].*[@_!#$%^&*()<>?/\|}{~:]*\d*", input_str)

    if(psswd_match):
        return True
    else:
        return False


#find the type of IP Address using Regex
def determine_IP(input_str):
    ipv4_match = re.match(r"^\d+\.\d+\.\d+\.\d+$", input_str)
    ipv6_match = re.match(r"^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$", input_str)
    #ipv6_match = re.match(r"^[\da-fA-F]{1,4}+\:[\da-fA-F]{1,4}\:[\da-fA-F]{1,4}\:[\da-fA-F]{1,4}\:[\da-fA-F]{1,4}\:[\da-fA-F]{1,4}\:[\da-fA-F]{1,4}\:[\da-fA-F]{1,4}$", input_str)
    ipv6_match = re.match(r"^([\da-fA-F]{1,4}:){7}[\da-fA-F]{1,4}$", input_str)

    if(ipv4_match):
        print("IPv4 address")
    elif(ipv6_match):
        print("IPv6 address")
    else:
        print("Neither")


#Check if String Contains Only Defined Characters               
def check_chars(input_str, pattern):
    chars = re.findall(r"[0-9a-zA-Z]", pattern)
    chars_in_str = re.findall(r"[0-9a-zA-Z]", input_str)

    for i in chars:
        if i not in chars_in_str:
            return False

    return True


#find Indices of Overlapping Substrings
def find_overlapping_indices(input_str, pattern):
    index_match = re.finditer(f"(?={pattern})", input_str)
    match_list = []
    
    for i in index_match:
        match_list.append(i.start())

    return match_list


#extract Strings between HTML Tags
def extract_strs_between_tags(input_str, tag):
    match_pattern = re.findall(rf"\<{tag}\>(.*?)\<\/{tag}\>", input_str)

    if(match_pattern):
        return match_pattern
    else:
        return False
    



#find files having a particular extension using RegEx
def find_files_xml_ext(input_list):
    ext_match = r"\.xml$"
    out = []

    for ind, list_item in enumerate(input_list):
        if(re.search(ext_match, list_item)):
            tuple_data = (ind, list_item)
            out.append(tuple_data)
            
    return out




def main():
    input_str1 = "asdasd123asmdasdk34234kfdsd34sdfk5"
    input_str2 = "asdasddfk"

    check_digit(input_str1)
    check_digit(input_str2)

    psswd1 = "asdsab@!@234"
    psswd2 = "3&&asdsab@!@234"

    print(validate_psswd(psswd1))
    print(validate_psswd(psswd2))

    test_IP_1 = "192.0.2.126"
    test_IP_2 = "3001:0da8:75a3:0000:0000:8a2e:0370:7334"
    test_IP_3 = "36.12.08.20.52"

    determine_IP(test_IP_1)
    determine_IP(test_IP_2)
    determine_IP(test_IP_3)

    chars1 = "a657"
    chars2 = "a65c7"
    test_str = "786b5a3" 
    print(check_chars(test_str, chars1))
    print(check_chars(test_str, chars2))
 
    test_index_str = "geeksforgeeksforgeeks"
    pattern_index_str = "geeksforgeeks"
    print(find_overlapping_indices(test_index_str, pattern_index_str))

    test_tag = "<b>Gfg</b> is <b>Best</b>. I love <b>Reading CS</b>"
    tag = "b"
    print(extract_strs_between_tags(test_tag, tag))


    test_list = ["gfg.html", "geeks.xml", "computer.txt", "geeksforgeeks.jpg", "file.xml"]
    print(find_files_xml_ext(test_list))

if __name__ == "__main__":
    main()