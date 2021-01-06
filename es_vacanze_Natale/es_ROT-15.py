def rot15(s):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[15:]+chars[:15]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c)>-1 else c
    return ''.join( rot_char(c) for c in s )

print(rot15(i))    