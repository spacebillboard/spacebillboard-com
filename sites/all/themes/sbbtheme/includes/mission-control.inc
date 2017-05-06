<div class="row mission-control">
  <div class="col-md-3 hidden-xs hidden-sm scrollspy-target">

    <ul class="nav nav-list sbb-sidenav" data-spy="affix" data-offset-top="286" data-offset-bottom="270">
      <li>
        <?php include_once(drupal_get_path('theme', 'sbbtheme') . '/featured-sponsor/featured-sponsor.inc.php'); sbb_generate_featured_sponsor(); ?>
      </li>
    </ul>

  </div>
  <div class="col-md-9 col-sm-12 col-xs-12 content">

    <div class="alert alert-info"><span class="glyphicon glyphicon-warning-sign"></span> This page illustrates the mission control center of the satellite after it has been launched. As such, this page will only be shown after the launch of the billboard.</div>

    <div class="row">
      <div class="col-md-12">
        <div id="map-canvas" style="width: 100%; height: 400px;"></div>
      </div>
    </div>
    <div class="row position-details">
      <div class="col-md-3 col-sm-3 col-xs-3">
        <strong>Longitude:</strong><span class="longitude"></span>&deg;
      </div>
      <div class="col-md-3 col-sm-3 col-xs-3">
        <strong>Latitude:</strong><span class="latitude"></span>&deg;
      </div>
      <div class="col-md-3 col-sm-3 col-xs-3">
        <strong>Height:</strong><span class="height-km"></span> km<br/><span class="height-mi"></span> miles
      </div>
      <div class="col-md-3 col-sm-3 col-xs-3">
        <strong>Passing over:</strong><span class="passing-over"></span>
      </div>
    </div>

    <div class="visible-xs visible-sm">
      <?php sbb_generate_horizontal_featured_sponsor(); ?>
    </div>

    <section id="our-mission" class="cubesat-status">
      <h2 class="page-header icon heartbeat">Current CubeSat Status</h2>
      <div class="row">
        <div class="col-md-6 col-sm-6 col-xs-6 star-image">
          <img src="<?php sbb_echo_theme_file('resources/img/mission-control/star-image.png'); ?>" class="img-responsive center-block"/>
          Star sensor image taken <br/>on <span class="image-date">2014-03-10</span> at <span class="image-time">14:34:32</span> GMT.
        </div>
        <div class="col-md-3 col-sm-3 col-xs-3 system-values">
          <h4>Dashboard</h4>
          <div class="system-value">
            <span class="icon gauge"></span><span class="value"><p><span class="speed-km"></span>&nbsp;km/h</p><p><span class="speed-mi"></span>&nbsp;mph</p></span>
          </div>
          <div class="system-value">
            <span class="icon battery"></span><span class="value"><span class="percentage-charged">62</span>% charged</span>
          </div>
          <div class="system-value">
            <span class="icon satellite-dish"></span><span class="value"><span class="downlinking">Not downlinking</span></span>
          </div>
          <div class="system-value">
            <span class="icon power"></span><span class="value"><span class="watt">3.9</span> Watt</span>
          </div>
        </div>
        <div class="col-md-3 col-sm-3 col-xs-3 system-check">
          <h4>System check</h4>
          <div class="row">
            <div class="col-xs-8">
              Payload
            </div>
            <div class="col-xs-4">
              <span class="glyphicon glyphicon-ok"></span>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-8">
              EPS
            </div>
            <div class="col-xs-4">
              <span class="glyphicon glyphicon-ok"></span>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-8">
              COMM
            </div>
            <div class="col-xs-4">
              <span class="glyphicon glyphicon-ok"></span>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-8">
              OBC
            </div>
            <div class="col-xs-4">
              <span class="glyphicon glyphicon-ok"></span>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-8">
              ADCS
            </div>
            <div class="col-xs-4">
              <span class="glyphicon glyphicon-ok"></span>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-8">
              Solar panels
            </div>
            <div class="col-xs-4">
              <span class="glyphicon glyphicon-ok"></span>
            </div>
          </div>
          <div class="row">
            <div class="col-xs-8">
              Antennas
            </div>
            <div class="col-xs-4">
              <span class="glyphicon glyphicon-ok"></span>
            </div>
          </div>
          
        </div>
      </div>    
    </section>

    <section id="stats">
      <h2 class="page-header icon graph">Lifetime Statistics</h2>
      
      <div class="row">
        <div class="col-sm-3 col-xs-6 stat distance">
          <h4>Distance<br/>traveled</h4> 
          <div class="values">
            <div><span class="km">32.4</span> km</div>
            <div><span class="mi">20.1</span> miles</div>
          </div>
          <img src="<?php sbb_echo_theme_file('resources/img/mission-control/runner.jpg'); ?>" class="img-responsive center-block"/>
          <div><span class="ma">771,428</span> marathons</div>
        </div>
        <div class="col-sm-3 col-xs-6 stat">
          <h4>Data<br/>transmitted</h4>
          <div class="values"><span class="mb">1,438</span> megabytes</div>
          <img src="<?php sbb_echo_theme_file('resources/img/mission-control/books.png'); ?>" class="img-responsive center-block"/>
          <div><span class="sh">288</span> times the complete works of Shakespeare</div>
        </div>
        <div class="col-sm-3 col-xs-6 stat">
          <h4>Fasted orbit<br/>so far</h4>
          <div class="values"><span class="min">94.6</span> minutes</div>
          <img src="<?php sbb_echo_theme_file('resources/img/mission-control/orbit.png'); ?>" class="img-responsive center-block"/>
          <div><span class="d">79</span> days, <span class="h">22</span> hours and <span class="m">25.4</span> minutes better than Phileas Fogg</div>
        </div>
        <div class="col-sm-3 col-xs-6 stat">
          <h4>Aliens<br/>spotted</h4>
          <div class="values"><span class="nb">0</span></div>
          <img src="<?php sbb_echo_theme_file('resources/img/mission-control/alien.png'); ?>" class="img-responsive center-block"/>
          <div>Still looking to make friends</div>
        </div>
      </div>      
    </section>

  </div>
</div>

<script type="text/javascript">
(function($) {
  <?php include('mission-control/coords.js') ?>
  // values
  var startTime = new Date(2014, 1, 1, 0, 0, 0, 0);
  var long = coords[0][0];
  var long = coords[0][1];
  var speed = coords[0][2]; // km/s
  var height = 448.7; // km
  // helper functions
  var kmToMi = function(km) {
    return km * 0.621371192;
  };
  var kmpsecTokmph = function(kmpsec) {
    return kmpsec * 60 * 60;
  };
  var now = function() {
    return new Date();
  };
  var timeInOrbit = function() { // in seconds
    return Math.round((now() - startTime) / 1000);
  };
  var distanceTraveled = function() { // in km
    return timeInOrbit() * speed;
  };
  var kmToMarathons = function(km) { // in marathons
    return km / 42.195;
  };
  // 
  var f = function(v) { // print as float with 2 digits
    return Number(v).toFixed(2);
  };
  var pf = function(v) { // print as pretty float
    return f(v).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  };
  var n = function(v) { // print as integer
    return Number(v).toFixed(0);
  };
  var pn = function(v) { // print as pretty integer
    return n(v).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
  };
  var c = function(v) { // print as coordinate
    return Number(v).toFixed(4);
  };
  // functionality
  var showInitialValues = function() {
    $('.height-km').text(f(height));
    $('.height-mi').text(f(kmToMi(height)));
    $('.speed-km').text(f(speed));
    $('.speed-mi').text(f(kmToMi(speed)));
    $('.distance .km').text(pn(distanceTraveled()));
    $('.distance .mi').text(pn(kmToMi(distanceTraveled())));
    $('.distance .ma').text(pn(kmToMarathons(distanceTraveled())));
  };
  var updateValues = function() {
    $('.distance .km').text(pn(distanceTraveled()));
    $('.distance .mi').text(pn(kmToMi(distanceTraveled())));
    $('.distance .ma').text(pn(kmToMarathons(distanceTraveled())));
  };
  // show stuff
  showInitialValues();
  setInterval(updateValues,100);
  // export stuff
  $.sbb = {};
  $.sbb.coords = coords;
  $.sbb.updatePassingOver = function(location) {
    $(".passing-over").text(location);
  };
  $.sbb.updatePositionValues = function(lat, lng) {
    $(".position-details .longitude").text(c(lng));
    $(".position-details .latitude").text(c(lat));
  };
})(jQuery);
</script>
<script type="text/javascript"
  src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBXQ5wd1C0yUnpLFmY9sm2lcQxjiwLPt6Y&sensor=false">
</script>
<script type="text/javascript">
(function($) {
  function initialize() {
    var mapOptions = {
      center: new google.maps.LatLng(-34.397, 150.644),
      zoom: 2
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);

    // show orbit
    var orbitCoordinates = [];
    for(i in $.sbb.coords) {
      orbitCoordinates.push(new google.maps.LatLng($.sbb.coords[i][0], $.sbb.coords[i][1]));
    }
    var orbitPath = new google.maps.Polyline({
      path: orbitCoordinates,
      geodesic: true,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2
    });
    orbitPath.setMap(map);

    // helper function for reverse geocoding
    var country = function(latLng, callback) {
      $.getJSON("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + latLng.toUrlValue() + "&result_type=country&sensor=false&key=AIzaSyBXQ5wd1C0yUnpLFmY9sm2lcQxjiwLPt6Y",
        function(data) {
          console.log(data);
          if(data.results.length == 0) {
            callback("Ocean");
          } else {
            callback(data.results[0]['formatted_address']);
          }
        });
    };

    // show satellite
    var coordsIndex = 250;
    var coords = $.sbb.coords;
    var nextSatellitePosition = function() {
      coordsIndex++;
      var pos = coords[coordsIndex % coords.length];
      return new google.maps.LatLng(pos[0],pos[1]);
    };
    var satellite;
    var showInitialSatellitePosition = function() {
      var pos = nextSatellitePosition();
      satellite = new google.maps.Marker({
          position: pos,
          map: map,
          icon: '<?php sbb_echo_theme_file('resources/img/mission-control/satellite-black.png'); ?>'
      });
      map.panTo(satellite.getPosition());
      $.sbb.updatePositionValues(pos.lat(),pos.lng());
      country(pos, $.sbb.updatePassingOver);
    };
    showInitialSatellitePosition();
    
    // update satellite position later on
    setInterval(function() {
      var pos = nextSatellitePosition();
      satellite.setPosition(pos);
      $.sbb.updatePositionValues(pos.lat(),pos.lng());
    }, 6000);
  }
  google.maps.event.addDomListener(window, 'load', initialize);
})(jQuery);
</script>
