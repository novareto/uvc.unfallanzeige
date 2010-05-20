/* Step3 */
$(document).ready(function(){

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
         $('#form-widgets-vehearbeitsv-row').fadeIn();
     }
     else {
         $('#form-widgets-vehearbeitsv-row input:radio').removeAttr('checked');
         $('#form-widgets-vehebis-row :input, #form-widgets-veheentgeltbis-row :input').val('');
         $('#form-widgets-vehearbeitsv-row, #form-widgets-vehebis-row, #form-widgets-veheentgeltbis-row').hide();
     }
     });

 var ehegattenav = $('#form-widgets-vehearbeitsv-0:checked').val();
 if (ehegattenav == 'Ja'){
     $('#form-widgets-vehebis-row, #form-widgets-veheentgeltbis-row').show();
 }

 $('#form-widgets-vehearbeitsv-row input:radio').change(function() {
     var value = $(this).val();
     if (value == 'Ja'){
         $('#form-widgets-vehebis-row, #form-widgets-veheentgeltbis-row').fadeIn();
     }
     else {
         $('#form-widgets-vehebis-row :input, #form-widgets-veheentgeltbis-row :input').val('');
         $('#form-widgets-vehebis-row, #form-widgets-veheentgeltbis-row').hide();
     }
     });

 // Doppel Feld //
 $('#form-widgets-ikzort-row').appendFieldTo('#form-widgets-ikzplz-row');
 $('#form-widgets-iknr-row').appendFieldTo('#form-widgets-ikstr-row');

});
