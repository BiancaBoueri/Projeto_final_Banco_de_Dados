from logging.config import valid_ident
from dbConnection import mydb, mycursor

def parseNullInTuple(inTuple):
    for i in inTuple:
        if (i is None) or (i == ''):
            return True


def advancedSelect(choicesList, SQLnamesList, conditionalVar1, conditional1, conditionalVar2, conditional2, conditionalVar3):
    sql = ["SELECT "]
    firstElementFlag = True

    if (not any(choicesList) or all(choicesList)):
        sql.append("username, password, creationDate, localization, preferredLanguage, PIN, profilePicture")
    else:
        for i in range(len(choicesList)):
            if (choicesList[i]):
                if (not firstElementFlag):
                    sql.append(str(", "+SQLnamesList[i]))
                else:
                    sql.append(str(SQLnamesList[i]))
                    firstElementFlag = False

    sql.append(" FROM maplestory.account ")

    if (not parseNullInTuple(conditionalVar1)):
        sql.append("WHERE {} {} '{}'".format(conditionalVar1[0], conditionalVar1[1], conditionalVar1[2]))

    if (conditional1 is not None and not parseNullInTuple(conditionalVar2)):
        if (conditional2 is not None):
            sql.append(" {} ({} {} '{}'".format(conditional1, conditionalVar2[0], conditionalVar2[1], conditionalVar2[2]))
        else:
            sql.append(" {} {} {} '{}'".format(conditional1, conditionalVar2[0], conditionalVar2[1], conditionalVar2[2]))

    if (conditional2 is not None and not parseNullInTuple(conditionalVar3)):
        if (conditional1 is not None):
            sql.append(" {} {} {} '{}')".format(conditional2, conditionalVar3[0], conditionalVar3[1], conditionalVar3[2]))
        else:
            sql.append(" {} {} {} '{}'".format(conditional2, conditionalVar3[0], conditionalVar3[1], conditionalVar3[2]))
    sql.append(";")

    sql = ''.join(sql)
    mycursor.execute(sql)
    resultList = []
    for i in mycursor:
      resultList.append(i)
    return resultList
