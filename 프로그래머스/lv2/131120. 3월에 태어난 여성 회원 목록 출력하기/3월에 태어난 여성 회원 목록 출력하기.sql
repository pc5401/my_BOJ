-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, 
        TO_CHAR(DATE_OF_BIRTH, 'yyyy-mm-dd') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE TO_CHAR(DATE_OF_BIRTH,'yyyy-mm-dd') like '%-03-%'
AND GENDER = 'W'
AND NOT TLNO IS NULL
ORDER BY MEMBER_ID ASC;