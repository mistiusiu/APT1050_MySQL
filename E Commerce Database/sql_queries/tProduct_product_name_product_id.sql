SELECT id AS ProductID, ProductName 
FROM tProduct 
WHERE id IN (
    SELECT ProductID 
    FROM tOrderDetail 
    GROUP BY ProductID 
    HAVING SUM(OrderQty) > 25
);