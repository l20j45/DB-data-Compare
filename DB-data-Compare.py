import mysql.connector
import csv
import os
from dotenv import load_dotenv

load_dotenv()

#Var Initializing
listaNuevos=[]
contadorNuevos =0
contadorDiferentes = 0
columnsList = []
hashMap = {}
tabla = os.getenv('TableToCheck')


#.env load_dotenv values
conexionHeaders = mysql.connector.connect(
                host=os.getenv('DatabaseServer1'),
                user=os.getenv('User1'),
                passwd=os.getenv('Password1'),
                database=os.getenv('Bd1'),
                port=os.getenv('Port1'))

conexionDatabase1 = mysql.connector.connect(
                host=os.getenv('DatabaseServer1'),
                user=os.getenv('User1'),
                passwd=os.getenv('Password1'),
                database=os.getenv('Bd1'),
                port=os.getenv('Port1'))

conexionDatabase2 = mysql.connector.connect(
                host=os.getenv('DatabaseServer2'),
                user=os.getenv('User2'),
                passwd=os.getenv('Password2'),
                database=os.getenv('Bd2'),
                port=os.getenv('Port2'))

#Create Csv Files to write
filecsv2 = open(os.getenv('FileCodeNotExistInServer2')+".csv", 'w',encoding="utf-8")
filecsv3 = open(os.getenv('FileWithDiferentValues')+".csv", 'w',encoding="utf-8")
myFile2=csv.writer(filecsv2)
myFile3=csv.writer(filecsv3)


# Get Table Columns
try:
    with conexionHeaders:
        with conexionHeaders.cursor() as cursor:
            sentencia = f'show columns from {tabla};'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for r in registros:
                columnsList.append(r[0]) 
            for counter,column in enumerate(columnsList):
                print(f"{counter}.- {column}")
            columnsListcopy = list(columnsList)
            eliminar=input("Ingrese las columnas que deseas borrar: ")
            print(eliminar)
            listasColumnasEliminar = eliminar.split(",")
            for popColumn in listasColumnasEliminar:
                columnsListcopy.remove(columnsList[int(popColumn)])
            print("eliminados".center(len("eliminados")+6,"*"))
            for counter,column in enumerate(columnsListcopy):
                print(f"{counter}.- {column}")
            campos = ",".join(columnsListcopy)
            print(campos)  
except Exception as e:
    print(f'Ocurrio un error {e} ')
finally:
    conexionHeaders.close()
            
#Get first Select (database1)
try:
    with conexionDatabase1:
        with conexionDatabase1.cursor() as cursor:            
            with open("DB1.csv", 'w',encoding="utf-8") as filecsv:
                myfile = csv.writer(filecsv)
                myfile.writerow(tuple(columnsListcopy))
            sentencia = f'select {campos} from {tabla}'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for r in registros:
                print(r)
                hashMap[r[0]]=r
            with open("DB1.csv", 'a',encoding="utf-8") as filecsv:
                myfile = csv.writer(filecsv)
                myfile.writerows(registros)
except Exception as e:
    print(f'Ocurrio un error {e} ')
finally:
    conexionDatabase1.close()
    
#Get Second Select (database2)    
try:
    with conexionDatabase2:
        with conexionDatabase2.cursor() as cursor:
            with open("DB2.csv", 'w',encoding="utf-8") as filecsv:
                myfile = csv.writer(filecsv)
                myfile.writerow(tuple(columnsListcopy))
            sentencia = f'select {campos} from {tabla}'
            cursor.execute(sentencia)
            registros2 = cursor.fetchall()
            with open("prod.csv", 'a',encoding="utf-8") as filecsv:
                myfile = csv.writer(filecsv)
                myfile.writerows(registros2)
except Exception as e:
    print(f'Ocurrio un error {e} ')
finally:
    conexionDatabase2.close()

for r in registros2:
    if r[0] not in hashMap:
        print("no encontrato")
        myFile2.writerow(r)
        contadorNuevos +=1
        listaNuevos.append(r[0])
    if r[0] in hashMap:
        if  r != hashMap[r[0]]:
            print("diferente")
            myFile3.writerow(r)
            contadorDiferentes+=1
print("nuevos",contadorNuevos)
print("diferentes",contadorDiferentes)
