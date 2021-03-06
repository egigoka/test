USE test;
GO

--SELECT FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff')  -- https://stackoverflow.com/questions/5312205/how-to-print-getdate-in-sql-server-with-milliseconds-in-time
--WAITFOR DELAY '00:00:01'  -- https://stackoverflow.com/questions/664902/sleep-command-in-t-sql
--SELECT FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff')



/*SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;  -- https://docs.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql?view=sql-server-2017
GO  
BEGIN TRAN
SELECT (N'@@trancount') as 'command', @@trancount as output  -- https://stackoverflow.com/questions/11764818/nested-transactions-in-tsql
SELECT * from someproducts_copy;
END
BEGIN TRAN
SELECT (N'@@trancount') as 'command', @@trancount as output
SELECT * from someproducts_copy
BEGIN TRAN
SELECT (N'@@trancount') as 'command', @@trancount as output
INSERT INTO someproducts_copy (product, cost, currency, shippable) VALUES (1,2,3,4)
SELECT * from someproducts_copy


ROLLBACK TRAN
SELECT (N'@@trancount') as 'command', @@trancount as output
SELECT * from someproducts_copy*/

SELECT COUNT(*) FROM guid_table
INSERT INTO guid_table VALUES (CAST(NEWID() as char(36)))
SELECT COUNT(*) FROM guid_table