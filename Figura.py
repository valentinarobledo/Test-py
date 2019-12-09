n = int(input("Ingrese número"))

if n > 0:

	for i in range(1, n+1):
		print("")
		for j in range(1, i+1):
			print(j, end=" ")

	for i in range(n-1, 0, -1):
		print("")
		for j in range(1, i+1):
			print(j, end=" ")

else: 

	print("Incorrecto")	