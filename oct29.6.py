string_input=input("enter a string:")
vowels="aeiouAEIOU"
vowels_count=0
consonant_count=0
for char in string_input:
    if char in vowels:
        vowels_count+=1
    else:
         consonant_count+=1
print(f"number of vowels in given string {string_input}={vowels_count}")
print(f"number of consonant in given string{string_input}={consonant_count}")