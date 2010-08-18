/* Step3 */
$(document).ready(function(){

/* Hide Show Ehegatten */

/* 1) Initialize) First we hide the relevant Fields */
 $('#field-form-person-field-vehearbeitsv, \
    #field-form-person-field-vehebis, \
    #field-form-person-field-veheentgeltbis').hide()

 var ehegatte = $('#form-widgets-unfbu-1:checked').val();
 if (ehegatte == 'Ehegatte des Unternehmers'){
     $('#field-form-person-field-vehearbeitsv').show();
 }
 
 /* 2) On click on unfbu1 we should show/hide the fields */
 $('#field-form-person-field-unfbu input:radio').change(function() {
     var value = $(this).val();
     if (value == 'Ehegatte des Unternehmers'){
         $('#field-form-person-field-vehearbeitsv').fadeIn();
     }
     else {
         $('#field-form-person-field-vehearbeitsv input:radio').removeAttr('checked');
         $('#field-form-person-field-vehebis :input, #field-form-person-field-veheentgeltbis :input').val('');
         $('#field-form-person-field-vehearbeitsv, #field-form-person-field-vehebis, #field-form-person-field-veheentgeltbis').hide();
     }
     });

 var ehegattenav = $('#field-form-person-field-vehearbeitsv input:checked').val();
 if (ehegattenav == 'Ja'){
     $('#field-form-person-field-vehebis, #field-form-person-field-veheentgeltbis').show();
 }

 $('#field-form-person-field-vehearbeitsv input:radio').change(function() {
     var value = $(this).val();
     if (value == 'Ja'){
         $('#field-form-person-field-vehebis, #field-form-person-field-veheentgeltbis').fadeIn();
     }
     else {
         $('#field-form-person-field-vehebis :input, #field-form-person-field-veheentgeltbis :input').val('');
         $('#field-form-person-field-vehebis, #field-form-person-field-veheentgeltbis').hide();
     }
     });

 // Doppel Feld //
 $('#field-form-person-field-ikzort').appendFieldTo('#field-form-person-field-ikzplz');
 $('#field-form-person-field-iknr').appendFieldTo('#field-form-person-field-ikstr');

});
