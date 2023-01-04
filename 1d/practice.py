# Find Number of Days Above Avg Temp.
num_of_days = int(input("Enter the days \t"))
temp_list = list()
total = 0
for day in range(num_of_days):
    temp = int(input(f"Enter {day+1}'s day temp \t"))
    temp_list.append(temp)
    total += temp
avg_temp = total/len(temp_list) 
print(avg_temp)
li = [ temp  for temp in temp_list if temp>avg_temp ]
print(li)
# for temp in temp_list:
#     if temp > avg_temp:
#         print(temp_list.index(temp)+1)