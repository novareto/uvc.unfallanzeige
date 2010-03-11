$(document).ready(function(){
  $('a.validate').click(function(e) {
        e.preventDefault();
	dataString = $("form").serialize();
        idx = $(this).closest('fieldset').attr('rel');
	$.ajax({
	    type: "POST",
	    url: $('form').attr('action') + '/++validate++fieldset/' + idx,
	    data: dataString,
	    dataType: "json",
	    success: function(data) {
		if(data.success) {
		    alert('no error');
		} 
		else
		{
		    $.each(data.errors, function(i, error) {
			alert(i + ' ' + error);
		    });
		}
	    }
	});
    });
});
