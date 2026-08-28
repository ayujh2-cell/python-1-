coded_msg=input("enter the coded string: ")
secret_msg=input("enter the secret msg: ")

if (secret_msg in coded_msg):
    print("the coded message is: ",coded_msg)
else:
    print("the secret message is wrong")
