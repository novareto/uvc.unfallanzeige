$(document).ready(function(){
 // Init Hide All //

 $('#form-widgets-unfeba1-row, #form-widgets-unfae1-row, #form-widgets-unfaedatum-row, #form-widgets-unfaezeit-row, #form-widgets-unfwa1-row, #form-widgets-unfwax-row').hide();

 var death = $('#form-widgets-prstkz-row input:checked').val();
 if (death == 'nein'){
   $('#form-widgets-unfae1-row').show();   
 }

 var fortgesetzt = $('#form-widgets-unfae1-row input:checked').val();
 if (fortgesetzt == 'ja, sofort'){
   $('#form-widgets-unfwa1-row').show();
 }
 if (fortgesetzt == 'ja, spaeter am'){
   $('#form-widgets-unfwa1-row').show();
   $('#form-widgets-unfaedatum-row, #form-widgets-unfaezeit-row').show();
 }

 var aufgenommen = $('#form-widgets-unfwa1-row input:checked').val();
 if (aufgenommen == 'ja'){
   $('#form-widgets-unfwax-row').show();
 }

 //Tödlicher Unfall //
 $('#form-widgets-prstkz-1').click( function(event){ 
   $('#form-widgets-unfae1-row').fadeIn();   
 });   

 //Kein Tödlicher Unfall//
 $('#form-widgets-prstkz-0').click( function(event){ 
   $('#form-widgets-unfae1-row input:radio, #form-widgets-unfwa1-row input:radio').removeAttr('checked');   
   $('#form-widgets-unfwax-row :input, #form-widgets-unfaedatum-row :input, #form-widgets-unfaezeit-row :input').val('');
   $('#form-widgets-unfwa1-row, #form-widgets-unfwax-row, #form-widgets-unfaedatum-row, #form-widgets-unfaezeit-row, #form-widgets-unfae1-row').fadeOut();   
 });    

 // Arbeit nicht beendent //
 $('#form-widgets-unfae1-0').click( function(event){
   $('#form-widgets-unfwa1-row input:radio').removeAttr('checked');
   $('#form-widgets-unfwa1-row').hide();
   $('#form-widgets-unfwax-row :input, #form-widgets-unfaedatum-row :input, #form-widgets-unfaezeit-row :input').val('');
   $('#form-widgets-unfwax-row, #form-widgets-unfaedatum-row, #form-widgets-unfaezeit-row').hide();
 });

 //Arbeit sofort eingetellt//
 $('#form-widgets-unfae1-1').click( function(event){
   $('#form-widgets-unfwa1-row').show();
   $('#form-widgets-unfaedatum-row :input, #form-widgets-unfaezeit-row :input').val('');
   $('#form-widgets-unfaedatum-row, #form-widgets-unfaezeit-row').hide();
 });

 //Arbeit eingestellt später am //
 $('#form-widgets-unfae1-2').click( function(event){
   $('#form-widgets-unfaedatum-row, #form-widgets-unfaezeit-row').show();
   $('#form-widgets-unfwa1-row').show();
   $('#form-widgets-unfaezeit-row').hide()
 });


 //Arbeit wieder aufgenommen am //
 $('#form-widgets-unfwa1-0').click( function(event){
   $('#form-widgets-unfwax-row').show();
 });

 //Arbeit nicht wieder aufgenommen am //
 $('#form-widgets-unfwa1-1').click( function(event){
   $('#form-widgets-unfwax-row :input').val('');
   $('#form-widgets-unfwax-row').hide();
 });


 // Besuch beim Arzt //
 var arzt = $('#form-widgets-unfeba-row input:checked').val();
 if (arzt == 'Name und Anschrift'){
   $('#form-widgets-unfeba1-row').show();
 }

 $('#form-widgets-unfeba-0').click( function(event){
   $('#form-widgets-unfeba1-row :input').val('');
   $('#form-widgets-unfeba1-row').fadeOut();
 });

 $('#form-widgets-unfeba-1').click( function(event){
   $('#form-widgets-unfeba1-row').fadeIn();
 });

 //DoppelFelder //
 $('#form-widgets-unfaezeit-row').appendFieldTo('#form-widgets-unfaedatum-row');
 $('#form-widgets-uadbabis-row').appendFieldTo('#form-widgets-uadbavon-row');
});
