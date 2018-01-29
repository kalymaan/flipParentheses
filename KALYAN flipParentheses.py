def rParentheses(s):
    
    # base case:
    if '(' not in s:
        return s

    for i in range(len(s)):
        if s[i] == '(':
            firstIndex = i
            
    secondIndex = firstIndex + s[firstIndex:].find(')')
    
    beg = s[:firstIndex]
    middle = s[firstIndex+1:secondIndex]
    end = s[secondIndex+1:]

    newS = beg + middle[::-1] + end
    
    return rParentheses(newS)

test = "a(bc)de"
print rParentheses(test)
test = "a(bcdefghijkl(mno)p)q"
print rParentheses(test)
test = 'co(de(fight)s)'
print rParentheses(test)
test = "Code(Cha(lle)nge)"
print rParentheses(test)
test = "Where are the parentheses?"
print rParentheses(test)
test = "abc(cba)ab(bac)c"
print rParentheses(test)
test = "The ((quick (brown) (fox) jumps over the lazy) dog)"
print rParentheses(test)



