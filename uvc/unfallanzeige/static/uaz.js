$(document).ready(function(){
 // Buttons
 $('input#form-action-back').removeClass('btn-primary').addClass('btn-default');
 $('input#form-action-speichern, input#form-action-weiter').addClass('btn btn-primary');

 $('input#form-action-5a7572c3bc636b').addClass('btn btn-light');


 $('input#form-job-field-uadst').attr('placeholder', 'MM.JJJJ').mask('99.9999');
 $('input#form-person-field-prsgeb').attr('placeholder', 'TT.MM.JJJJ').mask('99.99.9999');
 $('input#form-accidentii-field-unfaedatum').attr('placeholder', 'TT.MM.JJJJ').mask('99.99.9999');
 $('input#form-accidentii-field-unfaezeit').attr('placeholder', 'HH:MM').mask('99:99');
 $('input#form-accidentii-field-unfwax').attr('placeholder', 'TT.MM.JJJJ').mask('99.99.9999');
 $('input#form-accidentii-field-uadbabis').attr('placeholder', 'HH:MM').mask('99:99');
 $('input#form-accidentii-field-uadbavon').attr('placeholder', 'HH:MM').mask('99:99');
 /*
 $('#form-accidenti-field-unfdatum').focus();
 */
});