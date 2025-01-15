-- Import data into in450a
\copy in450a (Time, source, destination, protocol, length, info) FROM '~/database-application/data/IN450A.csv' DELIMITER ',' CSV HEADER;

-- Import data into in450b
\copy in450b (first_name, last_name, email, source, destination) FROM '~/database-application/data/IN450B.csv' DELIMITER ',' CSV HEADER;

-- Import data into in450c
\copy in450c (AppID, AppName, AppVersion, source, destination, DigSig) FROM '~/database-application/data/IN450C.csv' DELIMITER ',' CSV HEADER;

CREATE ROLE IN450a 
LOGIN 
PASSWORD 'D3fault_p@ssw0rd1';

CREATE ROLE IN450b 
LOGIN 
PASSWORD 'D3fault_p@ssw0rd2';

CREATE ROLE IN450c
LOGIN
PASSWORD 'D3fault_p@ssw0rd3';

GRANT SELECT
ON in450a, in450b, in450c
TO IN450a;

GRANT SELECT
ON in450b
TO IN450b;

GRANT SELECT
ON in450c
TO IN450c;