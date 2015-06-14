def move(time,speed):
	print("I am moving"+ str(speed) + "kmph" + "at" + str(time))
	speed = speed - 1
	time = time + 1
	print("I am moving on" + str(speed) + "kmph" + "at" + str(time))

move(10,5)
print("____________")
move(2,10)
print("____________")



def stars(n):
 	print(n * "*")

stars(5)
stars(10)
stars(20)