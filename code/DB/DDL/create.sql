-- DDL (Data Definition Language)
-- 데이터베이스, 테이블을 정의하는 언어

-- 1. CREATE
CREATE DATABASE test_db;
DROP DATABASE test_db;

-- 인코딩 지정
CREATE DATABASE test_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


-- 인코딩 지정
CREATE DATABASE my_shop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE test_db;

CREATE TABLE user (
	user_id INT NOT NULL PRIMARy KEY AUTO_INCREMENT,
    user_name VARCHAR(10) NOT NULL,
    address VARCHAR(45),
    join_date DATE
);

SHOW TABLES;
DESC user;


CREATE TABLE customer (
	cust_id CHAR(10) NOT NULL PRIMARY KEY,
    cust_name VARCHAR(10) NOT NULL,
    address CHAR(10) NOT NULL,
    phone CHAR(11),
	birth DATE
);
DESC customer;