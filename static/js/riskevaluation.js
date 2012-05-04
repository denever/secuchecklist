function beforeSubmit(formData, jqForm, options){
}

function showResponse(responseText, statusText, xhr, $form){
}

function error(responseText, statusText, xhr, $form){
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
    if($("#id_check").is(':checked')){
        $( "#tabs" ).tabs("enable", 1);
    }

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
