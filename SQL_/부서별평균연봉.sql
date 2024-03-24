SELECT D.DEPT_ID, D.DEPT_NAME_EN, ROUND(AVG(E.SAL), 0) AVG_SAL
FROM HR_DEPARTMENT D
INNER JOIN HR_EMPLOYEES E
ON D.DEPT_ID = E.DEPT_ID
GROUP BY DEPT_ID
ORDER BY AVG_SAL DESC
