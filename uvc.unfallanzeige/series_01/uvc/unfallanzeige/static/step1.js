$(document).ready(function(){

/* Doppel Felder */

 $('#field-form-basic-field-anspfon').appendFieldTo('#field-form-basic-field-anspname');
 $('#field-form-basic-field-unfunr').appendFieldTo('#field-form-basic-field-unfustrasse');
 $('#field-form-basic-field-unfuort').appendFieldTo('#field-form-basic-field-unfuplz');

/* Pflichtfelder rotmarkieren */
$('span.label[for="form-basic-field-unfuname"], \
   span.label[for="form-basic-field-unfustrasse"], \
   span.label[for="form-basic-field-unfunr"], \
   span.label[for="form-basic-field-unfuplz"], \
   span.label[for="form-basic-field-unfuort"]').after('<span class="field-required"></span>')


/* Andere Adresse */

 var zweigstelle = $('#field-form-basic-field-unfustdor input:checked').val();
 
 if (zweigstelle == 'In einer Zweigniederlassung') {
     $('#field-form-basic-field-unfustrasse, \
        #field-form-basic-field-unfuname, \
        #field-form-basic-field-unfuplz').show()
        }
 else {
     $('#field-form-basic-field-unfustrasse, \
        #field-form-basic-field-unfuname, \
        #form-widgets-unfunr-row, \
        #field-form-basic-field-unfuplz, \
        #field-form-basic-field-unfuort').hide()
        }

 $('#field-form-basic-field-unfustdor input:radio').click( function(event){
     val = $(this).val()
     if (val=='In dem vorher genannten Unternehmen') {
       /* Feldinhalte leeren */ 
      /* $('#form-basic-field-unfustrasse, \
          #form-basic-field-unfuname, \
          #form-basic-field-unfuplz, \
          #form-basic-field-unfunr, \
          #form-basic-field-unfuort').find('input').val("");*/
      
 
       $('#field-form-basic-field-unfustrasse, \
          #field-form-basic-field-unfuname, \
          #form-widgets-unfunr-row, \
          #field-form-basic-field-unfuplz, \
          #field-form-basic-field-unfuort').slideUp().find('input').val("");
        }  
        if (val=='In einer Zweigniederlassung') {
       $('#field-form-basic-field-unfustrasse, \
        #field-form-basic-field-unfuname, \
        #field-form-basic-field-unfuplz').slideDown();
      }  
 });

});
