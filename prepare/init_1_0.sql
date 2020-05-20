-- MySQL Script generated by MySQL Workbench
-- Fri May  8 12:37:29 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema ProTJec
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `ProTJec` ;

-- -----------------------------------------------------
-- Schema ProTJec
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `ProTJec` DEFAULT CHARACTER SET utf8 ;
USE `ProTJec` ;

-- -----------------------------------------------------
-- Table `ProTJec`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ProTJec`.`users` ;

CREATE TABLE IF NOT EXISTS `ProTJec`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `usr_no` VARCHAR(7) NOT NULL,
  `usr_password` VARCHAR(32) NOT NULL,
  `usr_name` VARCHAR(30) NOT NULL,
  `usr_userlevel` INT NOT NULL,
  `usr_inst` VARCHAR(45) NOT NULL COMMENT 'institute of school',
  `usr_grade` INT NOT NULL DEFAULT 2018,
  `usr_avatar` VARCHAR(250) NOT NULL DEFAULT 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
  `usr_document` VARCHAR(250) NOT NULL DEFAULT '一个普通的 ProTJec 使用者',
  `usr_chat` VARCHAR(100) NOT NULL DEFAULT 'qq: 123456',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProTJec`.`projects`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ProTJec`.`projects` ;

CREATE TABLE IF NOT EXISTS `ProTJec`.`projects` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pro_name` VARCHAR(45) NOT NULL,
  `pro_sort` VARCHAR(45) NOT NULL,
  `pro_releaseTime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `pro_endTime` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `pro_need` INT NOT NULL,
  `pro_intro` TEXT NOT NULL,
  `pro_state` INT NOT NULL DEFAULT 0 COMMENT '0 表示正在审核，1 表示审核通过，2 表示审核失败，直接删除，3 表示不缺人了，也不删除，算是归档。',
  `pro_deleted` ENUM('Y', 'N') NOT NULL DEFAULT 'N',
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProTJec`.`usr_pro`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ProTJec`.`usr_pro` ;

CREATE TABLE IF NOT EXISTS `ProTJec`.`usr_pro` (
  `upr_role` ENUM('C', 'F') NOT NULL DEFAULT 'C' COMMENT 'C means captain, while F means followers.',
  `usr_id` INT NOT NULL,
  `pro_id` INT NOT NULL,
  INDEX `fk_response_users1_idx` (`usr_id` ASC) ,
  INDEX `fk_response_projects1_idx` (`pro_id` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProTJec`.`messages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ProTJec`.`messages` ;

CREATE TABLE IF NOT EXISTS `ProTJec`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `msg_content` TEXT NOT NULL,
  `msg_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `usr_from` INT NOT NULL,
  `usr_to` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_message_users1_idx` (`usr_from` ASC) ,
  INDEX `fk_message_users2_idx` (`usr_to` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProTJec`.`loginLogs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ProTJec`.`loginLogs` ;

CREATE TABLE IF NOT EXISTS `ProTJec`.`loginLogs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `lgi_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `usr_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_loginLogs_users1_idx` (`usr_id` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProTJec`.`tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ProTJec`.`tags` ;

CREATE TABLE IF NOT EXISTS `ProTJec`.`tags` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tag_name` VARCHAR(45) NOT NULL,
  `tag_cnt` INT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProTJec`.`pro_tag`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ProTJec`.`pro_tag` ;

CREATE TABLE IF NOT EXISTS `ProTJec`.`pro_tag` (
  `tag_id` INT NOT NULL,
  `pro_id` INT NOT NULL,
  INDEX `fk_pro_tag_tags1_idx` (`tag_id` ASC) ,
  INDEX `fk_pro_tag_projects1_idx` (`pro_id` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ProTJec`.`response`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `ProTJec`.`response` ;

CREATE TABLE IF NOT EXISTS `ProTJec`.`response` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `rsp_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `rsp_state` ENUM('P', 'F', 'W') NOT NULL DEFAULT 'W' COMMENT 'P means pass, N means fail, while W means waiting for judge',
  `usr_id` INT NOT NULL,
  `pro_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_response_projects2_idx` (`pro_id` ASC) ,
  INDEX `fk_response_users2_idx` (`usr_id` ASC) )
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `ProTJec`.`users`
-- -----------------------------------------------------
START TRANSACTION;
USE `ProTJec`;
INSERT INTO `ProTJec`.`users` (`id`, `usr_no`, `usr_password`, `usr_name`, `usr_userlevel`, `usr_inst`, `usr_grade`, `usr_avatar`, `usr_document`, `usr_chat`) VALUES (1, '1852409', '123456', 'skyleaworlder', 0, '电信学院', 2018, DEFAULT, DEFAULT, 'qq: 123456');
INSERT INTO `ProTJec`.`users` (`id`, `usr_no`, `usr_password`, `usr_name`, `usr_userlevel`, `usr_inst`, `usr_grade`, `usr_avatar`, `usr_document`, `usr_chat`) VALUES (2, '1850001', '456789', 'wei', 1, '经管学院', 2018, DEFAULT, DEFAULT, 'qq: 321546');
INSERT INTO `ProTJec`.`users` (`id`, `usr_no`, `usr_password`, `usr_name`, `usr_userlevel`, `usr_inst`, `usr_grade`, `usr_avatar`, `usr_document`, `usr_chat`) VALUES (3, '1951135', 'ljgsb!', 'trick_beta', 1, '医学院', 2019, DEFAULT, DEFAULT, 'qq: 325148');

COMMIT;


-- -----------------------------------------------------
-- Data for table `ProTJec`.`projects`
-- -----------------------------------------------------
START TRANSACTION;
USE `ProTJec`;
INSERT INTO `ProTJec`.`projects` (`id`, `pro_name`, `pro_sort`, `pro_releaseTime`, `pro_endTime`, `pro_need`, `pro_intro`, `pro_state`, `pro_deleted`) VALUES (1, 'proTJec', '理工', '2020-04-21 22:18:36', '2020-12-31 12:31:31', 3, '只是来显摆一下', DEFAULT, DEFAULT);
INSERT INTO `ProTJec`.`projects` (`id`, `pro_name`, `pro_sort`, `pro_releaseTime`, `pro_endTime`, `pro_need`, `pro_intro`, `pro_state`, `pro_deleted`) VALUES (2, 'ljg_OVE', '文史', '2020-05-01 10:03:01', '2020-11-30 12:59:59', 1, '那个人就是……', DEFAULT, DEFAULT);
INSERT INTO `ProTJec`.`projects` (`id`, `pro_name`, `pro_sort`, `pro_releaseTime`, `pro_endTime`, `pro_need`, `pro_intro`, `pro_state`, `pro_deleted`) VALUES (3, 'WTF', '社科', '2020-05-02 09:12:18', '2021-01-31 23:50:59', 2, '越强越好', DEFAULT, DEFAULT);

COMMIT;


-- -----------------------------------------------------
-- Data for table `ProTJec`.`usr_pro`
-- -----------------------------------------------------
START TRANSACTION;
USE `ProTJec`;
INSERT INTO `ProTJec`.`usr_pro` (`upr_role`, `usr_id`, `pro_id`) VALUES ('C', 1, 1);
INSERT INTO `ProTJec`.`usr_pro` (`upr_role`, `usr_id`, `pro_id`) VALUES ('C', 2, 3);
INSERT INTO `ProTJec`.`usr_pro` (`upr_role`, `usr_id`, `pro_id`) VALUES ('F', 2, 1);
INSERT INTO `ProTJec`.`usr_pro` (`upr_role`, `usr_id`, `pro_id`) VALUES ('C', 3, 2);
INSERT INTO `ProTJec`.`usr_pro` (`upr_role`, `usr_id`, `pro_id`) VALUES ('F', 3, 3);

COMMIT;


-- -----------------------------------------------------
-- Data for table `ProTJec`.`messages`
-- -----------------------------------------------------
START TRANSACTION;
USE `ProTJec`;
INSERT INTO `ProTJec`.`messages` (`id`, `msg_content`, `msg_time`, `usr_from`, `usr_to`) VALUES (1, '厉害啊，我想试试', DEFAULT, 1, 3);
INSERT INTO `ProTJec`.`messages` (`id`, `msg_content`, `msg_time`, `usr_from`, `usr_to`) VALUES (2, 'i love you', DEFAULT, 2, 3);
INSERT INTO `ProTJec`.`messages` (`id`, `msg_content`, `msg_time`, `usr_from`, `usr_to`) VALUES (3, 'so da yo', DEFAULT, 3, 1);

COMMIT;


-- -----------------------------------------------------
-- Data for table `ProTJec`.`tags`
-- -----------------------------------------------------
START TRANSACTION;
USE `ProTJec`;
INSERT INTO `ProTJec`.`tags` (`id`, `tag_name`, `tag_cnt`) VALUES (1, 'lovelive', 2);
INSERT INTO `ProTJec`.`tags` (`id`, `tag_name`, `tag_cnt`) VALUES (2, 'hehe', 1);
INSERT INTO `ProTJec`.`tags` (`id`, `tag_name`, `tag_cnt`) VALUES (3, '建模', 0);

COMMIT;


-- -----------------------------------------------------
-- Data for table `ProTJec`.`pro_tag`
-- -----------------------------------------------------
START TRANSACTION;
USE `ProTJec`;
INSERT INTO `ProTJec`.`pro_tag` (`tag_id`, `pro_id`) VALUES (1, 1);
INSERT INTO `ProTJec`.`pro_tag` (`tag_id`, `pro_id`) VALUES (2, 1);
INSERT INTO `ProTJec`.`pro_tag` (`tag_id`, `pro_id`) VALUES (3, 2);

COMMIT;

