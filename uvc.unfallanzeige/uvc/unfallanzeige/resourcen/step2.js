/* Step II */
$(document).ready(function(){

/* Pflichtfelder rotmarkieren */
$('span.label[for="form-job-field-unvlaraddr"]').after('<span class="field-required"></span>')


var leihfirma = $('#field-form-job-field-unflar input:checked').val();
 if (leihfirma == 'ja') {
     $('#field-form-job-field-unvlaraddr').show()
     }
 else {
     $('#field-form-job-field-unvlaraddr').hide()
     }

  $('#field-form-job-field-unflar input:radio').change(function() {
      if ($(this).val() == 'ja') {
        $('#field-form-job-field-unvlaraddr').fadeIn();
      }
      else {
        $('#field-form-job-field-unvlaraddr').fadeOut();
      }
  });
});
