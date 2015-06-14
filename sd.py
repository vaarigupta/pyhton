name=int(input("enter no of employees"))
for y in range(1, name+1):
	n=int(input("employee:"+ str(y) +"how many days:"))
	for x in range(0,n):
		hrs=int(input("hours ?"))
	tot=tot+hrs
	print("total=" +str(tot))
	avg=tot/n
	print("average=" +str(avg))	