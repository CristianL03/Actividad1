D1 = float(input("Importes de venta departamento 1:"))
D2 = float(input("Importes de venta departamento 2:"))
D3 = float(input("Importes de venta departamento 3:"))
SI = float(input("Salario de los vendedores:"))
T = D1+D2+D3
P = T*(33/100)
B = SI*(20/100)
if D1>=P and D2>=P and D3>=P:
  SF = SI+B
  print("El salario de todos los vendedores es:",SF)
elif D1>=P and D2<=P and D3<=P:
  SF = SI+B
  print(f"Salario vendedores depto 1:{SF}", f"Salario vendedores depto2 y 3:{SI}",sep="\n")
elif D2>=P and D1<=P and D3<=P:
  SF = SI+B
  print(f"Salario vendedores depto 2:{SF}", f"Salario vendedores depto1 y 3:{SI}",sep="\n")
elif D3>=P and D2<=P and D1<=P:
  SF = SI+B
  print(f"Salario vendedores depto 3:{SF}", f"Salario vendedores depto1 y 2:{SI}",sep="\n")
elif D1>=P and D2>=P and D3<=P:
  SF = SI+B
  print(f"Salario vendedores depto1 y 2:{SF}", f"Salario vendedores depto3:{SI}",sep="\n")
elif D1>=P and D3>=P and D2<=P:
  SF = SI+B
  print(f"Salario vendedores depto1 y 3:{SF}", f"Salario vendedores depto2:{SI}",sep="\n")
elif D3>=P and D2>=P and D1<=P:
  SF = SI+B
  print(f"Salario vendedores depto2 y 3:{SF}", f"Salario vendedores depto1:{SI}",sep="\n")
