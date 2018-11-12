$(document).ready(function(){
function openMemo(url,type,wt,ht){

		if(wt == undefined){
			wt = 700;
		}
		if(ht == undefined){
			ht = 450;
		}
			$("#modalbox").dialog({

				width:wt,
				height:ht,
				title:type,
				modal:true,
	      	    resizable: false,
	      	   draggable: false,
	      	   closeOnEscape: false,
	      	   close: function(event, ui) {
	      	    $("#modalContent").empty();
				$("#modalbox").dialog("close");
	      	   }
			});


	   	$("#modalContent").load(url,function(){
	  		$("#modalbox").dialog("open");
	   	});

}})