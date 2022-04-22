from dbConnection import mydb, mycursor 
import map1

def printTerminal():
  for i in mycursor: 
    print (i)

print("main")
map1.insert()
map1.select()
printTerminal()



# autoincrement no script

# modularizar

# DAO

# boolean inserir um obj(obj)
# INSERT

# bool apagar obj(obj)
# DELETE

# bool apagar obj(PK)
# DELETE

# bool atualizar obj(obj)
# UPDATE

# OBJ buscar por chave primaria obj(chave prim)
# SELECT

# Coleção buscar todos obj() 
# SELECT