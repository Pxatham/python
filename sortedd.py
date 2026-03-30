n = int(input("Size: "))

nums = []
for i in range(n):
    nums.append(int(input("Enter number: ")))

sorted_flag = True

for i in range(len(nums)-1):
    if nums[i] > nums[i+1]:
        sorted_flag = False
        break

if sorted_flag:
    print("List is sorted")
else:
    print("Not sorted")