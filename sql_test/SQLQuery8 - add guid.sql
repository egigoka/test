USE test;
GO

--DELETE FROM guid_table

SELECT COUNT(*) FROM guid_table
SELECT FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff') as 'datetime'  -- https://stackoverflow.com/questions/5312205/how-to-print-getdate-in-sql-server-with-milliseconds-in-time
SELECT * FROM guid_table
--SELECT COUNT(guid_table)


INSERT INTO guid_table VALUES (CAST(NEWID() as char(36)))
SELECT N'INSERTed new GUID' as message, FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff') as datetime
SELECT COUNT(*) FROM guid_table
SELECT * FROM guid_table
GO


UPDATE guid_table
SET guidobj = CAST(NEWID() as char(36));
SELECT N'UPDATEd GUIDs' as message, FORMAT(GETDATE(), 'yyyy-MM-dd HH:mm:ss.fff') as datetime


SELECT COUNT(*) FROM guid_table
SELECT * FROM guid_table

--https://stackoverflow.com/questions/4034976/difference-between-read-commit-and-repeatable-read
/* under REPEATABLE READ the second SELECT is guaranteed to see the rows that has seen at first select 
unchanged. New rows may be added by a concurrent transaction in that one minute, but the existing rows
 cannot be deleted nor changed. */