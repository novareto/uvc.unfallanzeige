$(document).ready(function(){
    var v1 = $('#form-widgets-unfustdor-0').is(":checked");
    if ( v1 != true )
      {
        $('#form-widgets-unfustrasse-row').hide();
        $('#form-widgets-unfunr-row').hide();
        $('#form-widgets-unfuplz-row').hide();
        $('#form-widgets-unfuort-row').hide();
      }  

    $('#form-widgets-unfustdor-0').click(function(){
        $('#form-widgets-unfustrasse-row').toggle();
        $('#form-widgets-unfunr-row').toggle();
        $('#form-widgets-unfuplz-row').toggle();
        $('#form-widgets-unfuort-row').toggle();
    });
    $('#form-widgets-unfustdor-1').click(function(){
        $('#form-widgets-unfustrasse-row').toggle();
        $('#form-widgets-unfunr-row').toggle();
        $('#form-widgets-unfuplz-row').toggle();
        $('#form-widgets-unfuort-row').toggle();
    });
});
