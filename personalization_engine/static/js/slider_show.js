
$(document).ready(function(){

$('.done').click(function(){

  user_profile[3]=user_score;
  fetch_itinerary(user_profile);
 

 });



$('.back').click(function(){
   $(this).parent().hide().prev().show();//hide parent and show previous


   sliderUI.reset();

});
 
var slider = document.getElementById('slider');
var node   = document.createElement('div');

var l_emo = document.getElementById('left_emo');
var r_emo = document.getElementById('right_emo');



var sliderUI= noUiSlider.create(slider, {
  start: [0],
  connect: false,
  animate: false,
  range: {
    'min': -10,
    'max': 10
  }
});


node.classList.add('fake-fill');
slider.appendChild(node);



sliderUI.on('update', (values, handle, unencoded, tap, positions) => {


$('.next').click(function(){
   $(this).parent().hide().next().show();//hide parent and show next
   
   user_score=$(this).closest('.next').attr('frame_data')+pos;
   if (user_score >= 1000) {
    user_score=1000
   }

   sliderUI.reset();
});

 var pos = positions[0];
 

  if ((pos >= 0) && (pos < 20))
  {
    node.style.left = '50%';
    node.style.right = 'auto';
    node.style.width = (pos - 50) + '%';
    l_emo.src="/static/personalization_engine/heart_icon.png";
    r_emo.src="/static/personalization_engine/no_go_icon.png";
  }
  else if ((pos > 20) && (pos <40))
  {
    node.style.left = '50%';
    node.style.right = 'auto';
    node.style.width = (pos - 50) + '%';
    l_emo.src="/static/personalization_engine/thumbs_up_icon.png";
    r_emo.src="/static/personalization_engine/thumbs_down_icon.png";
  }
  else if ((pos > 40) && (pos <60))
  {
    node.style.left = '50%';
    node.style.right = 'auto';
    node.style.width = (pos - 50) + '%';
    l_emo.src="/static/personalization_engine/cool_icon.png";
    r_emo.src="/static/personalization_engine/cool_icon.png";
  }
  else if ((pos >= 60) && (pos <= 80)) {
    node.style.left = '50%';
    node.style.right = 'auto';
    node.style.width = (pos - 50) + '%';
    l_emo.src="/static/personalization_engine/thumbs_down_icon.png";
    r_emo.src="/static/personalization_engine/thumbs_up_icon.png";
  }  
  else if ((pos >= 80) && (pos <= 100)) {
    node.style.left = '50%';
    node.style.right = 'auto';
    node.style.width = (pos - 50) + '%';
    l_emo.src="/static/personalization_engine/no_go_icon.png";
    r_emo.src="/static/personalization_engine/heart_icon.png";

  }


});

});