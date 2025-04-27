

"""
Base Case Termination:

If current index idx equals string length len(s):

Return the accumulated result ans (now fully reversed)

Recursive Case:

Take the current character s[idx]

Prepend it to the accumulator: s[idx] + ans

Recur with:

Same string s

Next index idx + 1

New accumulator s[idx] + ans

Step-by-Step Execution for "abc":

CallStack	idx	s[idx]	ans (Before)	ans (After)

1st_call	0	'a'	""	"a"

2nd_call	1	'b'	"a"	"ba"

3rd_call	2	'c'	"ba"	"cba"

4th_call	3	(end)	"cba"	Returns "cba"

"""

def reverse_str(s, idx=0, ans=""):
    if idx == len(s):
        return ans
    return reverse_str(s, idx+1, s[idx] + ans) 


str_input = "mani"
print(reverse_str(str_input)) 