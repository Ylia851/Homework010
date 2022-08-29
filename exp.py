import json

def export_data():
	with open("FIO.json", 'r', encoding='utf-8') as r_file:
		headersJson = ['ID', 'FIO', 'age', 'str_number', 'phone', 'post', 'otdel']
        file_reader = json.load(r_file, delimiter = ";", fieldnames = headersJson, dialect='excel')
		for row in file_reader:
            print(row['id'], row['FIO'], row['age'], row['str_number'], row['phone'], row['post'], row['otdel'], sep = ', ')
