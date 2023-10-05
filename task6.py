#Q1
lst = [30, 75, 9, 97, 50, -4, 70, 59]
print(max(lst))
lst.remove(min(lst))
lst.sort()
print(lst[-4:])

#Q2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
count=0
for inner_list in main_lst:
   for item in inner_list:
       if "python"==item:
            count+=1
print(count)

#Q3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
print(" ".join(my_lst).title())

#Q4
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
copy_lst=my_lst[:]
print(copy_lst)

#Q5
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2:]=my_lst[2:][::-1]
print(my_lst)
#Another solution
my_Lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_Lst[2],my_Lst[4]=my_Lst[4],my_Lst[2]
print(my_Lst)

#Q6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
print(sum(nums))
#Another solution using the for loop
sum_num=0
for num in nums:
    sum_num+=num
print(sum_num)

#Q7
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2=(9,)
new_tuple=tuple1+tuple2
print(new_tuple)

#Q8
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
new_tuple=tuple1+tuple2
print(new_tuple)



