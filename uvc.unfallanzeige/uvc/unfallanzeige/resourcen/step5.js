$(document).ready(function(){
 // Init Hide All //

 $('#field-form-accidentii-field-unfeba1, #field-form-accidentii-field-unfae1, #field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit, #field-form-accidentii-field-unfwa1, #field-form-accidentii-field-unfwax').hide();

 var death = $('#form-widgets-prstkz-row input:checked').val();
 if (death == 'nein'){
   $('#field-form-accidentii-field-unfae1').show();   
 }

 var fortgesetzt = $('#field-form-accidentii-field-unfae1 input:checked').val();
 if (fortgesetzt == 'ja, sofort'){
   $('#field-form-accidentii-field-unfwa1').show();
 }
 if (fortgesetzt == 'ja, spaeter am'){
   $('#field-form-accidentii-field-unfwa1').show();
   $('#field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit').show();
 }

 var aufgenommen = $('#field-form-accidentii-field-unfwa1 input:checked').val();
 if (aufgenommen == 'ja'){
   $('#field-form-accidentii-field-unfwax').show();
 }

 //Tödlicher Unfall //
 $('#form-accidentii-field-prstkz-nein').click( function(event){ 
   $('#field-form-accidentii-field-unfae1').fadeIn();   
 });   

 //Kein Tödlicher Unfall//
 $('#form-accidentii-field-prstkz-ja').click( function(event){ 
   $('#field-form-accidentii-field-unfae1 input:radio, #field-form-accidentii-field-unfwa1 input:radio').removeAttr('checked');   
   $('#field-form-accidentii-field-unfwax :input, #field-form-accidentii-field-unfaedatum :input, #field-form-accidentii-field-unfaezeit :input').val('');
   $('#field-form-accidentii-field-unfwa1, #field-form-accidentii-field-unfwax, #field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit, #field-form-accidentii-field-unfae1').fadeOut();   
 });    

 // Arbeit nicht beendent //
 $('#form-accidentii-field-unfae1-nein').click( function(event){
   $('#field-form-accidentii-field-unfwa1 input:radio').removeAttr('checked');
   $('#field-form-accidentii-field-unfwa1').hide();
   $('#field-form-accidentii-field-unfwax :input, #field-form-accidentii-field-unfaedatum :input, #field-form-accidentii-field-unfaezeit :input').val('');
   $('#field-form-accidentii-field-unfwax, #field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit').hide();
 });

 //Arbeit sofort eingetellt//
 $('#form-widgets-unfae1-1').click( function(event){
   $('#field-form-accidentii-field-unfwa1').show();
   $('#field-form-accidentii-field-unfaedatum :input, #field-form-accidentii-field-unfaezeit :input').val('');
   $('#field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit').hide();
 });

 //Arbeit eingestellt später am //
 $('#form-widgets-unfae1-2').click( function(event){
   $('#field-form-accidentii-field-unfaedatum, #field-form-accidentii-field-unfaezeit').show();
   $('#field-form-accidentii-field-unfwa1').show();
   $('#field-form-accidentii-field-unfaezeit').hide()
 });


 //Arbeit wieder aufgenommen am //
 $('#form-widgets-unfwa1-0').click( function(event){
   $('#field-form-accidentii-field-unfwax').show();
 });

 //Arbeit nicht wieder aufgenommen am //
 $('#form-widgets-unfwa1-1').click( function(event){
   $('#field-form-accidentii-field-unfwax :input').val('');
   $('#field-form-accidentii-field-unfwax').hide();
 });


 // Besuch beim Arzt //
 var arzt = $('#form-widgets-unfeba-row input:checked').val();
 if (arzt == 'Name und Anschrift'){
   $('#field-form-accidentii-field-unfeba1').show();
 }

 $('#form-widgets-unfeba-0').click( function(event){
   $('#field-form-accidentii-field-unfeba1 :input').val('');
   $('#field-form-accidentii-field-unfeba1').fadeOut();
 });

 $('#form-widgets-unfeba-1').click( function(event){
   $('#field-form-accidentii-field-unfeba1').fadeIn();
 });

 //DoppelFelder //
 $('#field-form-accidentii-field-unfaezeit').appendFieldTo('#field-form-accidentii-field-unfaedatum');
 $('#form-widgets-uadbabis-row').appendFieldTo('#form-widgets-uadbavon-row');
});
