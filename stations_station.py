class Station:
	def __init__(self, station_dict):
		self.id = station_dict['id']
		self.available_docks = int(station_dict['availableDocks'])
		self.total_docks = int(station_dict['totalDocks'])
		self.available_bikes = int(station_dict['availableBikes'])
		self.last_communication_time = station_dict['lastCommunicationTime']
		self.color = '' # Populates on initiation
		self._set_color()

	def _get_broken_docks(self):
		# Get number of docks that are not functional
		return self.total_docks - self.available_docks - self.available_bikes

	def _set_color(self):
		# Set color according to: green <= 10 , 10 < yellow < 30, red >= 30
		broken_docks = self._get_broken_docks()

		if broken_docks <= 10:
			self.color = StationStatus.GREEN
		elif 10 < broken_docks < 30:
			self.color = StationStatus.YELLOW
		else:
			self.color = StationStatus.RED

class StationStatus:
	# Assign constants 
    GREEN = 'Green'
    YELLOW = 'Yellow'
    RED = 'Red'