USE `lahman2017`;
TRUNCATE `Batting`;
LOAD DATA LOCAL INFILE 
	'/home/joe/PycharmProjects/C411/HW1/Data/Batting.csv'
INTO TABLE `Batting`;

