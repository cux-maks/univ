DROP DATABASE `MyCocktail`;
CREATE DATABASE `MyCocktail`;

USE `MyCocktail`;

CREATE TABLE `Default_Board`(
	`board_id` INT AUTO_INCREMENT,
	`title` VARCHAR(50),
    `recipe_id` INT,
    `member_id` VARCHAR(20),
    `write_time` DATETIME NOT NULL,
    `img_url` VARCHAR(255),
    `text` VARCHAR(4096) NOT NULL,
    `good_cnt` INT DEFAULT 0,
    `snack` VARCHAR(255),
    `tool` VARCHAR(1024),
    PRIMARY KEY(`board_id`),
    FOREIGN KEY(`member_id`) REFERENCES `member`(`member_id`),
    FOREIGN KEY(`recipe_id`) REFERENCES `Recipe`(`recipe_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `Recipe`(
	`recipe_id` VARCHAR(50) NOT NULL,
    `ingredient` VARCHAR(255) NOT NULL,
    `ratio` FLOAT NOT NULL,
    PRIMARY KEY(`recipe_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `Default_Board_Comment`(
	`comment_id` INT AUTO_INCREMENT,
    `text` VARCHAR(2048) NOT NULL,
    `member_id` VARCHAR(20) NOT NULL,
    `datetime` DATETIME,
    `good_cnt` INT DEFAULT 0,
    `board_id` INT,
    PRIMARY KEY(`comment_id`),
    FOREIGN KEY(`member_id`) REFERENCES `member`(`member_id`),
    FOREIGN KEY(`board_id`) REFERENCES `Default_Board`(`board_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `My_Board`(
	`board_id` INT AUTO_INCREMENT,
	`title` VARCHAR(50),
    `recipe_id` INT,
    `member_id` VARCHAR(20),
    `write_time` DATETIME NOT NULL,
    `img_url` VARCHAR(255),
    `text` VARCHAR(4096) NOT NULL,
    `good_cnt` INT DEFAULT 0,
    `snack` VARCHAR(255),
    `tool` VARCHAR(1024),
    PRIMARY KEY(`board_id`),
    FOREIGN KEY(`member_id`) REFERENCES `member`(`member_id`),
    FOREIGN KEY(`recipe_id`) REFERENCES `Recipe`(`recipe_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `My_Board_Comment`(
	`comment_id` INT AUTO_INCREMENT,
    `text` VARCHAR(2048) NOT NULL,
    `member_id` VARCHAR(20) NOT NULL,
    `datetime` DATETIME,
    `good_cnt` INT DEFAULT 0,
    `board_id` INT,
    PRIMARY KEY(`comment_id`),
    FOREIGN KEY(`member_id`) REFERENCES `member`(`member_id`),
    FOREIGN KEY(`board_id`) REFERENCES `My_Board`(`board_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `member`(
	`member_name` VARCHAR(10) NOT NULL,
    `tel` VARCHAR(20) UNIQUE,
    `member_id` VARCHAR(20),
    `passwd` VARCHAR(1024) NOT NULL,
    `birth` DATE NOT NULL,
    `email` VARCHAR(50) UNIQUE,
    PRIMARY KEY(`member_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `snack`(
	`snack_id` INT,
    `snack_name` VARCHAR(255) NOT NULL,
    `recipe_id` VARCHAR(50),
    PRIMARY KEY(`snack_id`),
    FOREIGN KEY(`recipe_id`) REFERENCES `recipe`(`recipe_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `liquor`(
	`liquor_id` INT AUTO_INCREMENT,
    `liquor_name` VARCHAR(255) NOT NULL,
    `price` INT NOT NULL,
    PRIMARY KEY(`liquor_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `garnish`(
	`garnish_id` INT AUTO_INCREMENT,
    `garnish_name` VARCHAR(255) NOT NULL,
    `price` INT NOT NULL,
    PRIMARY KEY(`garnish_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `beveridge`(
	`beveridge_id` INT AUTO_INCREMENT,
    `beveridge_name` VARCHAR(255) NOT NULL,
    `price` INT NOT NULL,
    PRIMARY KEY(`beveridge_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `syrup`(
	`syrup_id` INT AUTO_INCREMENT,
    `syrup_name` VARCHAR(255) NOT NULL,
    `price` INT NOT NULL,
    PRIMARY KEY(`syrup_id`)
) ENGINE = MyISAM CHARSET = utf8;

CREATE TABLE `tools`(
	`tool_id` INT AUTO_INCREMENT,
    `tool_name` VARCHAR(255) NOT NULL,
    `price` INT NOT NULL,
    PRIMARY KEY(`tool_id`)
) ENGINE = MyISAM CHARSET = utf8;