/* Step II */
$(document).ready(function(){

/* Pflichtfelder rotmarkieren */
$('label[for="form-job-field-unvlaraddr"] span').after('<span> *</span>')


var leihfirma = $('#field-form-job-field-unflar input:checked').val();
 if (leihfirma == 'ja') {
     $('#field-form-job-field-unvlaraddr').show()
     }
 else {
     $('#field-form-job-field-unvlaraddr').hide()
     }

  $('#field-form-job-field-unflar input:radio').change(function() {
      if ($(this).val() == 'ja') {
        $('#field-form-job-field-unvlaraddr').fadeIn().find('textarea').val("");
      }
      else {
        $('#field-form-job-field-unvlaraddr').fadeOut();
      }
  });
});
