-- 코드를 입력하세요
SELECT T1.BOOK_ID, T2.AUTHOR_NAME, TO_char(T1.PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
FROM BOOK T1
INNER JOIN AUTHOR T2
ON T1.AUTHOR_ID = T2.AUTHOR_ID
WHERE T1.CATEGORY = '경제'
ORDER BY T1.PUBLISHED_DATE ASC