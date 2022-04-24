from dbConnection import mydb, mycursor 

def insert(idMap,mapName,spawnPosition):
  sql = "INSERT INTO Map VALUES (%s,%s,%s)"
  vals = (idMap,mapName,spawnPosition)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(idMap,mapName,spawnPosition):
  if(mapName):
    sql = "UPDATE Map SET mapName = %s WHERE idMap = %s"
    vals = (mapName,idMap)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(spawnPosition):
    sql = "UPDATE Map SET spawnPosition = %s WHERE idMap = %s"
    vals = (spawnPosition,idMap)
    mycursor.execute(sql,vals)
    mydb.commit()
    
def selectAll():
  mycursor.execute("SELECT * FROM Map")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def select(idMap):
  sql = "SELECT * FROM Map WHERE idMap = '%s'" %(idMap)
  mycursor.execute(sql)
  for i in mycursor:
    return i

def delete(idMap):
  sql = "DELETE FROM Map WHERE idMap = '%s'" %(idMap)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM Map")
  mydb.commit()





