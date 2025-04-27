


def reverse_str(s, idx=0, ans=""):
    if idx == len(s):
        return ans
    return reverse_str(s, idx+1, s[idx] + ans) 

str_input = "mani"
print(reverse_str(str_input)) 