$(document).ready(function(){

  var form = $('form'); 
  var wizard = $('#wizard')

  $("ul.tabs", wizard).tabs("#panes > div",
			    function(event, index) { 
	if (index > 0) {
	    dataString = form.serialize();
            idx = index - 1;
	    success = false;
	    $.ajax({
		type: "POST",
		url: form.attr('action') + '/++validate++fieldset/' + idx,
		data: dataString,
		dataType: "json",
		async: false,
		success: function(data) {
		    if (data.success == true) {
			alert('success');
			success = true;
		    } 
		    else {
			alert('failure');
			success = false;
		    }
		}
	    });
	    return success;
	}
    });
 
    $("#panes > div").not(':last').append(
	'<button class="next">Next</button>');

    $("#panes > div").not(':first').append(
	'<button class="prev">Previous</button>');

    $("#panes > div:last").append(
	'<button class="submit">Send</button>');

    form.find('input[type=submit]').remove();

    var api = $("ul.tabs", wizard).tabs(0); 

    // "next tab" button 
    $("button.next").click(function() { 
        api.next(); 
    }); 
 
    // "previous tab" button 
    $("button.prev").click(function() { 
        api.prev(); 
    });

    $("button.submit").click(function() {
        form.submit();
    });

});
