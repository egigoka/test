We have tried to make these label formats as correct as possible according to the UPS specification titled "Guide To Bar Coding With UPS OnLine For Customers Generating Bar Code Labels" Version 5.  You will need to test print and submit samples for approval from UPS before using these label formats in production.  If you find mistakes or if the specification changes, please contact us and inform us of any changes needed and we will make the necessary adjustments to improve the quality of our sample formats.

This file contains the default field assignment list for the label formats "UPS Domestic.btw" and "UPS International.btw."  These labels are complex and have several shared and hidden fields. If you are starting a new database it is recommended you use these field assignments.  This will allow you to use these formats without any changes or adjustments. 

Field 	Data Type
-------------------------------------------------------
1	Ship_To_Name
2	Ship_To_Phone_Number
3	Ship_To_Company
4	Ship_To_Attention
5	Ship_To_Address_1
6	Ship_To_Address_2
7	Ship_To_City
8	Ship_To_State\Province
9	Ship_To_Postal_Code
10	Ship_To_Country
11	Country_Code
12	Class_Of_Service
13	Reference_Number
14	Package_Count
15	Package_Total
16	Package_Weight
17	Packages_Total_Weight
18	Address_Validation
19	Earliest_Delivery_Time
20	VCD
21	COD
22	COD_Cash
23	Hazardous_Materials
24	International_Billing_Options
25	UPS_Account_Number
26	Third_Party_Billing_Account_Number
27	Description
28	EDI_EDI-DOC_INV_or_KEY
29	POA_Power_Of_Attorney
30	SED_Shipper's_Export_Decloration
31	CO_Certificate_of_Origin

To adjust these labels to fit your existing database you will need to use the "Select All" feature from the Edit menu.  You will then see extra "handles" appear around hidden fields that are only in use some of the time depending on the data sent.  These fields are only in use at the time of print and depend on the UPS data and codes needed for your UPS shipment. 

To aid in seeing all the fields, the sample data file "UPS Label.dat" will allow the printing of several labels with different field combinations in use.  Please test print with the sample data file first and then make your changes to your existing database fields.  This will allow you to use the output from our sample to check and compare to your changes.  This should help make sure all the necessary fields have been updated.

Tip:  The document "Guide To Bar Coding With UPS OnLine For Customers Generating Bar Code Labels" Version 5, does not list the UPS 3-digit country codes.  The ISO 3166 codes can be found on the World Wide Web at: http://en.wikipedia.org/wiki/ISO_3166

Reminder:  Submit your new samples to UPS for approval before using these new labels in production.  This will save time and prevent fines or returns.