from dbConnection import mydb, mycursor 

def insert(idItem, value, stock):
  sql = "INSERT INTO Store VALUES (%s,%s,%s)"
  vals = (idItem, value, stock)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(idItem, value, stock):
  if(value):
    sql = "UPDATE Store SET value = %s WHERE idItem = %s"
    vals = (value,idItem)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(stock):
    sql = "UPDATE Store SET stock = %s WHERE idItem = %s"
    vals = (stock,idItem)
    mycursor.execute(sql,vals)
    mydb.commit()
    
def selectAll():
  mycursor.execute("SELECT * FROM Store")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def select(idItem):
  sql = "SELECT * FROM Store WHERE idItem = '%s'" %(idItem)
  mycursor.execute(sql)
  for i in mycursor:
    return i

def delete(idItem):
  sql = "DELETE FROM Store WHERE idItem = '%s'" %(idItem)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM Store")
  mydb.commit()





