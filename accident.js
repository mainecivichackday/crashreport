function accident(town,county,locName,latitude,longitude,time,fatalities,weather,notes) {
	this.town = town;
	this.county = county;
	this.locName = locName;
	this.latitude = latitude;
	this.longitude = longitude;
	this.time = time;
	this.fatalities = fatalities;
	this.weather = weather;
	this.notes = notes;
  }

var union = new accident('Bangor','Penobscot','Union Street x I-95', 44.812121, -68.790245, '2013-06-01T12:37:04',0,'Raining');
console.log(union);
