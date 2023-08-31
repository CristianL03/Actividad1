T = str(input("Nombre del trabajador:"))
H = int(input("Numero de horas trabajadas:"))
V = float(input("Valor por hora:"))
SN = V*40
SF = 0
HE = 0
if H<=40:
  float(SF = V*H)
else:
  HE = H-40
  if HE<=8:
    float(SF = SN+(2*V*HE))
  else:
    HE = H-48
    float(SF = SN+(2*V*8)+(3*V*HE))
print("El trabajador",T,"devengo:",SF)