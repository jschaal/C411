SELECT Batting.playerID,  
(SELECT People.nameFirst FROM People WHERE People.playerID=Batting.playerID) as first_name,
(SELECT People.nameLast FROM People WHERE People.playerID=Batting.playerID) as last_name, 
sum(Batting.H) /sum(Batting.AB) as career_average, 
sum(Batting.H) as career_hits, 
sum(Batting.AB) as career_at_bats , 
min(Batting.yearID) as first_year, 
max(Batting.yearID) as last_year 
FROM Batting 
GROUP BY playerId
HAVING career_at_bats > 200 AND last_year >1960  ORDER BY 
career_average DESC 
LIMIT 10;
