while True:
	operasi = input("\ntentukan operasi yang ingin anda lakukan,misalnya +,-,*,/:")
	if operasi not in("+","-","*","/"):
		print("maaf,operasi yang anda masukkan tidak valid")
		pass
	
	
	x =int(input("masukkan angka pertama:"))
	y =int(input("masukkan angka kedua:"))
	z =int(input("masukkan angka ketiga:"))
	
	if operasi == "+":
		print("hasil dari",x,"+",y,"+",z,"=",x+y+z)
	elif operasi == "-":
		print("hasil dari",x,"-",y,"-",z,"=",x-y-z)
	elif operasi == "*":
		print("hasil dari",x,"*",y,"*",z,"=",x*y*z)
	elif operasi == "/":
		print("hasil dari",x,"/",y,"/",z,"=",x/y/z)