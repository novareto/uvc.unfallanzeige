$(document).ready(function(){
 
 $('input#form-accidenti-field-unfdatum').attr('placeholder', 'TT.MM.JJJJ').mask('99.99.9999');
 $('input#form-accidenti-field-unfzeit').attr('placeholder', 'HH:MM').mask('99:99');
 $('#field-form-accidenti-field-unfzeit').appendFieldTo('#field-form-accidenti-field-unfdatum');
});
