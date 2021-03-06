USE test;
GO
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;  
GO  
BEGIN TRANSACTION;  
SELECT N'Started isolated transaction' as message, FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff') as datetime  -- https://stackoverflow.com/questions/5312205/how-to-print-getdate-in-sql-server-with-milliseconds-in-time
SELECT COUNT(*) FROM guid_table
SELECT * FROM guid_table
GO

SELECT N'Started sleeping for 30 sec' as message, FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff') as datetime
GO
WAITFOR DELAY '00:00:30'  -- https://stackoverflow.com/questions/664902/sleep-command-in-t-sql
SELECT N'Ended sleeping for 30 sec' as message, FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff') as datetime
GO

SELECT COUNT(*) FROM guid_table
SELECT * FROM guid_table

SELECT N'Ended isolated transaction' as message, FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff') as datetime 
COMMIT TRANSACTION;  
GO