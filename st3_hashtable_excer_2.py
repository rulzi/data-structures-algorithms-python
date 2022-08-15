'''
st3poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
You have to read this file in python and print every word and its count as show below.
Think about the best data structure that you can use to solve this problem and figure 
out why you selected that specific data structure.
'''

poems = {}
with open("data/st3poem.txt", "r") as f:
    for line in f:
        words = line.split(" ")
        for word in words:
            word = word.replace(",", "")
            word = word.replace(".", "")
            word = word.replace("\n", "")
            if word in poems:
                poems[word] += 1
            else:
                poems[word] = 1
        
print(poems)