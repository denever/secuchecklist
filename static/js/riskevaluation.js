// jQuery(document).ajaxSend(function(event, xhr, settings) {
//     function getCookie(name) {
//         var cookieValue = null;
//         if (document.cookie && document.cookie != '') {
//             var cookies = document.cookie.split(';');
//             for (var i = 0; i < cookies.length; i++) {
//                 var cookie = jQuery.trim(cookies[i]);
//                 // Does this cookie string begin with the name we want?
//                 if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
//     function sameOrigin(url) {
//         // url could be relative or scheme relative or absolute
//         var host = document.location.host; // host + port
//         var protocol = document.location.protocol;
//         var sr_origin = '//' + host;
//         var origin = protocol + sr_origin;
//         // Allow absolute or scheme relative URLs to same origin
//         return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
//             (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
//             // or any other URL that isn't scheme relative or absolute i.e relative.
//             !(/^(\/\/|http:|https:).*/.test(url));
//     }
//     function safeMethod(method) {
//         return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//     }

//     if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
//         xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//     }
// });
function beforeSubmit(formData, jqForm, options){
}

function showResponse(responseText, statusText, xhr, $form){
    console.log(statusText);
}

function error(responseText, statusText, xhr, $form){
    console.log(responseText);
    console.log(statusText);
    console.log(xhr);
}

function risk_evaluation_interface() {
    $( "#tabs" ).tabs();
    $( "#tabs" ).tabs("disable", 1);
    $( "#tabs" ).tabs("select", 0);
    $( "#show-notes" ).button({
				  text: false,
				  icons: { primary: "ui-icon-info"},
			      }).click(function() {
					   $("#dlg-notes").dialog('open');
				       });
    $( "#show-sugg-yes" ).button({
				     text: false,
				     icons: { primary: "ui-icon-info"},
				 }).click(function() {
					      $("#dlg-sugg-yes").dialog('open');
					  });
    $( "#show-sugg-no" ).button({
				    text: false,
				    icons: { primary: "ui-icon-info"},
				}).click(function() {
					     $("#dlg-sugg-no").dialog('open');
					 });
    $( "#id_check" ).button().change(
	function(){
	    if($("#id_check").is(':checked')){
		$( "#tabs" ).tabs("enable", 1);
	    }else{
		$( "#tabs" ).tabs("disable", 1);
	    }
	}
    );
    $( "#dlg-notes" ).dialog({ autoOpen: false });
    $( "#dlg-sugg-no" ).dialog({ autoOpen: false });
    $( "#dlg-sugg-yes" ).dialog({ autoOpen: false });
    $( "#riskevalform" ).ajaxForm({
				      beforeSubmit: beforeSubmit,
				      error: error,
				      complete: showResponse,
				      type: 'post'
				  });
}
