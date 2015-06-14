def box(width,height):
	print (width * "*")
	for i in range(height - 2):
		print ("*" + (width - 2) * " " + "*")
	print (width * "*")

# main
print (13 * "*")
print (7  * "*")
print (35 * "*")
box(10,3)
box(5,4)