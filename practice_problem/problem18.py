# Practice Problem: Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.

words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
words_with_len=[]

for word in words:
    len_cal=len(word)
    print(f"{word} - {len_cal}")
    