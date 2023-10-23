# 1
word1 = "123456789"
# A
print(word1[2])

# B
before_last = (word1[-2])
print(before_last[0])

# C
print(word1[0:5])

# D
print(word1[:-2])

# E
print(word1[1::2])

# F
print(word1[0::2])

# G
print(word1[::-1])

# H
print(word1[::-2])

# I
print(len(word1))

# 2
word2 = "I do not have time ;-;"
print(word2[:-1].count(" ")+1)

# 3
word3 = "CH Ch cH notch Nh"
word_lower = word3.lower()
find_ch = word_lower.find("ch")

while find_ch != -1:
    print("'ch' found at position:", find_ch)
    find_ch = word_lower.find("ch", find_ch + 1)
else:
    print("There are no more letters 'ch'")

# 4
new = None
word4 = "hehheh"
first = word4.find('h')
last = word4.rfind('h')

if first == -1:
    print("The letter h is not found in this string.")
else:
    new = word4[:first + 1] + word4[first + 1:last].replace('h', 'H') + word4[last:]
    print("Replaced string:", new)
