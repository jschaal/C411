ALTER TABLE `lahman2017`.`Batting` 
CHANGE COLUMN `playerID` `playerID` VARCHAR(9) NULL DEFAULT NULL ,
ADD INDEX `indPlayerID` (`playerID` ASC);

ALTER TABLE `lahman2017`.`People2` 
CHANGE COLUMN `playerID` `playerID` VARCHAR(9) NULL DEFAULT NULL ,
ADD INDEX `indPlayerID` (`playerID` ASC);

ALTER TABLE `lahman2017`.`Appearances` 
CHANGE COLUMN `playerID` `playerID` VARCHAR(9) NULL DEFAULT NULL ,
ADD INDEX `indPlayerID` (`playerID` ASC);