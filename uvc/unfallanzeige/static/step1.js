$(document).ready(function(){


/* Pflichtfelder rotmarkieren */
/*
$('span.label[for="form-basic-field-unfuname"], \
   span.label[for="form-basic-field-unfustrasse"], \
   span.label[for="form-basic-field-unfunr"], \
   span.label[for="form-basic-field-unfuplz"], \
   span.label[for="form-basic-field-unfuort"]').after('<span class="field-required"></span>')

*/
/* Andere Adresse */

var zweigstelle = $('#field-form-basic-field-unfustdor input:checked').val();
if (zweigstelle == 'In einer Zweigniederlassung') {
     $('div#unfustdor').show()
        }
else {
     $('div#unfustdor').hide().find('input').attr('disabled', 'disabled');
        }
 $('#field-form-basic-field-unfustdor input:radio').click( function(event){
     val = $(this).val()
     if (val=='In dem vorher genannten Unternehmen') {
       $('div#unfustdor').slideUp().find('input').attr('disabled','disabled').val('');
     }  
     if (val=='In einer Zweigniederlassung') {
       $('div#unfustdor').slideDown().find('input').removeAttr('disabled');
     }  
 });
});
