USE `lahman2017`;

DROP TABLE `People`;

CREATE TABLE `People` (
  `playerID` varchar(9) DEFAULT NULL,
  `birthYear` text,
  `birthMonth` text,
  `birthDay` text,
  `birthCountry` text,
  `birthState` text,
  `birthCity` text,
  `deathYear` text,
  `deathMonth` text,
  `deathDay` text,
  `deathCountry` text,
  `deathState` text,
  `deathCity` text,
  `nameFirst` text,
  `nameLast` text,
  `nameGiven` text,
  `weight` text,
  `height` text,
  `bats` text,
  `throws` text,
  `debut` text,
  `finalGame` text,
  `retroID` text,
  `bbrefID` text,
  KEY `indPlayerID` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
