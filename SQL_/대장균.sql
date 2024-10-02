-- 메모리 상의 가상의 테이블 저장
-- 최초에 기준이 되는 쿼리 필요
-- 반복하려는 쿼리르 union으로 붙임
-- 반복쿼리가 종료되는 조건
-- 반복되어 생성된 가상의 테이블 사용

WITH RECURSIVE GEN_DATA AS (
    SELECT
        ID,
        PARENT_ID,
        1 AS GEN
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    UNION ALL
    SELECT
        E.ID,
        E.PARENT_ID,
        (GEN+1) AS GEN
    FROM ECOLI_DATA E
    INNER JOIN GEN_DATA G ON E.PARENT_ID = G.ID
)
SELECT ID FROM GEN_DATA ORDER BY ID

SELECT AA.ID
  FROM ECOLI_DATA AA
  JOIN (SELECT A.ID
          FROM ECOLI_DATA A
          JOIN (SELECT *
                  FROM ECOLI_DATA
                 WHERE PARENT_ID IS NULL) B
            ON (A.PARENT_ID = B.ID)) BB
    ON (AA.PARENT_ID = BB.ID)
 ORDER BY AA.ID
