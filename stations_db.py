import json

DB_FILE_NAME = 'DataBand_db.json'

def _open_or_create_db_file():
	# Open db file for reading and writting or create and init new db text file
	try:
		with open(DB_FILE_NAME, 'r+') as f:
			return json.load(f)
	except FileNotFoundError:
		with open(DB_FILE_NAME, 'w') as f:
			db_data = []
			json.dump(db_data, f)
			return db_data

def _append_data(processed_data):
	# Append db data with new data
	db_data = _open_or_create_db_file()
	db_data.append(processed_data)
	return db_data

def save_data(processed_data):
	# Save the business data in an accessible location
	update_db_data = _append_data(processed_data)
	with open(DB_FILE_NAME, 'w') as f:
		json.dump(update_db_data, f, indent=4)