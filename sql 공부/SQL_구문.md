## 데이터 조회

- SELECT : 테이블의 데이터를 조회할 때 사용하는 구문
- \*(asterisk) : 모든 값을 조회함(모든 컬럼)
- WHERE : 특정 조건을 만족하는 row들만 보여줌

```
SELECT * FROM copang_main.member WHERE email = 'taehos@hanmail.net';
```

- BETWEEN ~ AND
  - 날짜에도 사용 가능

```
SELECT * FROM member WHERE age BETWEEN 30 and 39;
SELECT * FROM member WHERE age NOT BETWEEN 30 and 39;
SELECT * FROM member WHERE sign_up_day BETWEEN '2018-01-01' and '2018-12-31';
```

- LIKE

```
SELECT * FROM member WHERE address LIKE '서울%'
# 서울% : 서울로 시작하는 모든 문자열(서울시, 서울 중구, 서울특별시 등)
# %고양시% : 고양시가 포함된 모든 문자열
```

- IN

```
SELECT * FROM member WHERE age IN (20, 30);
# age가 딱 20세, 30세인 회원만
```

- \_(언더바) : 한 글자만 나타냄

```
c_____(언더바 5개) : cowboy, codeit
```

### 날짜

- 연도, 월, 일 추출

```
SELECT * FROM member WHERE YEAR(birthday) = '1992';
SELECT * FROM member WHERE MONTH(birthday) IN (6, 7, 8);
SELECT * FROM member WHERE DAYOFMONTH(sign_up_day) BETWEEN 15 and 31;
```

- DATEDIFF(날짜 1, 날짜 2) : 날짜 1 - 날짜 2(날짜 간 차이)

```
SELECT email, sign_up_day, CURDATE(), DATEDIFF(CURDATE(), sign_up_day) FROM member;
# CURDATE() : 오늘 날짜를 구하는 함수
# 오늘을 기준으로 며칠 이전인지
```

- DATE_ADD(날짜, INTERVAL 300 DAY) : 날짜 기준으로 300일 이후의 날짜
- DATE_SUB(날짜, INTERVAL 250 DAY) : 날짜 기준으로 250일 이전의 날짜

```
SELECT email, sign_up_day, DATE_SUB(sign_up_day, INTERVAL 250 DAY) FROM member;
```

- UNIX_TIMESTAMP(sign_up_day) : 1970년 1월 1일을 기준으로, sign_up_day까지 총 몇 초가 지났는지
- FROM_UNIXTIME(UNIX_TIMESTAMP(sign_up_day)) : 날짜와 시간 형식으로 보여줌

### 여러 개의 조건 걸기

- AND가 OR보다 우선 순위가 더 높음

```
SELECT * FROM member
WHERE gender = 'm'
  AND address LIKE '서울%'
  AND age BETWEEN 25 and 29;

SELECT * FROM member
WHERE MONTH(sign_up_day) BETWEEN 3 and 5
  OR MONTH(sign_up_day) BETWEEN 9 and 11;

SELECT * FROM member
WHERE (gender = 'm' AND height >= 180)
  OR (gender = 'f' AND height >= 170);
```
