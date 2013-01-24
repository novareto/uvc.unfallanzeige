$(document).ready(function(){

/* Pflichtfelder rotmarkieren */
$('label[for="form-accidentii-field-unfae1"], \
   label[for="form-accidentii-field-unfwa1"], \
   label[for="form-accidentii-field-unfaedatum"], \
   label[for="form-accidentii-field-unfwax"], \
   label[for="form-accidentii-field-unfeba1"]').after('<span>*</span>')

// Init Hide All //
 $('#field-form-accidentii-field-unfeba1, #field-form-accidentii-field-unfae1, #field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit, #field-form-accidentii-field-unfwa1, #field-form-accidentii-field-unfwax').hide();

 var death = $('#field-form-accidentii-field-prstkz input:checked').val();
 if (death == 'nein'){
   $('#field-form-accidentii-field-unfae1').show();   
 }

 var fortgesetzt = $('#field-form-accidentii-field-unfae1 input:checked').val();
 if (fortgesetzt == 'ja, sofort'){
   $('#field-form-accidentii-field-unfwa1').show();
 }
 if (fortgesetzt == 'ja, spaeter am:'){
   $('#field-form-accidentii-field-unfwa1').show();
   $('#field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit').show();
 }

 var aufgenommen = $('#field-form-accidentii-field-unfwa1 input:checked').val();
 if (aufgenommen == 'ja'){
   $('#field-form-accidentii-field-unfwax').show();
 }

 //Tödlicher Unfall //
 $('#form-accidentii-field-prstkz-1').click( function(event){ 
   $('#field-form-accidentii-field-unfae1').fadeIn();   
 });   

 //Kein Tödlicher Unfall//
 $('#form-accidentii-field-prstkz-0').click( function(event){ 
   $('#field-form-accidentii-field-unfae1 input:radio, #field-form-accidentii-field-unfwa1 input:radio').removeAttr('checked');   
   $('#field-form-accidentii-field-unfwax :input, #field-form-accidentii-field-unfaedatum :input, #field-form-accidentii-field-unfaezeit :input').val('');
   $('#field-form-accidentii-field-unfwa1, #field-form-accidentii-field-unfwax, #field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit, #field-form-accidentii-field-unfae1').fadeOut();   
 });    

 // Arbeit nicht beendent //
 $('#form-accidentii-field-unfae1-0').click( function(event){
   $('#field-form-accidentii-field-unfwa1 input:radio').removeAttr('checked');
   $('#field-form-accidentii-field-unfwa1').hide();
   $('#field-form-accidentii-field-unfwax :input, #field-form-accidentii-field-unfaedatum :input, #field-form-accidentii-field-unfaezeit :input').val('');
   $('#field-form-accidentii-field-unfwax, #field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit').hide();
 });

 //Arbeit sofort eingetellt//
 $('#form-accidentii-field-unfae1-1').click( function(event){
   $('#field-form-accidentii-field-unfwa1').show();
   $('#field-form-accidentii-field-unfaedatum :input, #field-form-accidentii-field-unfaezeit :input').val('');
   $('#field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit').hide();
 });

 //Arbeit eingestellt später am //
 $('#form-accidentii-field-unfae1-2').click( function(event){
   $('#field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit').show();
   $('#field-form-accidentii-field-unfwa1').show();
   $('#field-form-accidentii-field-unfaezeit').hide()
 });


 //Arbeit wieder aufgenommen am //
 $('#form-accidentii-field-unfwa1-0').click( function(event){
   $('#field-form-accidentii-field-unfwax').show();
 });

 //Arbeit nicht wieder aufgenommen am //
 $('#form-accidentii-field-unfwa1-1').click( function(event){
   $('#field-form-accidentii-field-unfwax :input').val('');
   $('#field-form-accidentii-field-unfwax').hide();
 });


 // Besuch beim Arzt //
 var arzt = $('#field-form-accidentii-field-unfeba input:checked').val();
 if (arzt == 'Aerztliche Behandlung bei:'){
   $('#field-form-accidentii-field-unfeba1').show();
 }

 $('#form-accidentii-field-unfeba-0').click( function(event){
   $('#field-form-accidentii-field-unfeba1 :input').val('');
   $('#field-form-accidentii-field-unfeba1').fadeOut();
 });

 $('#form-accidentii-field-unfeba-1').click( function(event){
   $('#field-form-accidentii-field-unfeba1').fadeIn();
 });

 //DoppelFelder //
 $('#field-form-accidentii-field-unfaezeit').appendFieldTo('#field-form-accidentii-field-unfaedatum');
 $('#field-form-accidentii-field-uadbabis').appendFieldTo('#field-form-accidentii-field-uadbavon');
});
