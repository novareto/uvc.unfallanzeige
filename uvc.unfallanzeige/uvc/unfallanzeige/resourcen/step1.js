$(document).ready(function(){

/* Doppel Felder */

 $('#form-widgets-anspfon-row').appendFieldTo('#form-widgets-anspname-row');
 $('#form-widgets-unfuort-row').appendFieldTo('#form-widgets-unfuplz-row');
 $('#form-widgets-unfunr-row').appendFieldTo('#form-widgets-unfustrasse-row');

/* Andere Adresse */

 var zweigstelle = $('#form-widgets-unfustdor-row input:checked').val();
 
 if (zweigstelle == 'In einer Zweigniederlassung') {
     $('#form-widgets-unfustrasse-row, \
        #form-widgets-unfuname-row, \
        #form-widgets-unfuplz-row').show()
        }
 else {
     $('#form-widgets-unfustrasse-row, \
        #form-widgets-unfuname-row, \
        #form-widgets-unfunr-row, \
        #form-widgets-unfuplz-row, \
        #form-widgets-unfuort-row').hide()
        }

 $('#form-widgets-unfustdor-0').click( function(event){
     $('#form-widgets-unfustrasse-row, \
        #form-widgets-unfuname-row, \
        #form-widgets-unfunr-row, \
        #form-widgets-unfuplz-row, \
        #form-widgets-unfuort-row').slideUp();
 });

 $('#form-widgets-unfustdor-1').click( function(event){
     $('#form-widgets-unfustrasse-row, \
        #form-widgets-unfuname-row, \
        #form-widgets-unfuplz-row').slideDown();
 });
});
