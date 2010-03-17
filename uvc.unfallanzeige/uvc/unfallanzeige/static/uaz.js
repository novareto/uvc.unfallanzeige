$(document).ready(function(){
  var form = $('form'); 

  function on_success() {

  }

  function on_failure(errors) {
      suffix = "-row";
      $.each(errors, function(key, value) {
	  row = $('#' + key + suffix);
	  row.addClass('row_error');
	  row.append("<div class='error'>" + value + "</div>");
      });
  }

  function inline_validation(idx) {
      $('.row_error').removeClass('row_error');
      $('div.error').remove();

      dataString = form.serialize();
      success = false;
      errors = null;
      $.ajax({
	  type: "POST",
	  url: form.attr('action') + '/++validate++fieldset/' + idx,
	  data: dataString,
	  dataType: "json",
	  async: false,
	  success: function(data) {
	      if (data.success == true) {
		  success = true;
	      } 
	      else {
		  success = false;
		  errors = data.errors
	      }
	  }
      });
      return errors
  }

  form.formToWizard({
      submitButton: 'form-buttons-add',
      validateMethod: inline_validation,
      onFailure: on_failure,
      onSuccess: on_success,
  });

});
