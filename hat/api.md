# Functions

1.Creating Functions

CREATE [OR REPLACE] FUNCTION function_name (arguments) 
RETURNS return_datatype AS $variable_name$
   DECLARE
      declaration;
      [...]
   BEGIN
      < function_body >
      [...]
      RETURN { variable_name | value }
   END; LANGUAGE plpgsql;

2.Calling the function

- select totalRecords();

# column defination

1.Writing a query to display column names:

select column_name,data_type,is_nullable from information_schema.columns where table_name='company';


2.Writing a function to return column names:

create or replace function col_def()
returns integer as $col$
declare 
col integer;
begin
select column_name,data_type,is_nullable from information_schema.columns where table_name='company';
return col;
end;
$def$ language plpgsql;

# Indexes

1.SELECT * FROM pg_indexes WHERE tablename = 'mytable';

2.Writing a function to return indexes:

create or replace function ind_def()
returns integer as $ind$
declare 
ind integer;
begin
SELECT * FROM pg_indexes WHERE tablename = 'company';
return ind;
end;
$def$ language plpgsql;

# Foreign key 

1.Creating first table:

CREATE TABLE COMPANY6(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);

2.Creating second table:

CREATE TABLE DEPARTMENT1(
   ID INT PRIMARY KEY      NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      references COMPANY6(ID)
);

These two tables are related to each other through reference from id column in COMPANY6.

3.Query to fetch foreign key from the table:

SELECT
    tc.table_schema, 
    tc.constraint_name, 
    tc.table_name, 
    kcu.column_name, 
    ccu.table_schema AS foreign_table_schema,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name 
FROM 
    information_schema.table_constraints AS tc 
    JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_schema = kcu.table_schema
    JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
    AND ccu.table_schema = tc.table_schema
WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name='mytable';

4.Fuction to fetch foreign key:

create or replace function fore_def()
returns integer as $fore$
declare 
fore integer;
begin
SELECT
    tc.table_schema, 
    tc.constraint_name, 
    tc.table_name, 
    kcu.column_name, 
    ccu.table_schema AS foreign_table_schema,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name 
FROM 
    information_schema.table_constraints AS tc 
    JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_schema = kcu.table_schema
    JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
    AND ccu.table_schema = tc.table_schema
WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name='dept';
return fore;
end;
$def$ language plpgsql;

# Reference table defination






