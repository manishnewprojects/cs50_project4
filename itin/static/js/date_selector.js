 $(document).ready(function() {

 $( "#datepicker" ).datepicker({
       minDate: new Date(),
      onSelect: function(selectedDate){
      user_profile[1]=selectedDate;
      user_profile[3]=get_trip_season(selectedDate); 
      //console.log("this is date", user_profile[0], "--goy--", selectedDate);

      }
    });
  
    function get_trip_season(visit_day) {

    var month = visit_day.substring(
        0,visit_day.lastIndexOf("/") - 3
    );
    var season = 1
    if ((month > 5) &&(month < 8))
      season=2;
    else if ((month > 7) &&(month < 10))
      season=3;
    else if ((month >= 10) || (month <= 2))
      season=4;
    return season;
    } //end of function get_trip_season


});
