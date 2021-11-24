

# SQL

### JOIN

두개 이상의 테이블이나 데이터베이스를 연결하여 데이터를 검색하는 방법

[기본 SQL 구문]

```sql
SELECT *
FROM 기준테이블
[INNER/LEFT/RIGHT/OUTER] JOIN 붙일테이블 ON join_기준열
```

<BR/>

**[EXAMPLE]**

```tex
[TABLE A]							[TABLE B]
 ID  |  ANAME						 ID  |  BNAME
1    |   A1							1    |   B1
2    |   A2							2    |   B2
3    |   A3							4    |   B4
									5    |   B5
```



##### INNER JOIN

- 교집합 A ∩ B

- JOIN하려는 모든 테이블에 존재하는 데이터

- ```sql
  SELECT A.ID, A.ANAME, B.BNAME
  FROM A 
  INNER JOIN B ON A.ID = B.ID;
  ```

  ```tex
  1|A1|B1
  2|A2|B2
  ```

<BR/>

##### LEFT JOIN

- A - B

```sql
SELECT A.ID, A.ANAME, B.BNAME
FROM A 
LEFT OUTER JOIN B ON A.ID = B.ID;
```

```tex
1|A1|B1
2|A2|B2
3|A3|
```

<BR/>

##### RIGHT JOIN

- B - A

```sql
SELECT A.ID, A.ANAME, B.BNAME
FROM A 
RIGHT OUTER JOIN B ON A.ID = B.ID;
```

```tex
1|A1|B1
2|A2|B2
4|NULL|B4
5|NULL|B5
```

<BR/>

##### FULL OUTER JOIN

- 합집합 A ∪ B

```sql
SELECT A.ID, A.ANAME, B.BNAME
FROM A 
FULL OUTER JOIN B ON A.ID = B.ID;
```

```tex
1|A1|B1
2|A2|B2
3|A3|NULL
4|NULL|B4
5|NULL|B5
```

- 합집합 - 교집합   (A ∪ B) - (A ∩ B)

```sql
SELECT A.ID, A.ANAME, B.BNAME
FROM A 
FULL OUTER JOIN B ON A.ID = B.ID
WHERE A.ID IS NULL OR B.ID IS NULL;
```

```tex
3|A3|NULL
4|NULL|B4
5|NULL|B5
```

<BR/>

---------

##### References

https://mizykk.tistory.com/81