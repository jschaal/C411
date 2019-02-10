# 02/10/19 09:20 AM

from CSVDataTable import CSVDataTable


def test0():
    testCount = 0
    testPass = 0

    #   test table load
    testCount += 1
    t1 = CSVDataTable("People",
                      connect_info={
                          #                          "directory": "/Users/Sophie/Documents/Databases/HW1/Data",
                          "directory": "/home/joe/PycharmProjects/C411/HW1/Data",
                          "file_name": "People.csv"
                      }, key_columns=['playerID'], debug=True)

    print(testCount, ": Test Table Creation")
    print(t1)
    print("")
    testPass += 1

    #   test find by template
    testCount += 1
    print(testCount, ": Test Find by Template")
    template = {"nameLast": "Williams"}
    r = t1.find_by_template(template)
    print("Table = ", r)
    print("")
    testPass += 1

    #   test field_list limitation
    testCount += 1
    print(testCount, ": Test Find by Template with Selected Fields")
    field_list = ['playerID', 'nameFirst', 'nameLast', 'birthYear']
    r = t1.find_by_template(template, field_list)
    print(r)
    print("")
    testPass += 1

    #   test find by primary key
    testCount += 1
    print(testCount, ": Test Find by Primarmy Key")
    keys = ['willial02']
    r = t1.find_by_primary_key(keys, field_list)
    print(r)
    print("")
    testPass += 1

    #   test rejected insert of existing primary key
    testCount += 1
    print(testCount, ": Test Rejection of Insert of a record with an existing Primarmy Key")
    rec = {'playerID': 'willial02', 'nameFirst': 'Al', 'nameLast': 'Williams', 'birthYear': '1914'}
    try:
        t1.insert(rec)
    except ValueError as e:
        print("Insert Error Caught:", e)
        print("")
        testPass += 1

    # test insert of a record with non existant primary key
    testCount += 1
    print(testCount, ": Test Insert of a record with non-existant Primarmy Key")
    keys = ['willial99']
    rec = {'playerID': 'willial99', 'nameFirst': 'Al', 'nameLast': 'Williams', 'birthYear': '1914'}
    t1.insert(rec)
    r = t1.find_by_primary_key(keys, field_list)
    print("Record added", r)
    print("")
    testPass += 1

    # test deleting of a record by template by first showing it is there, deleting it, and then inserting it again
    testCount += 1
    print(testCount, ": Test Deleting records from Template")
    # verify that record to delete exists
    r = t1.find_by_template(template, field_list)
    print("Pre-Delete Records Found", len(r))
    deletedRecs = t1.delete_by_template(template)
    print("Records deleted", deletedRecs)
    r = t1.find_by_template(template, field_list)
    print("Post Delete Records Found", len(r))
    print("")
    testPass += 1

    # test updating of that results in a duplicate key
    testCount += 1
    print(testCount, ": Test Updating Records resulting in Duplicate Key")
    rec = {'playerID': 'willial99', 'nameFirst': 'Al', 'nameLast': 'Williams', 'birthYear': '1914'}
    t1.insert(rec)
    rec = {'playerID': 'willial02', 'nameFirst': 'Al', 'nameLast': 'Williams', 'birthYear': '1914'}
    t1.insert(rec)
    new_values = {'playerID': 'willial02'}
    template = {"nameLast": "Williams"}
    try:
        updateCount = t1.update_by_template(template, new_values)
    except ValueError as e:
        print("Update Error Caught:", e)
        print("")
        testPass += 1

    # test updating of that results that do not effect primarmy keys
    testCount += 1
    print(testCount, ": Test Updating Records that do not resulting in Duplicate Keys")
    template = {"nameLast": "Williams"}
    new_values = {'nameLast': 'Slytheren'}
    updateCount = t1.update_by_template(template, new_values)
    print("Records Updated:", updateCount)
    template = {"nameLast": "Slytheren"}
    r = t1.find_by_template(template, field_list)
    print("New Records Found", len(r))
    print(r)
    print("")
    testPass += 1

    # test update by primamry key
    testCount += 1
    print(testCount, ": Test Update of Primary Key")
    key_fields = ['aaronto01']
    r = t1.find_by_primary_key(key_fields, field_list)
    print("Before Update", r)
    new_values = {'nameFirst': 'Salazar', 'nameLast': 'Slytheren'}
    updateCount = t1.update_by_key(key_fields, new_values)
    print("Records Updated", updateCount)
    r = t1.find_by_primary_key(key_fields, field_list)
    print("After Update", r)
    print("")
    testPass += 1
    print("")

    if testCount != testPass:
        raise Exception("Tests Failed!.  Expected {}.  Completedd {}".format(testCount, testPass))
    else:
        print("All Tests Succssful")
        print("")


def test1():
    testCount = 0
    testPass = 0

    #   test table load
    testCount += 1
    t1 = CSVDataTable("BattingSmall",
                      connect_info={
                          #                          "directory": "/Users/Sophie/Documents/Databases/HW1/Data",
                          "directory": "/home/joe/PycharmProjects/C411/HW1/Data",
                          "file_name": "BattingSmall.csv"
                      }, key_columns=['playerID', 'yearID', 'stint'], debug=True)

    print(testCount, ": Test Table Creation")
    print(t1)
    print("")
    testPass += 1

    #   test find by template
    testCount += 1
    print(testCount, ": Test Find by Template")
    template = {'yearID': '1871', 'teamID': 'TRO'}
    r = t1.find_by_template(template)
    print("Table = ", r)
    print("")
    testPass += 1

    #   test field_list limitation
    testCount += 1
    print(testCount, ": Test Find by Template with Selected Fields")
    field_list = ['playerID', 'yearID', 'stint', 'teamID', 'lgID']
    r = t1.find_by_template(template, field_list)
    print(r)
    print("")
    testPass += 1

    #   test find by primary key
    testCount += 1
    print(testCount, ": Test Find by Primarmy Key")
    keys = ['allisar01', '1871', '1']
    r = t1.find_by_primary_key(keys, field_list)
    print(r)
    print("")
    testPass += 1

    #   test rejected insert of existing primary key
    testCount += 1
    print(testCount, ": Test Rejection of Insert of a record with an existing Primarmy Key")
    rec = {'playerID': 'allisar01', 'yearID': '1871', 'stint': '1', 'teamID': 'CL1', 'lgID': 'NA'}
    try:
        t1.insert(rec)
    except ValueError as e:
        print("Insert Error Caught:", e)
        print("")
        testPass += 1

    # test insert of a record with non existant primary key
    testCount += 1
    print(testCount, ": Test Insert of a record with non-existant Primarmy Key")
    rec = {'playerID': 'allisar01', 'yearID': '1871', 'stint': '2', 'teamID': 'TR0', 'lgID': 'NA'}
    t1.insert(rec)
    keys = ['allisar01', '1871', '2']
    r = t1.find_by_primary_key(keys, field_list)
    print("Record added", r)
    print("")
    testPass += 1

    # test deleting of a record by template by first showing it is there, deleting it, and then inserting it again
    testCount += 1
    print(testCount, ": Test Deleting records from Template")
    # verify that record to delete exists
    r = t1.find_by_template(template, field_list)
    print("Pre-Delete Records Found", len(r))
    deletedRecs = t1.delete_by_template(template)
    print("Records deleted", deletedRecs)
    r = t1.find_by_template(template, field_list)
    print("Post Delete Records Found", len(r))
    print("")
    testPass += 1

    # test updating of that results in a duplicate key
    testCount += 1
    print(testCount, ": Test Updating Records resulting in Duplicate Key")
    rec = {'playerID': 'allisar01', 'yearID': '1871', 'stint': '3', 'teamID': 'TRO', 'lgID': 'NA'}
    t1.insert(rec)
    rec = {'playerID': 'allisar01', 'yearID': '1871', 'stint': '4', 'teamID': 'TRO', 'lgID': 'NA'}
    t1.insert(rec)
    new_values = {'stint': '1'}
    template = {'yearID': '1871', 'teamID': 'TRO'}
    try:
        updateCount = t1.update_by_template(template, new_values)
    except ValueError as e:
        print("Update Error Caught:", e)
        print("")
        testPass += 1

    # test updating of that results that do not effect primarmy keys
    testCount += 1
    print(testCount, ": Test Updating Records that do not resulting in Duplicate Keys")
    template = {'yearID': '1871', 'teamID': 'TRO'}
    new_values = {'lgID': 'SS', 'teamID': 'NY1'}
    r = t1.find_by_template(template, field_list)
    print("Before Update", r)
    updateCount = t1.update_by_template(template, new_values)
    print("Records Updated:", updateCount)
    template = {'yearID': '1871', 'teamID': 'NY1'}
    r = t1.find_by_template(template, field_list)
    print("New Records Found", len(r))
    print(r)
    print("")
    testPass += 1

    # test update by primamry key
    testCount += 1
    print(testCount, ": Test Update of Primary Key")
    key_fields = ['allisar01', '1871', '2']
    r = t1.find_by_primary_key(key_fields, field_list)
    print("Before Update", r)
    new_values = {'lgID': 'SS', 'teamID': 'NY1'}
    updateCount = t1.update_by_key(key_fields, new_values)
    print("Records Updated", updateCount)
    r = t1.find_by_primary_key(key_fields, field_list)
    print("After Update", r)
    print("")
    testPass += 1
    print("")

    if testCount != testPass:
        raise Exception("Tests Failed!.  Expected {}.  Completedd {}".format(testCount, testPass))
    else:
        print("All Tests Succssful")
        print("")


def test2():
    testCount = 0
    testPass = 0

    #   test table load
    testCount += 1
    t1 = CSVDataTable("People",
                      connect_info={
                          #                          "directory": "/Users/Sophie/Documents/Databases/HW1/Data",
                          "directory": "/home/joe/PycharmProjects/C411/HW1/Data",
                          "file_name": "PeopleSmall.csv"
                      }, key_columns=['playerID'], debug=True)

    print(testCount, ": Test Table Creation")
    print(t1)
    print("")
    testPass += 1

    #   test find by template
    testCount += 1
    print(testCount, ": Test Find by Template")
    template = {"birthCity": "Mobile"}
    r = t1.find_by_template(template)
    print("Table = ", r)
    print("")
    testPass += 1

    #   test field_list limitation
    testCount += 1
    print(testCount, ": Test Find by Template with Selected Fields")
    field_list = ['playerID', 'nameFirst', 'nameLast', 'birthYear']
    r = t1.find_by_template(template, field_list)
    print(r)
    print("")
    testPass += 1

    #   test find by primary key
    testCount += 1
    print(testCount, ": Test Find by Primarmy Key")
    keys = ['aaronto01']
    r = t1.find_by_primary_key(keys, field_list)
    print(r)
    print("")
    testPass += 1

    #   test rejected insert of existing primary key
    testCount += 1
    print(testCount, ": Test Rejection of Insert of a record with an existing Primarmy Key")
    rec = {'playerID': 'aaronha01', 'nameFirst': 'Hank', 'nameLast': 'Aaron', 'birthYear': '1934'}
    try:
        t1.insert(rec)
    except ValueError as e:
        print("Insert Error Caught:", e)
        print("")
        testPass += 1

    # test insert of a record with non existant primary key
    testCount += 1
    print(testCount, ": Test Insert of a record with non-existant Primarmy Key")
    keys = ['willial99']
    rec = {'playerID': 'willial99', 'nameFirst': 'Al', 'nameLast': 'Williams', 'birthYear': '1914'}
    t1.insert(rec)
    r = t1.find_by_primary_key(keys, field_list)
    print("Record added", r)
    print("")
    testPass += 1

    # test deleting of a record by template by first showing it is there, deleting it, and then inserting it again
    testCount += 1
    print(testCount, ": Test Deleting records from Template")
    # verify that record to delete exists
    r = t1.find_by_template(template, field_list)
    print("Pre-Delete Records Found", len(r))
    deletedRecs = t1.delete_by_template(template)
    print("Records deleted", deletedRecs)
    r = t1.find_by_template(template, field_list)
    print("Post Delete Records Found", len(r))
    print("")
    testPass += 1

    # test updating of that results in a duplicate key
    testCount += 1
    print(testCount, ": Test Updating Records resulting in Duplicate Key")
    rec = {'playerID': 'willial77', 'nameFirst': 'Al', 'nameLast': 'Williams', 'birthYear': '1914'}
    t1.insert(rec)
    rec = {'playerID': 'willial02', 'nameFirst': 'Al', 'nameLast': 'Williams', 'birthYear': '1914'}
    t1.insert(rec)
    new_values = {'playerID': 'willial02'}
    template = {"nameLast": "Williams"}
    try:
        updateCount = t1.update_by_template(template, new_values)
    except ValueError as e:
        print("Update Error Caught:", e)
        print("")
        testPass += 1

    # test updating of that results that do not effect primarmy keys
    testCount += 1
    print(testCount, ": Test Updating Records that do not resulting in Duplicate Keys")
    template = {"nameLast": "Williams"}
    new_values = {'nameLast': 'Smith'}
    updateCount = t1.update_by_template(template, new_values)
    print("Records Updated:", updateCount)
    template = {"nameLast": "Smith"}
    r = t1.find_by_template(template, field_list)
    print("New Records Found: {}", len(r))
    print(r)
    testPass += 1

    if testCount != testPass:
        raise Exception("Tests Failed!.  Expected {}.  Completedd {}".format(testCount, testPass))
    else:
        print("All Tests Succssful")


test0()
test1()
test2()
