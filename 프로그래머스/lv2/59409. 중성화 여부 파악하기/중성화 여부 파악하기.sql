-- 코드를 입력하세요
SELECT 
  ANIMAL_ID, 
  NAME, 
  CASE
    WHEN lower(SEX_UPON_INTAKE) LIKE '%neutered%' THEN 'O'
    WHEN lower(SEX_UPON_INTAKE) LIKE '%spayed%' THEN 'O'
    ELSE 'X'
  END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;