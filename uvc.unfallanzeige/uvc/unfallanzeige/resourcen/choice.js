  $(document).ready(function() {

    $('input.alternative-input').hide();
    $('select.alternative-choice').append(
        '<option class="alt-opt" id="alternative-choice-opt" value="">My value</option>'
    )

    $('select.alternative-choice').change(function(e) {
	if ($(this).find("option:selected").attr('class') == 'alt-opt') {
	    $('input.alternative-input').show('slow');
	}
	else {
	    $('input.alternative-input').hide();
	}
    });

    $('form').submit(function(e) {
        $("option.alt-opt:selected").each(function(){
	    mselect = $(this).closest('select');
	    container = $(this).closest('div');
	    value = container.find('input.alternative-input').val();
	    if (value == "") {
	       alert('Please input a value');
	       e.preventDefault();
	       return false;
            }
	    else {
	       size = mselect.find('option').length;
               id = mselect.attr('id') + '-' + size;
	       mselect.append('<option value="'+value+'" id="'+id+'">'+value+'</option>');
	       mselect.val(value);
	    }
	});
    });
  });