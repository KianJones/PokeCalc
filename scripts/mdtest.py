# import re

# re.compile("$:

def enquote(s):
    return "'" + s[0:len(s)-1] + "':"

print ""
    
with open('mdtest.txt', 'r') as f:
    for line in f.readlines():
        for word in line.split(' '):
            if word[len(word)-1] == ":" and not word[len(word)-2] == '"':
                word.replace(word, enquote(word))
        print line