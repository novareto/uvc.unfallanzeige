/* Step3 */
$(document).ready(function(){

/* Plfichtfelder rotmarkieren */
$('span.label[for="form-person-field-vehearbeitsv"], \
   span.label[for="form-person-field-vehebis"], \
   span.label[for="form-person-field-veheentgeltbis"]').after('<span class="field-required"></span>')

/* Hide Show Ehegatten */

 $('#field-form-person-field-vehearbeitsv, \
    #field-form-person-field-vehebis, \
    #field-form-person-field-veheentgeltbis').hide().find('input').attr('disabled', 'disabled')

 var ehegatte = $('#form-person-field-unfbu-4:checked').val();
 if (ehegatte == 'Ehegatte des Unternehmers'){
     $('#field-form-person-field-vehearbeitsv').show().find('input').removeAttr('disabled');
 }
 

 /* 2) On click on unfbu1 we should show/hide the fields */
 $('#field-form-person-field-unfbu input:radio').change(function() {
     var value = $(this).val();
     if (value == 'Ehegatte des Unternehmers' || value == 'eingetragene Lebenspartnerschaft'){
         $('#field-form-person-field-vehearbeitsv').fadeIn().find('input').removeAttr('disabled');
     }
     else {
         $('#field-form-person-field-vehearbeitsv input:radio').removeAttr('checked');
         $('#field-form-person-field-vehebis :input, #field-form-person-field-veheentgeltbis :input').val('');
         $('#field-form-person-field-vehearbeitsv, #field-form-person-field-vehebis, #field-form-person-field-veheentgeltbis').hide().find('input').attr('disabled','disabled');
     }
     });

 var ehegattenav = $('#field-form-person-field-vehearbeitsv input:checked').val();
 if (ehegattenav == 'Ja'){
     $('#field-form-person-field-vehebis, #field-form-person-field-veheentgeltbis').show().find('input').removeAttr('disabled');
 }

 $('#field-form-person-field-vehearbeitsv input:radio').change(function() {
     var value = $(this).val();
     if (value == 'Ja'){
         $('#field-form-person-field-vehebis, #field-form-person-field-veheentgeltbis').fadeIn().find('input').removeAttr('disabled');
     }
     else {
         $('#field-form-person-field-vehebis :input, #field-form-person-field-veheentgeltbis :input').val('');
         $('#field-form-person-field-vehebis, #field-form-person-field-veheentgeltbis').hide().find('input').attr('disabled','disabled');
     }
     });



});
