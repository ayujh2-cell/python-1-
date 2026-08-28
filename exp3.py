assignment = ["assign1" , "assign2" , "assign3" , "assign4"]
a = str(input("Enter new assignment name: "))
b = str(input("Enter completed assignment name: "))
assignment.append(a)
assignment.remove(b)
print(assignment)
