USE test
GO

/*ALTER TABLE someproducts
ADD CONSTRAINT someproducts_product_unique UNIQUE (product);*/
-- make product UNIQUE column

--ALTER TABLE someproducts
--DROP CONSTRAINT someproducts_product_unique;

/*DELETE
TOP(1) cost, shippable
FROM someproducts
WHERE [currency] = 'USD'; */

--SELECT *
--FROM [someproducts]
--WHERE [currency] = 'USD'
--OR
--[currency] = 'RUB' AND cost = 3000;

--SELECT COUNT(product)
--FROM [someproducts]
--WHERE [currency] = 'USD'
--OR
--[currency] = 'RUB' AND cost = 3000;

--SELECT AVG(cost)
--FROM someproducts
--WHERE currency = 'RUB';  -- средняя цена

--SELECT SUM(shippable)
--FROM someproducts;  -- количество всех товаров

--INSERT INTO someproducts (product, cost, currency, shippable)
--VALUES (N'mouse', 3, N'USD', 14)



/*UPDATE someproducts
SET currency = 'GPB'
WHERE currency = 'RUB';
*/

SELECT FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff')
WAITFOR DELAY '00:00:01'
SELECT FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff')
SELECT * from someproducts

--SELECT *
--FROM someproducts;

--SELECT DISTINCT cost, currency -- досаём уникальные цены из таблицы
--FROM someproducts;

--DROP TABLE someproducts_2



--SELECT * FROM someproducts

--SELECT * FROM someproducts_copy

/*SELECT * FROM someproducts
UNION
SELECT * FROM someproducts_copy*/