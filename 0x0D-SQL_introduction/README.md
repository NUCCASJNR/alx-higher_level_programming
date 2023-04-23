## 0x0D-SQL_introduction

## Comments for your SQL file

```bash
cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;

```

## Install MySQL 8.0 on Ubuntu 20.04 LTS

```bash
sudo apt update

```

```bash
sudo apt install mysql-server

```

```bash
mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))

```

## RECOMMENDED MATERIALS

[MYSQL TUTORIAL](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

[tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

[ddl and dml](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/ddldml.php)

[queries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/queries.php)

[techniques](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/functions.php)

[sub-queries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)

[backtick and apostrophe](https://stackoverflow.com/questions/29402361/what-makes-the-big-difference-between-a-backtick-and-an-apostrophe/29402458)

[cheat sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)

[syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

[installing](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)
