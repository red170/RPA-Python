import pandas as pd

#Leer y mostrar el CSV con Pandas 
df = pd.read_csv("./Resources/test.csv")
df2 = pd.read_csv("./Resources/test.csv")

#Mostrar datos de una columna especifica
print(df["nombre"])

#Ordenar el Dataframe por un Conjunto de valores especifcos de forma ascendente
df_ordenado = df.sort_values("edad")
print(df_ordenado)

#Ordenar el Dataframe por un Conjunto de valores especifcos de forma descendente
df_ordenado_f = df.sort_values("edad", ascending=False)
print(df_ordenado_f)

#Concatenar 2 DF
df_conca =pd.concat([df,df2])
print(df_conca)

#Acceder a la Primeras Fila (segun el numero del parametro asi sera la cantidad de filas desde el principio que mostrara)
primer_fila = df.head(3)
print(primer_fila)

#Acceder a la Ultimas Fila (segun el numero del parametro asi sera la cantidad de filas desde el final que mostrara)
ultima_fila = df.tail(1)
print(ultima_fila)

#Acceder a la cantidad de filas y columnas
fyc_totales = df.shape
f_total = fyc_totales[0] #Filas
c_total = fyc_totales[1] #Columnas
print(fyc_totales)
print(f_total)
print(c_total)

#Obetener Data Estadistica de Data Frame
df_Info = df.describe()
print(df_Info)

#Acceder a un Elemento espcifico con loc
especifico_loc = df.loc[2,"edad"]
print(especifico_loc)

#Acceder a un Elemento espcifico con iloc
especifico_iloc = df.iloc[2,2]
print(especifico_iloc)

#Acceder a las Filas de una Columna
apellidos = df.iloc[:,1]
print(apellidos)