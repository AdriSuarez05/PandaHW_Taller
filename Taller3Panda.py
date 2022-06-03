# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:18:55 2022

@author: Adriana Suarez
"""

"""
email: adriana.suarezb@upb.edu.co
ID: 502197

"""
import pandas as pd

my_data = pd.read_excel(r'C:\Users\Adriana Suarez\my_python\Spyder\Tabla_InfoEstudiantes.xlsx', sheet_name='Tabla_InfoEstudiantes')



#def indice_masacorporal():
    
    
# EJERCICIO 1: 
# Calcule el índice de masa corporal de cada individuo 
# y lo almacene en una variable
    
my_data["IMC"] = round(my_data['Peso (kg)']/(my_data['Altura']**2))


#Ciclo para mostrar el IMC junto con el nombre de la persona que tuvo el resultado
n_imc = len(my_data['IMC'])
n_nombre = len(my_data['Nombre'])
index = 0

while index < n_imc:
    print("Tu índice de masa corporal es: " + str(my_data['IMC'][index]) + " " + my_data['Nombre'][index])
    index += 1
    
print(" ")


# EJERCICIO 2: 
# Calcular el capital obtenido en la inversión

capital_final = my_data['Dinero a invertir']*((my_data['Interes anual']/100+1)**my_data['Años de inversión'])
print("El capital final es: ")
print(capital_final)
print(" ")




# Ejercicio 3 
# Con una función se logró hacer el condicional del tiempo para crear la columna
# de descuento y luego se uso la funcion apply para llamar la función creada por el 
# programador


precio_pan = 15000

def calcular_descuento(time):
    
    if time <= 6:
        return 0.1
    
    elif (time > 6) & (time <= 12):
        return 0.2
    
    elif (time > 12) & (time <=18):
        return 0.3
    
    else:
        return 0.4
    
my_data["Descuento"] = my_data['HoraCompra (h)'].apply(calcular_descuento)
my_data["Precio_final"] = precio_pan - my_data['Descuento']    
    



# Ejercicio 4
# Debe organizar en el DataFrame (nueva columna) las extensiones de forma
# que si el sexo de la persona es M, debe poner como extensión 11 y si el
# sexo es F, debe poner como extensión 10.

# Función que crea la nueva columna que guarda los valores de la extensión
def funcion_extension(sexo):
    if sexo == "Masculino":
        return 11
    
    elif sexo == "Femenino":
        return 10
my_data["Extension_Num"] = my_data['Sexo'].apply(funcion_extension)    



# metodo While para imprimer el número de telefono 
# con la extensión por medio de la consola
    
n_numext = len(my_data['Extension_Num']) 
aux = 0
    
while aux < n_numext:
    print("+ " + my_data['Numero telefonico'][aux] + " - " + str(my_data['Extension_Num'][aux]))
    aux+= 1
#











