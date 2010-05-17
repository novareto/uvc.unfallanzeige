$(document).ready(function(){

/* Doppel Feld Telefonnummer Ansprechpartner */

 $('#form-widgets-anspfon-row').appendFieldTo('#form-widgets-anspname-row');


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


/* Hide Show Ehegatten */
 /* 1) Initialize) First we hide the relevant Fields */
 $('#form-widgets-vehearbeitsv-row, \
    #form-widgets-vehebis-row, \
    #form-widgets-veheentgeltbis-row').hide()

 var ehegatte = $('#form-widgets-unfbu-1:checked').val();
 if (ehegatte == 'Ehegatte des Unternehmers'){
     $('#form-widgets-vehearbeitsv-row').show();
 }
 
 /* 2) On click on unfbu1 we should show/hide the fields */
 $('#form-widgets-unfbu-row input:radio').change(function() {
     var value = $(this).val();
     if (value == 'Ehegatte des Unternehmers'){
         $('#form-widgets-vehearbeitsv-row').show();
     }
     else {
         $('#form-widgets-vehearbeitsv-row').hide();
     }
     });

 var ehegattenav = $('#form-widgets-vehearbeitsv-0:checked').val();
 if (ehegattenav == 'Ja'){
     $('#form-widgets-vehebis-row, #form-widgets-veheentgeltbis-row').show();
 }

 $('#form-widgets-vehearbeitsv-row input:radio').change(function() {
     var value = $(this).val();
     if (value == 'Ja'){
         $('#form-widgets-vehebis-row, #form-widgets-veheentgeltbis-row').show();
     }
     else {
         $('#form-widgets-vehebis-row, #form-widgets-veheentgeltbis-row').hide();
     }
     });

});
