$(document).ready(function(){
 // Buttons
 $('input#form-action-back').removeClass('btn-primary');
 $('input#form-action-speichern, input#form-action-weiter').addClass('btn-primary');
 // Placeholders
 $('#field-form-basic-field-title').hide()
 $('input#form-job-field-uadst').mask('99.9999');
 $('input#form-job-field-uadst').attr('placeholder', 'MM.JJJJ');
 $('input#form-person-field-prsgeb').mask('99.99.9999').attr('placeholder', 'TT.MM.JJJJ');
 $('input#form-accidenti-field-unfdatum').mask('99.99.9999').attr('placeholder', 'TT.MM.JJJJ');
 $('input#form-accidenti-field-unfzeit').mask('99:99').attr('placeholder', 'HH:MM');
 $('input#form-accidentii-field-unfaedatum').mask('99.99.9999').attr('placeholder', 'TT.MM.JJJJ');
 $('input#form-accidentii-field-unfaezeit').mask('99:99').attr('placeholder', 'HH:MM');
 $('input#form-accidentii-field-unfwax').mask('99.99.9999').attr('placeholder', 'TT.MM.JJJJ');
 $('input#form-accidentii-field-uadbavon').mask('99:99').attr('placeholder', 'HH:MM');
 $('input#form-accidentii-field-uadbabis').mask('99:99').attr('placeholder', 'HH:MM');
});
