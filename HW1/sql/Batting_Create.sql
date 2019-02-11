USE `lahman2017`;

DROP TABLE`Batting`;

CREATE TABLE `Batting` (
  `playerID` varchar(9) DEFAULT NULL,
  `yearID` text,
  `stint` text,
  `teamID` text,
  `lgID` text,
  `G` text,
  `AB` text,
  `R` text,
  `H` text,
  `2B` text,
  `3B` text,
  `HR` text,
  `RBI` text,
  `SB` text,
  `CS` text,
  `BB` text,
  `SO` text,
  `IBB` text,
  `HBP` text,
  `SH` text,
  `SF` text,
  `GIDP` text,
  KEY `indPlayerID` (`playerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
