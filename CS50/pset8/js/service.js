/**
 * service.js
 *
 * Computer Science 50
 * Problem Set 8
 *
 * Implements a shuttle service.
 */

// default height
var HEIGHT = 0.8;


// default latitude
var LATITUDE = 42.3745615030193;

// default longitude
var LONGITUDE = -71.11803936751632;

// default heading
var HEADING = 1.757197490907891;

// default number of seats
var SEATS = 10;

// default velocity
var VELOCITY = 50;

// global reference to shuttle's marker on 2D map
var bus = null;

// global reference to 3D Earth
var earth = null;

// global reference to 2D map
var map = null;

//global # of drop offs
var dropped = 0;

//track # of passengers remaining to be picked up
var num_passengers = 0;

//start on the ground until we fly
var on_the_ground = true;

// global reference to shuttle
var shuttle = null;

// load version 1 of the Google Earth API
google.load("earth", "1");

// load version 3 of the Google Maps API
google.load("maps", "3", {other_params: "sensor=false"});

// once the window has loaded
$(window).load(function() {

    // listen for keydown anywhere in body
    $(document.body).keydown(function(event) {
        return keystroke(event, true);
    });

    // listen for keyup anywhere in body
    $(document.body).keyup(function(event) {
        return keystroke(event, false);
    });

    // listen for click on Drop Off button
    $("#dropoff").click(function(event) {
        dropoff();
    });

    // listen for click on Pick Up button
    $("#pickup").click(function(event) {
        pickup();
    });

    // listen for click on Fly button
    $("#fly").click(function(event) {
        fly();
    });

    // listen for click on Land button
    $("#land").click(function(event) {
        land();
    });

    // listen for click on Autopilot button
    $("#autopilot").click(function(event) {
        autopilot();
    });
    
    // load application
    load();
});

// unload application
$(window).unload(function() {
    unload();
});

/**
 * Renders seating chart.
 */
function chart()
{
    var html = "<div id = 'chart_head'> Seating Chart </div> <ol start='0'>";
    for (var i = 0; i < shuttle.seats.length; i++)
    {
        if (shuttle.seats[i] == null)
        {
            html += "<li>Empty Seat</li>";
        }
        else
        {
            html += "<li>" + shuttle.seats[i].name + " : " + shuttle.seats[i].house + "</li>";
        }
    }
    html += "</ol>";
    $("#chart").html(html);
}

function fly()
{
    $("#announcements").html("Each time you hit the Fly button you rise by 10mt.");
    shuttle.height += 10;
    shuttle.velocity += 50;
    shuttle.cameraAltitude += 10;
    on_the_ground = false;
}

function land()
{
    $("#announcements").html("Prepare to land.");
    shuttle.height = 0.8;
    shuttle.velocity = 50;
    shuttle.cameraAltitude = 0.8;
    on_the_ground = true;
}

/**
 * Drops up passengers if their stop is nearby.
 */
function dropoff()
{
    if (on_the_ground == true)
    {
        dropoffs = [];
        for (var house in HOUSES)
        {
            var lat = HOUSES[house].lat;
            var lng = HOUSES[house].lng;
            var dist = shuttle.distance(lat, lng);  
            if (dist < 30) dropoffs.push(house);
            else $("#announcements").html("No house nearby"); 
        }
    
        for (var s in shuttle.seats)
        {
            if (shuttle.seats[s] != null)
            {
                for(d in dropoffs)
                {
                    if (shuttle.seats[s].house == dropoffs[d])
                    {
                        shuttle.seats[s] = null;
                        $("#announcements").html("Dropped off!");
                        num_passengers--;
                        if (num_passengers > 0)
                        {
                            $("#score").html("There are still " + num_passengers + "<br>waiting to get home.");
                        }
                        else
                        {
                            $("#score").html("CONGRATULATIONS!<br/>You got everybody safely home!");
                        }
                        chart();
                    }   
                }
            
            }
        }
    }
    else $("#announcements").html("You need to land before you can drop off.");
}

/**
 * Called if Google Earth fails to load.
 */
function failureCB(errorCode) 
{
    // report error unless plugin simply isn't installed
    if (errorCode != ERR_CREATE_PLUGIN)
    {
        alert(errorCode);
    }
}

/**
 * Handler for Earth's frameend event.
 */
function frameend() 
{
    shuttle.update();
}

/**
 * Called once Google Earth has loaded.
 */
function initCB(instance) 
{
    // retain reference to GEPlugin instance
    earth = instance;

    // specify the speed at which the camera moves
    earth.getOptions().setFlyToSpeed(100);

    // show buildings
    earth.getLayerRoot().enableLayerById(earth.LAYER_BUILDINGS, true);

    // disable terrain (so that Earth is flat)
    earth.getLayerRoot().enableLayerById(earth.LAYER_TERRAIN, false);

    // prevent mouse navigation in the plugin
    earth.getOptions().setMouseNavigationEnabled(false);

    // instantiate shuttle
    shuttle = new Shuttle({
        heading: HEADING,
        height: HEIGHT,
        latitude: LATITUDE,
        longitude: LONGITUDE,
        planet: earth,
        seats: SEATS,
        velocity: VELOCITY
    });
      
    // synchronize camera with Earth
    google.earth.addEventListener(earth, "frameend", frameend);

    // synchronize map with Earth
    google.earth.addEventListener(earth.getView(), "viewchange", viewchange);

    // update shuttle's camera
    shuttle.updateCamera();

    // show Earth
    earth.getWindow().setVisibility(true);

    // render seating chart
    chart();

    // populate Earth with passengers and houses
    populate();
}

/**
 * Handles keystrokes.
 */
function keystroke(event, state)
{
    // ensure we have event
    if (!event)
    {
        event = window.event;
    }

    //make announcement as shuttle moves
    if (event)
    {
        $("#announcements").html("Remain seated while bus is moving.");
    }
      
    // left arrow
    if (event.keyCode == 37)
    {
        shuttle.states.turningLeftward = state;
        return false;
    }

    // up arrow
    else if (event.keyCode == 38)
    {
        shuttle.states.tiltingUpward = state;
        return false;
    }

    // right arrow
    else if (event.keyCode == 39)
    {
        shuttle.states.turningRightward = state;
        return false;
    }

    // down arrow
    else if (event.keyCode == 40)
    {
        shuttle.states.tiltingDownward = state;
        return false;
    }

    // A, a
    else if (event.keyCode == 65 || event.keyCode == 97)
    {
        shuttle.states.slidingLeftward = state;
        return false;
    }

    // D, d
    else if (event.keyCode == 68 || event.keyCode == 100)
    {
        shuttle.states.slidingRightward = state;
        return false;
    }
  
    // S, s
    else if (event.keyCode == 83 || event.keyCode == 115)
    {
        shuttle.states.movingBackward = state;     
        return false;
    }

    // W, w
    else if (event.keyCode == 87 || event.keyCode == 119)
    {
        shuttle.states.movingForward = state;    
        return false;
    }
  
    return true;
}

/**
 * Loads application.
 */
function load()
{
    // embed 2D map in DOM
    var latlng = new google.maps.LatLng(LATITUDE, LONGITUDE);
    map = new google.maps.Map($("#map").get(0), {
        center: latlng,
        disableDefaultUI: true,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        scrollwheel: false,
        zoom: 16, //was 17
        zoomControl: true
    });

    // prepare shuttle's icon for map
    bus = new google.maps.Marker({
        icon: "https://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/bus.png",
        map: map,
        title: "you are here"
    });

    // embed 3D Earth in DOM
    google.earth.createInstance("earth", initCB, failureCB);
}

/**
 * Picks up nearby passengers.
 */
function pickup()
{   
    if(on_the_ground == true)
    {
        empty_seats = [];
        for (var s = 0; s < shuttle.seats.length; s++)
            {
                if (shuttle.seats[s] == null) empty_seats.push(s);
            }
    
        if (empty_seats.length == 0)
            {
                $("#announcements").html("Sorry! No more empty seats on the bus!");
                return;
            }
    
        else
        {
            //check if suitable passengers nearby for a ride
            pickups = [];
            for (var p in PASSENGERS) //check who is nearby & add to pickup list
            {      
                //check house & don't pick up same passenger twice!
                if (! PASSENGERS[p].collected)
                {
                    for (var house in HOUSES)
                    {    
                        if (PASSENGERS[p].house == house)
                        {
                            var lat = PASSENGERS[p].mark.position.k;
                            var lng = PASSENGERS[p].mark.position.A;
                            var dist = shuttle.distance(lat, lng);  
                            if (dist < 15) pickups.push(PASSENGERS[p]);
                        }
                    }
                }
            }
                 
            if (pickups.length == 0) $("#announcements").html("<strong>OOPS! No-one here to pick up!</strong>");
        
            else
            {
                for (var pickup in pickups)
                {
                    if (empty_seats.length == 0)
                    {
                        $("#announcements").html("Sorry! No more empty seats on the bus!");
                        return;
                    }
                
                    else
                    {
                        unoccupied = empty_seats.shift();
                        shuttle.seats[unoccupied] = pickups[pickup];
                        pickups[pickup]["collected"] = "true" //mark passenger as having been collected so not picked up twice
                        $("#announcements").html("Picking Up!");

                        //remove placemark
                        var features = earth.getFeatures();
                        features.removeChild(pickups[pickup].pmark);
        
                        //remove marker
                        pickups[pickup].mark.setMap(null);
                    
                        //redraw seating chart
                        chart();
                    } 
                } 
            }
        } 
    }
    else $("#announcements").html("You need to land before you can pick up!");
}      

function autopilot()
{
    pickup()
}    




/**
 * Populates Earth with passengers and houses.
 */
function populate()
{
    // mark houses
    for (var house in HOUSES)
    {
        // plant house on map
        new google.maps.Marker({
            icon: "https://google-maps-icons.googlecode.com/files/home.png",
            map: map,
            position: new google.maps.LatLng(HOUSES[house].lat, HOUSES[house].lng),
            title: house
        });
    }

    // get current URL, sans any filename
    var url = window.location.href.substring(0, (window.location.href.lastIndexOf("/")) + 1);

    // scatter passengers
    for (var i = 0; i < PASSENGERS.length; i++)
    {
        // pick a random building
        var building = BUILDINGS[Math.floor(Math.random() * BUILDINGS.length)];

        // prepare placemark
        var placemark = earth.createPlacemark("");
        placemark.setName(PASSENGERS[i].name + " to " + PASSENGERS[i].house);

        // prepare icon
        var icon = earth.createIcon("");
        icon.setHref(url + "/img/" + PASSENGERS[i].username + ".jpg");

        // prepare style
        var style = earth.createStyle("");
        style.getIconStyle().setIcon(icon);
        style.getIconStyle().setScale(4.0);

        // prepare stylemap
        var styleMap = earth.createStyleMap("");
        styleMap.setNormalStyle(style);
        styleMap.setHighlightStyle(style);

        // associate stylemap with placemark
        placemark.setStyleSelector(styleMap);

        // prepare point
        var point = earth.createPoint("");
        point.setAltitudeMode(earth.ALTITUDE_RELATIVE_TO_GROUND);
        point.setLatitude(building.lat);
        point.setLongitude(building.lng);
        point.setAltitude(0.0);

        // associate placemark with point
        placemark.setGeometry(point);

        // add placemark to Earth
        earth.getFeatures().appendChild(placemark);

        // add marker to map
        var marker = new google.maps.Marker({
            icon: "https://maps.gstatic.com/intl/en_us/mapfiles/ms/micons/man.png",
            map: map,
            position: new google.maps.LatLng(building.lat, building.lng),
            title: PASSENGERS[i].name + " at " + building.name
        });

        //remember passenger's placemark and marker for pick-up's sake
        var mark;
        var pmark;        
        PASSENGERS[i].mark = marker;
        PASSENGERS[i].pmark = placemark;
        
        //count number of legitimate passengers to be picked up  
        for (var house in HOUSES)
            {    
                if (PASSENGERS[i].house === house) num_passengers++;
            }                 
            $("#score").html("There are " + num_passengers + " people<br> to take home.");
        
    }
}

/**
 * Handler for Earth's viewchange event.
 */
function viewchange() 
{
    // keep map centered on shuttle's marker
    var latlng = new google.maps.LatLng(shuttle.position.latitude, shuttle.position.longitude);
    map.setCenter(latlng);
    bus.setPosition(latlng);
}

/**
 * Unloads Earth.
 */
function unload()
{
    google.earth.removeEventListener(earth.getView(), "viewchange", viewchange);
    google.earth.removeEventListener(earth, "frameend", frameend);
}
