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

select *
from table_name
where false;


2.Writing a function to return column names:

create or replace function show_columns()
returns integer as $total$
declare total integer;
begin select * from company where false;
return total;

# Indexes

1.REATE INDEX index_name
ON table_name (column_name);

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






