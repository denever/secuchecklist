function beforeSubmit(formData, jqForm, options){
    console.log('Sottomettiamola');
}

function showResponse(responseText, statusText, xhr, $form){
    console.log(statusText);
}

function buildtree(root_id){
    $('#riskfactors').jstree({
				 "plugins": ["themes",
					     "json",
					     "ui",
					     "cookies",
					     "dnd",
					     "types",
					     "search",
					     "hotkeys",
					     "contextmenu"
					    ],
				 "json": {
				     "ajax": {
					 "url" : function(n){
					     if(n==-1){
						 if(root_id){
						     return "/riskfactors/node/"+root_id;
						 }
						 return "/riskfactors/node/0/";
					     }
					     // if(n.data){
					     //		 console.log(n.children());
					     //		 console.log(n.data('id'));
					     //		 return "/riskfactors/"+n.data('id')+"/subtree/";
					     // }
					 },
					 progressive_render: true,
				     },
				 },
				 "search": {
				     "ajax" : {
					 "url" : "/riskfactors/search/",
					 "data": function (str){
					     return {
						 "operation": "search",
						 "search_str": "str"
					     };
					 }
				     }
				 },
				 "contextmenu": {
				     "items": function(node){
					 return	 {"detail": {
						      "label": "Detail",
						      "action": function(obj){
							  window.location = node.data('detail_url');
						      },
						      "icon": "edit",
						  },
						  "edit": {
						      "label": "Edit",
						      "action": function(obj){
							  window.location = node.data('edit_url');
						      },
						      "icon": "edit",
						  },
						  "add": {
						      "label": "Add",
						      "action": function(obj){
							  window.location = node.data('add_url');
						      },
						      "icon": "add",
						  },
						  "delete": {
						      "label": "Delete",
						      "action": function(obj){
							  window.location = node.data('delete_url');
						      },
						      "icon": "delete",
						  }
						 }
					 },
				     },
				 "type": {
				     "valid_children": "folder",
				     "types": {
					 "default": {
					     "valid_children": "none",
					     "icon": "leaf",
					 },
					 "folder": {
					     "valid_children": ["default", "folder"],
					     "icon": {
						 "image" : "http://static.jstree.com/v.1.0rc/_docs/_drive.png"
					     }
					 }
				     },
				 },
			     });
}

function buildevaldocument(){
    $('#riskfactors').jstree({
				 "plugins": ["themes",
					     "json",
					     "ui",
					     "cookies",
					     "dnd",
					     "types",
					     "search",
					     "hotkeys",
					    ],
				 "json": {
				     "ajax": {
					 "url" : function(n){
					     if(n==-1){
						 return "/riskfactors/node/0/";
					     }
					     // if(n.data){
					     //		 console.log(n.children());
					     //		 console.log(n.data('id'));
					     //		 return "/riskfactors/"+n.data('id')+"/subtree/";
					     // }
					 },
					 progressive_render: true,
				     },
				 },
				 "search": {
				     "ajax" : {
					 "url" : "/riskfactors/search/",
					 "data": function (str){
					     return {
						 "operation": "search",
						 "search_str": "str"
					     };
					 }
				     }
				 },
			     }).bind("select_node.jstree", function (event, data){
					 $.get("eval/" + data.rslt.obj.data("id"),
					       function(data){
						   $("#riskfactorevaluation").html(data);
						   $("#riskevalform").ajaxForm({
										   beforeSubmit: beforeSubmit,
										   success: showResponse,
										   type: 'post'
										   });
						   });
					 });
}


