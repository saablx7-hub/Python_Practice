#1. Given the list nums = [10, 20, 30, 40, 50], write a range to get the first three elements.
""" thislist = [10,20,30,40,50]
print(thislist[0:3]) """

#2. From the list nums = [1, 2, 3, 4, 5], retrieve all elements except the first one using slicing.
""" mylist = [1,2,3,4,5]
print(mylist[1:5]) """

#3. Given colors = ['red', 'green', 'blue', 'yellow'], slice the list to get only ['green', 'blue'].
""" colors = ['red','green', 'blue', 'yellow']
print(colors[1:3]) """

#4. From fruits = ['apple', 'banana', 'cherry', 'mango'], use slicing to get ['banana', 'cherry', 'mango'].
""" fruits = ['apple', 'banana', 'cherry', 'mango']
print(fruits[1:5]) """

#5. Given nums = [5, 10, 15, 20, 25, 30], slice to get the last two elements only
""" nums = [5, 10, 15, 20, 25, 30]
print(nums[4:6]) """

#6. Given nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], use slicing to get every second element.
""" nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::2]) """

""" nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(0,9,2):
    print(x) """

#7. From the list letters = ['a', 'b', 'c', 'd', 'e', 'f'], get the elements from index 2 to the end.
""" letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[2:6]) """

""" a= ["s","a", "a" ,"t","v","i","k"]
print(a[::-1]) """

#8. Given nums = [10, 20, 30, 40, 50, 60, 70], use slicing to reverse the list
""" nums = [10, 20, 30, 40, 50, 60, 70]
print(len(nums))
print(nums[::-1]) """

""" 9. From data = [1, 3, 5, 7, 9, 11, 13], slice the list to get elements starting from index 1 up to index 5
with a step of 2. """
""" data = [1, 3, 5, 7, 9, 11, 13]
print(data[1:5:2]) """

#10. Given nums = [100, 200, 300, 400, 500, 600], use slicing to get [200, 300, 400] without
#specifying the start index explicitly
""" nums = [100, 200, 300, 400, 500, 600]
for x in nums:
  if x == 100:
    continue
  if x == 500:
    continue
  if x == 600:
    continue
  print(x) """

""" nums = [100, 200, 300, 400, 500, 600]
print(nums[:4][1:]) """

#11. Given nums = [1, 2, 3, 4, 5], what will be the output of nums[10:]? Explain why
""" nums = [1, 2, 3, 4, 5]
print(nums[10:]) """

#12. From nums = [1, 2, 3, 4, 5], slice the list to get [4, 3, 2] using a negative step value.
""" nums = [1, 2, 3, 4, 5]
print(nums[-4:-1][::-1]) """

#13. Given nested = [[1, 2], [3, 4], [5, 6]], slice to get the first two sublists.
""" nested = [[1, 2], [3, 4], [5, 6]]
print(nested[2][0])
print(nested[1][1])
print(nested[0:2]) """

#14. From nums = list(range(1, 21)), use slicing to get the last 5 elements in reverse order.
""" nums = list(range(1, 21))
print(nums[15:][::-1]) """

#15. Given nums = [10, 20, 30, 40, 50], what happens if you slice it as nums[-1:-4]? Explain and fix it
#to get [50, 40, 30]
""" nums = [10, 20, 30, 40, 50]
print(nums[2:][::-1]) """


""" 1. Employee ID Validation
You are given a list of employee IDs. Valid IDs must be between 1001 and 1020 (inclusive).
👉 Write a program to:
•	Generate valid IDs using range() 
•	Filter out invalid IDs from a given list 
 """
""" nums= list(range(1001, 1021))
a = int(input("Enter your ID :"))
if a in nums:
    print("Authorized")
else:
    print("Not Authorized") """

a= int(input("Enter your ID :"))
for a in range(1001,1021):
    print("Authorized")
    continue
else:
    print("Not Authorized")