mes1 = int(input('Cuanto es tu presupuesto del mes de enero: '))
mes2 = int(input("Cuanto es tu presupuesto del mes de febrero: "))
mes3 = int(input("Cuanto es el presupuesto del mes de marzo: "))


total_presupuesto = mes1+mes2+mes3

print(f"El total del presupuesto es de {total_presupuesto}")


promedio_presupuesto = total_presupuesto/3

print(f"El promedio de los presupuestos es de {promedio_presupuesto}")