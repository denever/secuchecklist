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
				     }
				 });
}
