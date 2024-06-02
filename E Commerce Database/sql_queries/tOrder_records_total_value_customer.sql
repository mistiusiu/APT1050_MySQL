SELECT CustomerID, SUM(Value)
AS 'Total Value'
FROM tOrder
GROUP BY CustomerID;