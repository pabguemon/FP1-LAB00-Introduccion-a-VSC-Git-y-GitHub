from datetime import datetime

hora = datetime.now().hour

nombre=input("¿Cómo te llamas? ")

if hora<12:
    print(f"Buenos días, {nombre}")
elif hora>=12 and hora<21:
    print(f"Buenas tardes, {nombre}")
else:
    print(f"Buenas noches, {nombre}")