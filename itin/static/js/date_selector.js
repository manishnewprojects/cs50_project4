 $(document).ready(function() {

 $( "#datepicker" ).datepicker({
       minDate: new Date(),
      onSelect: function(selectedDate){
      user_profile[0]=get_trip_season(selectedDate); 
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


function call_profile_builder(){

    var data = {'trip_duration': user_profile[0],
                'trip_length': user_profile[1]
                };
    var profile_URL="personalization_engine/profile_builder"
    var csrftoken = Cookies.get('csrftoken');


    console.log("csrf", csrftoken)

    $.ajax({
      headers: { "X-CSRFToken": csrftoken },
      url:profile_URL, 
      method: 'POST',
      data: data, 
      success:function(response){
        if(response === 'success'){ alert('Yay!'); }
        else{ alert('Error! :('); }
      }

    });
}
 
 

$('#build_profile').click(function(){
       console.log("got click", user_profile);
       call_profile_builder();
    }); 


});
