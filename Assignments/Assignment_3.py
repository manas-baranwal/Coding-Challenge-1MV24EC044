s=input("enter a string: ")
v="aeiouAEIOU"
vowel=0
consonant=0
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z':
        if i in v:
            vowel+=1
        else:
            consonant+=1

print("Vowels=", vowel)
print("Consonants=", consonant)



