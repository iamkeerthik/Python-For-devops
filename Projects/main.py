import openpyxl
inv_file=openpyxl.load_workbook("Inventory.xlsx")
product_list= inv_file["Sheet1"]