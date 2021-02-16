import requests

from stations_station import Station, StationStatus
from stations_db import save_data


def fetch_data(url):
	# fetches data from URL
	request = requests.get(url)
	stations_dict = request.json()
	return stations_dict['executionTime'], stations_dict['stationBeanList']

def parse_data(stations_data):
	# Parse Json data into Station objects
	stations = []
	for stations_data in stations_data:
		stations.append(Station(stations_data))
	return stations

def parse_date(date):
	# Parse datetime into date
	return date.split()[0]

def count_red_stations(stations):
	# Count number of red stations in list
	counter = 0
	for station in stations:
		if station.color == StationStatus.RED:
			counter += 1
	return counter

def process_data(date, stations):
	# collect data 
	return {
		'date': date,
		'red_stations': count_red_stations(stations)
	}


#################################
### Main data ingestion logic ###
#################################

def start_data_ingestion(url):
    date, stations_data = fetch_data(url)
    parsed_date = parse_date(date)
    stations = parse_data(stations_data)
    processed_data = process_data(parsed_date, stations)
    save_data(processed_data)


if __name__ == "__main__":
    citibikenyc_url = "http://citibikenyc.com/stations/json"
    start_data_ingestion(url=citibikenyc_url)