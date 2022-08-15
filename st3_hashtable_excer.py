'''
st3weather new york city weather for first few days in the month of January. Write a program that can answer following,
1. What was the average temperature in first week of Jan
2. What was the maximum temperature in first 10 days of Jan
'''

# weather = []
# with open("st3weather.csv", "r") as f:
#     for line in f:
#         tokens = line.split(",")
#         day = tokens[0]
#         temp = int(tokens[1])
#         weather.append(temp)
        
# # 1
# print(sum(weather[0:7])/7)
# # 2
# print(max(weather))

'''
st3weather contains new york city weather for first few days in the month of January. Write a program that can answer following,
1. What was the temperature on Jan 9?
2. What was the temperature on Jan 4?
'''

weather = {}
with open("data/st3weather.csv", "r") as f:
    for line in f:
        tokens = line.split(",")
        day = tokens[0]
        temp = int(tokens[1])
        weather[day] = temp

# 1
print(weather["Jan 9"])
# 2
print(weather["Jan 4"])



