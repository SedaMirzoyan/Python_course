def gfg(input_str):
    str_lower = input_str.lower()

    if (str_lower.startswith("gfg") and str_lower.endswith("gfg")):
            return True
    return False


input_str1 = "gFgabcdEGfG"
input_str2 = "GgfhTnagfg"
print(gfg(input_str1))
print(gfg(input_str2))

