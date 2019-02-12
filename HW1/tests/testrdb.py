from RDBDataTable import RDBDataTable
import json

def test1():
    t=RDBDataTable("People",['playerID'])
    print(t)

def test2():
    t=RDBDataTable("People",['playerID'], debug=True)
    #print(t)

    tmp = { "nameLast": "Williams","nameFirst": "Ted" }

    result = t._template_to_where_clause(tmp)
    print("WC = ", str(result))

    q = "select * from People " + result[0]
    print("Query = ", q)

    result = t._run_q(cnx=None,q=q,args=result[1],commit=True, fetch=True)
    print("Query result = ", json.dumps(result, indent=2, default=str))



def test3():
    t= RDBDataTable("People",['platerID'],debug=True)

    tmp = { "nameLast": "Willliams", "nameFirst": "Ted" }
    result = t.find_by_template(tmp, field_list=['playerID','nameLast', 'throws'])

    print("Result = ", result)


def test4():
    t = RDBDataTable("People", ['playerID'], debug=True)
    # print(t)

    tmp = {"nameLast": "Williams", "nameFirst": "Ted" }

    #column that doesn't exist
    result = t.find_by_template(tmp, field_list=['playerID', 'nameLast', 'color'])

    print("Result = ", result)

def test5():
    t = RDBDataTable("People", key_columns=None, debug=True)
    # print(t)

    result = t.find_by_primary_key(['willite01'], field_list=['playerID', 'nameLast', 'throws'])

    print("Result = ", result)

    #AttributeError: 'tuple' object has no attribute '_rows'

def test52():
    t= RDBDataTable("Teams", key_columns=None, debug=True)

    result=t.find_by_primary_key(['BOS','2004'], field_list=['teamID','yearID','Rank','W', 'WSWin'])

    print("Result = ", result)


def test6():
    t = RDBDataTable("Batting", key_columns=None, debug=True)
    # print(t)

    result = t._get_primary_key()

    print("Result = ", json.dumps(result, indent=2))

def test7():
    t = RDBDataTable("People", key_columns=None, debug=True)
    # print(t)

    new_PERSON = {
        "playerID": "dff201:",
        "nameLast": "Ferguson",
        "throws": "R"
    }
    result = t.insert(new_person)

    print("Result = ", json.dumps(result, indent=2))

def test8():
    t=RDBDataTable("People", key_columns=None, debug=True)

    new_person = {
        "playerID": "dff201",
        "nameLast": "Ferguson",
        "throws":"R"
    }

    print("Result = ", json.dumps(result,indent=2))

    tmp={'plyaerID':'dff201'}
    r1=t.find_by_template(tmp)
    print("After insert, Q returns ", r1)

    result = t.delete_by_template({'plyaerID':'dff201'})

    r1=t.find_by_template(tmp)
    print("After delete, Q returns ", result)

def test82():
    t=RDBDataTable("People", key_columns=None, debug=True)

    new_person = {
        "playerID": "dff201",
        "nameLast": "Ferguson",
        "throws":"R"
    }

    result = t.insert(new_person)

    print("Result = ", json.dumps(result, indent=2))



    tmp={'playerID':'dff201'}

    new_c = {
        "nameFirst": "donald",
        "bats": "R"
    }

    r1=t.update_by_template(tmp, new_c)
    print("\n\nAfter update, Q returns " , r1)

def testTop10():

    #print(t)


    q = "SELECT Batting.playerID, " + \
        "(SELECT People.nameFirst FROM People WHERE People.playerID=Batting.playerID) as first_name, " + \
        "(SELECT People.nameLast FROM People WHERE People.playerID=Batting.playerID) as last_name, " + \
        "sum(Batting.H) /sum(Batting.AB) as career_average, " + \
        "sum(Batting.H) as career_hits, sum(Batting.AB) as career_at_bats , min(Batting.yearID) as first_year, " + \
        "max(Batting.yearID) as last_year " + \
        "FROM Batting GROUP BY playerId HAVING career_at_bats > 200 AND last_year >1960  " + \
        "ORDER BY career_average DESC LIMIT 10"

    print("Query = ", q)

    t=RDBDataTable("People",['playerID'], debug=True)

    result = t._run_q(q=q)
    print("Query result = ", json.dumps(result, indent=2, default=str))


testTop10()
