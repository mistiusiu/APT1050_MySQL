-- Queries
--- Number 1
---- Part d


SELECT *
FROM tEmployee


---- Part e


SELECT EmpNo, FirstName, LastName, HireDate
FROM tEmployee
ORDER BY HireDate ASC


---- Part f


SELECT EmpNo, FirstName, LastName, tDepartment.DeptName
FROM tEmployee
INNER JOIN tDepartment
ON tDepartment.DeptNo = tEmployee.DeptName
WHERE tDepartment.DeptNo = 1


--- Number 2
---- Part c


SELECT guestName
FROM Guest
INNER JOIN Booking
ON Guest.guestNo = Booking.guestNo
INNER JOIN Hotel
ON Booking.hotelNo = Hotel.hotelNo
WHERE Hotel.City = 'London' AND Hotel.hotelNo = 1;
