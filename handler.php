<html><body>
<?php

$county = $_POST['county'];
$state = $_POST['state'];
$location = $_POST['location'];
$latitude = $_POST['latitude'];
$actual_time = $_POST['actual_time'];
$submitted_time = $_POST['submitted_time'];
$fatalities = $_POST['fatalities'];
$notes = $_POST['notes'];
echo $notes


               
       /*         weather_dic = pywapi.get_weather_from_yahoo(pywapi.get_location_ids(town + ", " + state).keys()[0]);
                weather = (weather_dic['condition']['text']) + ", " + (weather_dic['condition']['temp']) + "C.";
                notes = self.get_argument("notes");
                crashinfo = json.dumps({'town': town, 'county': county, 'state': state, 'location': location, 'latitude': latitude, 'longitude': longitude, 'actual_time': actual_time, 'submitted_time': submitted_time.strftime("%c"), 'fatalities': fatalities, 'weather': weather, 'notes': notes}, sort_keys=False, indent=4, separators=(',', ': '));
                requests.post("http://evilteam.com/api/1/report", data=crashinfo, headers={'content-type': 'application/json'})
                self.write(TLoader.load("post.html")) */

?>
</body></html>

