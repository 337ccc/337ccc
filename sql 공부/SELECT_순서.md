## 작성 순서

1. SELECT : 테이블의 데이터를 조회할 때 사용하는 구문
2. FROM
3. WHERE : 특정 조건을 만족하는 row들만 보여줌
4. GROUP BY
5. HAVING
6. ORDER BY
7. LIMIT

## 실행 순서

1. FROM: 어느 테이블을 대상으로 할 것인지를 먼저 결정합니다
2. WHERE: 해당 테이블에서 특정 조건(들)을 만족하는 row들만 선별합니다.
3. GROUP BY: row들을 그루핑 기준대로 그루핑합니다. 하나의 그룹은 하나의 row로 표현됩니다.
4. HAVING: 그루핑 작업 후 생성된 여러 그룹들 중에서, 특정 조건(들)을 만족하는 그룹들만 선별합니다.
5. SELECT: 모든 컬럼 또는 특정 컬럼들을 조회합니다. SELECT 절에서 컬럼 이름에 alias를 붙인 게 있다면, 이 이후 단계(ORDER BY, LIMIT)부터는 해당 alias를 사용할 수 있습니다.
6. ORDER BY: 각 row를 특정 기준에 따라서 정렬합니다.
7. LIMIT: 이전 단계까지 조회된 row들 중 일부 row들만을 추립니다.
