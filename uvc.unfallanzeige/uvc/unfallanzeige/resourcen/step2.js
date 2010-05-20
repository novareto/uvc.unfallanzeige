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
      $('#form-widgets-unvlaraddr-row').toggle();
  });
});
