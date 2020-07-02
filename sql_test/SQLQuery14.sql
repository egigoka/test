USE [test]
GO

/*CREATE TABLE [dbo].[orders_details](
	id_detail int IDENTITY(1,1) NOT NULL,
	order_id bigint NOT NULL,
	product nvarchar(50) NOT NULL
) ON [PRIMARY]
GO
*/



--INSERT INTO orders_details (order_id, product_shadow) VALUES (3, N'someotherfood')
--DELETE TOP(1) from orders_details where product_shadow = 'cheese'

--SELECT * FROM orders_details

--SELECT * FROM someproducts
--SELECT * FROM someproducts_copy


--SELECT * FROM orders_details JOIN someproducts on product_shadow=product  -- показывает все детали ордеров с информацией о товарах, содержащихся в таблице someproducts
--SELECT * FROM orders_details JOIN someproducts_copy on product_shadow=product  -- показывает все детали ордеров с информацией о товарах, содержащихся в таблице someproducts_copy

--SELECT * FROM orders_details JOIN someproducts on product_shadow=product
--UNION
--SELECT * FROM orders_details JOIN someproducts_copy on product_shadow=product  -- показывает все детали ордеров с информацией о товарах, содержащихся в обоях таблиц

--SELECT * FROM orders_details JOIN someproducts_copy 
--	on product_shadow=product
--	where product = 'milk'  -- можно добавлять дополнительные условия


-- SELECT * FROM someproducts, someproducts_copy  -- cross join
--SELECT * FROM someproducts CROSS JOIN someproducts_copy

--SELECT * INTO orders_details_copy FROM orders_details



--SELECT * FROM orders_details_copy LEFT JOIN someproducts
--	on product_shadow=product

--SELECT * FROM orders_details_copy RIGHT JOIN someproducts
--	on product_shadow=product

--select * from orders_details_copy full join someproducts
--	on product_shadow=product




/*
SELECT * FROM someproducts
WHERE product='cpu'
UNION
SELECT * FROM someproducts
WHERE product='cpu'
UNION
SELECT * FROM orders_details
WHERE product_shadow='cpu'
--All queries combined using a UNION, INTERSECT or EXCEPT operator must have an equal number of expressions in their target lists.
*/


--insert into orders_details_copy values (5, N'cooler')
/*
go

SELECT * FROM someproducts
WHERE product='cpu'
UNION
SELECT * FROM someproducts
WHERE product='cpu'
UNION 
SELECT * FROM someproducts_copy
WHERE product='cheese' and currency='USD'
go 

SELECT * FROM someproducts_copy
WHERE product = 'milk' and currency='RUB



*/

SELECT * FROM orders_details JOIN someproducts on product_shadow=product













