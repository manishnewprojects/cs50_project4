
// Copyright (C) 2018, @mr_dreamerskies

function fetch_itinerary(user_profile){

console.log("got user: ", user_profile);
//console.log("user will visit in season", user_profile[0], "and stay for", user_profile[1], "day(s) and has a user score of", user_profile[2]);

//console.log("typeof", typeof user_profile[0]);

//NOTES: 
//Season: 1(Spring), 2(Summer), 3(Fall), 4(Winter), 5(Any)
//Time of day: 5(Any), 4(Morning), 3(Evening), 2(AFternoon), 1(Morning)
//Type score: 0 (anyone), 500 (Extreme enthu)
//Duration: Number of days in the city


//Check to make sure all info is present

if (typeof user_profile[0] === "undefined" || user_profile[1] == 0) {
	alert("Select Arrival & Days. Thx!");
	//window.location.assign("profile_builder.html");


}

var searchUrl = 'php_includes/getItinerary.php?user_season=' + user_profile[0] + '&user_duration=' + user_profile[1] + '&user_score=' + user_profile[2];

   downloadUrl(searchUrl, function(data) {
   	             	
		var itin_data 	= $.parseXML(data);

		var sight_nodes 	= itin_data.documentElement.getElementsByTagName("sights");

		var sights = new Array(sight_nodes.length);
		 
		for (var i = 0; i < sight_nodes.length; i++) {

		     	sights[i]=[];

		     	sights[i][0]	= sight_nodes[i].getAttribute("id");
		     	sights[i][1]	= sight_nodes[i].getAttribute("title");
		     	sights[i][2]	= sight_nodes[i].getAttribute("url");
		     	sights[i][3]	= parseFloat(sight_nodes[i].getAttribute("lat"));
		     	sights[i][4]    = parseFloat(sight_nodes[i].getAttribute("long"));
		     	sights[i][5] 	= sight_nodes[i].getAttribute("day_num");

 		}    	     

    	//console.log(sights);
 
		var restaurant_nodes = itin_data.documentElement.getElementsByTagName("restaurants");
		 
 		var restaurants = new Array(restaurant_nodes.length);


		for (var i = 0; i < restaurant_nodes.length; i++) {
		     	restaurants[i]=[];

		     	restaurants[i][0]	= restaurant_nodes[i].getAttribute("id");
		     	restaurants[i][1]	= restaurant_nodes[i].getAttribute("name");
		     	restaurants[i][2]	= restaurant_nodes[i].getAttribute("yelp_link");
		     	restaurants[i][3]	= restaurant_nodes[i].getAttribute("timeofday");
		     	restaurants[i][4]	= restaurant_nodes[i].getAttribute("type_score");


		}    	     
 	    //display_itinerary(sights, restaurants);
 	    localStorage.setItem('sights', JSON.stringify(sights));
 	    localStorage.setItem('restaurants', JSON.stringify(restaurants));
 	    localStorage.setItem('duration', user_profile[1]);

  

 	    //document.getElementById('sights').innerHTML = sights ;
 	    //document.getElementById('restaurants').innerHTML = restaurants ;

    	window.location.assign("MAEN_itin_display.php");

 
     });

   
}
 