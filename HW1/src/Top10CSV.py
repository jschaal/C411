import copy
import csv


def top10CSV():
    connection = {"directory": "/home/joe/PycharmProjects/C411/HW1/Data",
                  "file_name": "Batting.csv"}

    fn = connection['directory'] + "/" + connection["file_name"]

    players = {}
    newStats = {"avg": 0, "AB": 0, "H": 0, "firstYear": 0, "lastYear": 0, "nameFirst": "", "nameLast": ""}

    with open(fn, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')

        for row in reader:
            playerID = row["playerID"]
            yearID = int(row["yearID"])
            if playerID in players.keys():
                current = players[playerID]
            else:
                current = copy.copy(newStats)

            current["AB"] += int(row["AB"])
            current["H"] += int(row["H"])
            if current["lastYear"] < yearID:
                current["lastYear"] = yearID

            if current["firstYear"] == 0:
                current["firstYear"] = yearID

            players[playerID] = current

    results = []
    for playerID in players.keys():
        current = players[playerID]
        if current["lastYear"] > 1960:
            if current["AB"] > 200:
                current["avg"] = current["H"] / current["AB"]
                stats = [playerID, current["avg"], current["H"], current["AB"], current["firstYear"],
                         current["lastYear"]]
                results.append(stats)

    sorted_by_avg = sorted(results, key=lambda tup: tup[1])
    top20 = list(reversed(sorted_by_avg[len(sorted_by_avg) - 10:]))

    connection = {"directory": "/home/joe/PycharmProjects/C411/HW1/Data",
                  "file_name": "People.csv"}

    fn = connection['directory'] + "/" + connection["file_name"]

    with open(fn, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')

        final_results = []
        for row in reader:
            playerID = row["playerID"]
            lastName = row["nameFirst"]
            firstName = row["nameLast"]

            for player in top20:
                if player[0] == playerID:
                    match = [playerID, firstName, lastName, player[1], player[2], player[3], player[4], player[5]]
                    final_results.append(match)
                    break

    sorted_by_avg = list(reversed(sorted(final_results, key=lambda tup: tup[4])))

    return sorted_by_avg


print(top10CSV())
