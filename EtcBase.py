from dbConnection import mydb, mycursor 

def insert(idEtc, etcName, value):
  sql = "INSERT INTO EtcBase VALUES (%s,%s,%s)"
  vals = (idEtc, etcName, value)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(idEtc, etcName, value):
  if(etcName):
    sql = "UPDATE EtcBase SET etcName = %s WHERE idEtc = %s"
    vals = (etcName,idEtc)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(value):
    sql = "UPDATE EtcBase SET value = %s WHERE idEtc = %s"
    vals = (value,idEtc)
    mycursor.execute(sql,vals)
    mydb.commit()
    
def selectAll():
  mycursor.execute("SELECT * FROM EtcBase")

def select(idEtc):
  sql = "SELECT * FROM EtcBase WHERE idEtc = '%s'" %(idEtc)
  mycursor.execute(sql)

def delete(idEtc):
  sql = "DELETE FROM EtcBase WHERE idEtc = '%s'" %(idEtc)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM EtcBase")
  mydb.commit()





