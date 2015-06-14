class Avenger:
	avengersCount = 0

	def __init__(self,name,power):
		Avenger.avengersCount += 1
		self.name = name
		self.power = power


	def howMany():
		print("total avengers %d" % Avenger.avengersCount)

	def getName(self):
		print("Avengers Name: "+self.name+" have power"+ self.power)


hulk = Avenger("Hulk","Angryness")
print(hulk.name)
print(hulk.power)


print("AvengersCount: " , Avenger.avengersCount)
Avenger.howMany()
hulk.getName()

print("+++++++++++++++++++++++++")

ironMan = Avenger("ironMan","suite")

print(ironMan.name)
print(ironMan.power)
print("AvengersCount: " , Avenger.avengersCount)
Avenger.howMany()
ironMan.getName()

hulk.size = "Very Big"

print(hulk.size)

del hulk.power

# print(hulk.power)

print(hulk.name)


x= getattr(hulk,"name")
print(x)
print(setattr(hulk,"name","BadaHulk"))

print(hulk.name)


