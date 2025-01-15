DROP TABLE IF EXISTS in450a;
DROP TABLE IF EXISTS in450b;
DROP TABLE IF EXISTS in450c;

CREATE TABLE in450a(
Time DECIMAL,
Source VARCHAR(17),
Destination VARCHAR(17),
Protocol VARCHAR(10),
Length INTEGER,
Info TEXT
);

CREATE TABLE in450b(
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(100),
source VARCHAR(17),
destination VARCHAR(17)
);

CREATE TABLE in450c(
AppID VARCHAR(100),
AppName VARCHAR(100),
AppVersion VARCHAR(10),
source VARCHAR(17),
destination VARCHAR(17),    
DigSig VARCHAR(64)
);
