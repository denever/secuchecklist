function sameOrigin(url) {
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

function safeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function beforeSubmit(formData, jqForm, options){
}

//function showResponse(responseText, statusText, xhr, $form){
function showResponse(xhr){
    console.log(xhr);
}

function error(responseText, statusText, xhr, $form){
    console.log(responseText);
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

    $( "#id_status" ).change(
        function(){
            if($("#id_status").val() == 2){
                $( "#tabs" ).tabs("enable", 1);
                $( "#tabs" ).tabs("enable", 2);
            }else{
                $( "#tabs" ).tabs("disable", 1);
                $( "#tabs" ).tabs("disable", 2);
            }
            var postdata={
                'revision_id': $('#id_revision').val(),
                'riskfactor_id': $('#id_riskfactor').val(),
                'status': $('#id_status').val(),
            };
            $.post('status', postdata);
        }
    );

    $( "#id_measure_taken" ).change(
        function(){
            if($("#id_measure_taken").is(':checked')){
                var postdata={
                    'revision_id': $('#id_revision').val(),
                    'riskfactor_id': $('#id_riskfactor').val(),
                };
                $.post('take', postdata);
            }else{
                var postdata={
                    'revision_id': $('#id_revision').val(),
                    'riskfactor_id': $('#id_riskfactor').val(),
                };
                $.post('untake', postdata);
            }
        }
    );

    $( "#id_probability" ).change(
        function(){
            var postdata={
                'revision_id': $('#id_revision').val(),
                'riskfactor_id': $('#id_riskfactor').val(),
                'probability': $(this).val(),
            };
            $.post('probeval', postdata);
        }
    );

    $( "#id_seriousness" ).change(
        function(){
            var postdata={
                'revision_id': $('#id_revision').val(),
                'riskfactor_id': $('#id_riskfactor').val(),
                'seriousness': $(this).val(),
            };
            $.post('sereval', postdata);
        }
    );

    if($("#id_status").val() == 2){
        $( "#tabs" ).tabs("enable", 1);
        $( "#tabs" ).tabs("enable", 2);
    }else{
        $( "#tabs" ).tabs("disable", 1);
        $( "#tabs" ).tabs("disable", 2);
    }

    $( "#dlg-notes" ).dialog({ autoOpen: false });
    $( "#dlg-sugg-no" ).dialog({ autoOpen: false });
    $( "#dlg-sugg-yes" ).dialog({ autoOpen: false });

}
