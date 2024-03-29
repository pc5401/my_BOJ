-- 코드를 입력하세요
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS, 
CASE 
  WHEN FREEZER_YN = 'Y' THEN 'Y'
  WHEN FREEZER_YN = 'N' THEN 'N'
  WHEN FREEZER_YN IS NULL THEN 'N'
END
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '%경기%'
ORDER BY WAREHOUSE_ID ASC;