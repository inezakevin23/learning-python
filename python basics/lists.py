testing = ["1","2","3","4","5","6","7"]
print(testing[4:])
print(testing[:4])
print(testing[1:4])
# printing this data vertically
print("\n".join(testing[4:]))
new_list = ["8","9"]
#joining lists
joint_list = [testing, new_list]
print(joint_list)
print(joint_list[0])
#printing joined list vertically
print("\n".join(joint_list[0]))
#removing one data from list
testing.pop(1)
#removing range of data
del testing[4:5]
print(testing)