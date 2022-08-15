'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

expense = [2200, 2350, 2600, 2130, 2190]
print(expense)
# 1
print(expense[1]-expense[0])
# 2
print(expense[0]+expense[1]+expense[2])
# 3
print(2000 in expense)
# 4
expense.append(1980)
print(expense)
# 5
expense[3] = expense[3]-200
print(expense)

'''
heros=['spider man','thor','hulk','iron man','captain america']

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''
heros=['spider man','thor','hulk','iron man','captain america']
print(heros)

# 1
print(len(heros))
# 2
heros.append("black panther")
print(heros)
# 3
heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)
# 4
heros[1:3] = ["doctor strange"]
print(heros)
# 5
heros.sort()
print(heros)

'''
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''
max_number = input("max number: ")
list_number = []
for i in range(1, int(max_number)):
   if i%2 == 1:
      list_number.append(i)
      
print(list_number)