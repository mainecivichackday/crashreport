function accident(town,county,locName,latitude,longitude,time,fatalities,weather,id,notes) {
	this.town = town;
	this.county = county;
	this.locName = locName;
	this.latitude = latitude;
	this.longitude = longitude;
	this.time = time;
	this.fatalities = fatalities;
	this.weather = weather;
	this.id = id;
	this.notes = notes;

  }

function setMarkers(map, locations) {
  // Add markers to the map
  // Marker sizes are expressed as a Size of X,Y
  // where the origin of the image (0,0) is located
  // in the top left of the image.
  // Origins, anchor positions and coordinates of the marker
  // increase in the X direction to the right and in
  // the Y direction down.
  var image = {
    url: 'marker.png',
    //size: new google.maps.Size(20, 32),
    //origin: new google.maps.Point(0,0),
    //anchor: new google.maps.Point(0, 32)
  };
  // Shapes define the clickable region of the icon.
  // The type defines an HTML <area> element 'poly' which
  // traces out a polygon as a series of X,Y points. The final
  // coordinate closes the poly by connecting to the first
  // coordinate.
  //var shape = {
  //    coord: [1, 1, 1, 20, 18, 20, 18 , 1],
  //    type: 'poly'
  //};
  for (var i = 0; i < locations.length; i++) {
    var mark = locations[i];
    var myLatLng = new google.maps.LatLng(mark[1], mark[2]);
    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        shadow: shadow,
        icon: image,
        shape: shape,
        title: mark[0],
        zIndex: mark[3]
    });
  }
};

function initialize() {
  var mapOptions = {
    zoom: 16,
    center: new google.maps.LatLng(44.812111,-68.790441),
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'),
                                mapOptions);
  //var image = 'marker.png';
  //var myLatLng = new google.maps.LatLng(44.812111,-68.790441);
  //var beachMarker = new google.maps.Marker({
  //    position: myLatLng,
  //    map: map,
  //    icon: image
  var x = new accident('Bangor','Penobscot','Union Street Ramp Intersections', 44.810427, -68.79227, '2013-05-30T10:28:12',1,'Snow',0);
  var y = new accident('Bangor','Penobscot','Union Street x I-95', 44.812121, -68.790245, '2013-06-01T12:37:04',0,'Raining',1);
  var markers = [
	[x.locName,x.latitude,x.longitude,x.id],
	[y.locName,y.latitude,y.longitude,y.id]
  ];
  console.log(markers);
  setmarkers(map,markers);

};
