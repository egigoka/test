/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [id_detail]
      ,[order_id]
      ,[product_shadow]
  FROM [test].[dbo].[orders_details_copy]