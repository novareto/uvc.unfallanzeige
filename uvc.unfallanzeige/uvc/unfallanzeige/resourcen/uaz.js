$(document).ready(function(){

 $('#form-widgets-unfustdor-0').click( function(event){
     $('#form-widgets-unfustrasse-row, \
        #form-widgets-unfuname-row, \
        #form-widgets-unfunr-row, \
        #form-widgets-unfuplz-row, \
        #form-widgets-unfuort-row').fadeOut()
 });

 $('#form-widgets-unfustdor-1').click( function(event){
     $('#form-widgets-unfustrasse-row, \
        #form-widgets-unfuname-row, \
        #form-widgets-unfunr-row, \
        #form-widgets-unfuplz-row, \
        #form-widgets-unfuort-row').fadeIn()
 });

 $('#optselect').change( function(event){
     var value = $(this).val();
       if (value == '- sonstiges -')
          {
            $('#optinput').attr('disabled', '');
          }  
       else   
            $('#optinput').attr('disabled', 'disabled');
     });


});
