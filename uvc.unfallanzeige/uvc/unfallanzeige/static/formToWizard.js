/* Because trolls make the best wizards. */

(function($) {
    $.fn.formToWizard = function(options) {
        options = $.extend({  
            submitButton: "",
	    validateMethod: null,
	    onFailure: null,
	    onSuccess: null,
        }, options); 
        
        var element = this;

        var steps = $(element).find("fieldset");
        var count = steps.size();
        var submmitButtonName = "#" + options.submitButton;
        $(submmitButtonName).hide();

        // 2
        $(element).before("<ul id='steps'></ul>");

        steps.each(function(i) {
            $(this).wrap("<div id='step" + i + "'></div>");
            $(this).append("<p id='step" + i + "commands' class='wizard-commands'></p>");

            // 2
            var name = $(this).find("legend").html();
            $("#steps").append("<li id='stepDesc" + i + "'>Step " + (i + 1) + "<br /><span>" + name + "</span></li>");

            if (i == 0) {
                createNextButton(i);
                selectStep(i);
            }
            else if (i == count - 1) {
                $("#step" + i).hide();
                createPrevButton(i);
		createSubmitButton(i);
            }
            else {
                $("#step" + i).hide();
                createPrevButton(i);
                createNextButton(i);
            }
        });

        function createPrevButton(i) {
            var stepName = "step" + i;
            $("#" + stepName + "commands").append("<a href='#' id='" + stepName + "Prev' class='prev wizard-button'>< Back</a>");

            $("#" + stepName + "Prev").bind("click", function(e) {
		e.preventDefault();
                $("#" + stepName).hide();
                $("#step" + (i - 1)).show();
                $(submmitButtonName).hide();
                selectStep(i - 1);
            });
        }

        function createNextButton(i) {
            var stepName = "step" + i;
            $("#" + stepName + "commands").append("<a href='#' id='" + stepName + "Next' class='next wizard-button'>Next ></a>");

            $("#" + stepName + "Next").bind("click", function(e) {
		e.preventDefault();

		result = options.validateMethod(i);
		if (result != null) {
		    options.onFailure(result);
		    return false;
		}
		else {
		    options.onSuccess();
		}

                $("#" + stepName).hide();
                $("#step" + (i + 1)).show();
                selectStep(i + 1);
            });
        }

	function createSubmitButton(i) {
	    var stepName = "step" + i;
            $("#" + stepName + "commands").append("<a href='#' id='" + stepName + "Submit' class='submit wizard-button'>Submit</a>");

            $("#" + stepName + "Submit").bind("click", function(e) {
		e.preventDefault();

		result = options.validateMethod(i);
		if (result != null) {
		    options.onFailure(result);
		    return false;
		}
		else {
		    options.onSuccess();
                    $('form').submit();
		}
            });
	}

        function selectStep(i) {
            $("#steps li").removeClass("current");
            $("#stepDesc" + i).addClass("current");
        }

    }
})(jQuery); 