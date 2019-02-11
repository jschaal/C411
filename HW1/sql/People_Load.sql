USE `lahman2017`;
TRUNCATE `People`;
LOAD DATA LOCAL INFILE 
	'/home/joe/PycharmProjects/C411/HW1/Data/People.csv'
INTO TABLE `People`;

