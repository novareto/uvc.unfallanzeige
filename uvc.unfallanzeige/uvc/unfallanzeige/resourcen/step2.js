/* Step II */
$(document).ready(function(){
 var leihfirma = $('#form-widgets-unflar-row input:checked').val();
 if (leihfirma == 'ja') {
     $('#form-widgets-unvlaraddr-row').show()
     }
 else {
     $('#form-widgets-unvlaraddr-row').hide()
     }

  $('#form-widgets-unflar-row input:radio').change(function() {
      if ($(this).val() == 'ja') {
        $('#form-widgets-unvlaraddr-row').fadeIn();
      }
      else {
        $('#form-widgets-unvlaraddr-row').fadeOut();
      }
  });
});
