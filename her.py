name=int(input("no of days an employee1 work"))
print("no days hour" , name)
sum1 = 0
i=0
##name1=int(input("no of hour employee1 work in first day"))
##print("no days hour" , name1)
##name2=int(input("no days hour employee1 work in second day"))
##print("no days hour" , name2)
##name3=int(input("no hour employee1 work in third day"))
##print("no days hour" , name3)
for i in range(name):
    name1=int(input("no of hour employee1 work in day"))
    print("no of hour on day",i,":", name1)
    sum1 += name1
    
##print("you have worked", name1+name2+name3, "hour")
print("your average work", sum1/name, "in total days")
