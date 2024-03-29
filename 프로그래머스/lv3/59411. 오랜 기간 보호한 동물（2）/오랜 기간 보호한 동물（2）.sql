-- 코드를 입력하세요
SELECT T.ANIMAL_ID, T.NAME
FROM (SELECT AI.ANIMAL_ID, AI.NAME, AO.DATETIME - AI.DATETIME AS DAYS
FROM ANIMAL_INS AI INNER JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID
ORDER BY DAYS DESC) T
WHERE ROWNUM <= 2