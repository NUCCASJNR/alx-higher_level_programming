## 0x0E-SQL_more_queries

MORE SQL QUERIES

## Comments for your SQL file:

```bash
$ cat my_script.sq
````

```bash
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

## Install MySQL 8.0 on Ubuntu 20.04 LTS

```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
```
