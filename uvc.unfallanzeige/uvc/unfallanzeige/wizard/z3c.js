// (c) Souheil Chelfouh for Novareto

$(document).ready(function() {

   jQuery.fn.flash = function(opacity, cycle, duration) {
      for(current=0; current < cycle; current++) {
        this.animate( { opacity: opacity }, duration / 2 );
        this.animate( { opacity: '1' }, duration / 2 );
      }
    }

  $('form input[type=submit]').live("click", function(e) {
      clicked = "&" + $(this).attr('name') + "=" + $(this).attr('value');
      
      dataString = $('form').serialize() + clicked;
      success = false;
      errors = null;
      $.ajax({
	  type: $('form').attr('method'),
	  url: $('form').attr('action'),
	  data: dataString,
	  async: false,
	  complete: function(data, text) {
	      var html = $(data.responseText).find('#inner-page').html();

	      $("#inner-page").fadeOut("slow", function(){
		  $("#inner-page").html(html);
	      });
	      
	      $("#inner-page").fadeIn("slow", function(){
		  $("form input[type=submit]").flash(0.4, 2, 500);
	      });
	  }
      });
      return false;
  });

});