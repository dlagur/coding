SELECT B.category, sum(S.sales) TOTAL_SALES
FROM BOOK B
INNER JOIN BOOK_SALES S
ON B.book_id = S.book_id
WHERE DATE_FORMAT(S.sales_date, '%Y-%m') = '2022-01'
GROUP BY B.category
ORDER BY B.category
