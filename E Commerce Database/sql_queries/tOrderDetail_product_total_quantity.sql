SELECT ProductID, SUM(OrderQty)
AS Total_Quantity
FROM tOrderDetail
GROUP BY ProductID
HAVING SUM(OrderQty) > 20;