import csv
with open('C:/Users/admin/Desktop/file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)

# import csv
# with open('C:/Users/admin/Desktop/file - Copy.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line1 in csv_reader:
#         print(line1)
# =====================
# from openpyxl import load_workbook

# book = load_workbook('C:/Users/admin/Desktop/Book1.xlxs')
# sheet = book.active

# rows = sheet.rows

# headers = [cell.value for cell in next(rows)]

# for row in rows:
#     data = {}
#     for title, cell in zip(headers, row):
#         data[title] = cell.value
        
#     print(data)















