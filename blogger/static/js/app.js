// Note that the path doesn't matter for routing; any WebSocket
// connection gets bumped over to WebSocket consumers
socket = new WebSocket("ws://" + window.location.host + "/blogger/home/");
socket.onmessage = function(e) {
	var post = e.data.split('~');

	if (post[3] == 'new'){
		var postUser = (post[0][1]+post[0][2]+post[0][3]+post[0][4]);
		var currentUser = $('#user').val();
		$('#new').after(`<hr id="l`+post[2]+`" style="margin: 5px;">`); 
		document.getElementById("new").innerHTML = `<div id="`+post[2]+`" class="col-md-11"> `+post[1]+`</div>
													<div id="n`+post[2]+`" style="float: right;" class="col-md-1">`+post[0]+`</div>`;	
	    if(currentUser==postUser){
	    	$('#new').after(`<div class="row">
	    	<button style="margin: 5px;  float: right; background: white;" class="btn" id="e`+post[2]+`" type="button" onclick="callEdit(`+post[2]+`)">
            <input type="image" src="/static/img/002-edit.png"></button>
            <button style="margin: 5px; float: right; background: white;" id="d`+post[2]+`" type="button" class="btn" onclick="deletePost(`+post[2]+`)">
            <input type="image" src="/static/img/001-rubbish-bin.png"></button> </div>`);
	    }
	    document.getElementById("new").id =  'p'+post[2];
	    document.getElementById("post_body").value = '';  
	    $('#p'+post[2]).before(`<div id="new" class="row"></div>`);  	
	    }

	else if (post[3] == 'edit'){
		var currentUser = $('#user').val();
		var postUser = (post[0][1]+post[0][2]+post[0][3]+post[0][4]);
		if(currentUser != postUser){
			$('div#'+post[2]).html(post[1]);}
		else{
			cancelEdit(post[2]);
			$('div#'+post[2]).html(post[1]);
		}
	}
	
	else if (post[3] == 'delete'){
		var currentUser = $('#user').val();
		var postUser = (post[0][1]+post[0][2]+post[0][3]+post[0][4]);
		if(currentUser != postUser){
			$('#'+post[2]).remove();
			$('#n'+post[2]).remove();
			$('#l'+post[2]).remove();
		}
		else {
			$('#'+post[2]).remove();
			$('#n'+post[2]).remove();
			$('#l'+post[2]).remove();
			$('#e'+post[2]).remove();
			$('#d'+post[2]).remove();
			if (isEdit = true) {
				$(".editpost").remove();
			}
		}
	}					    										
}
//socket.onopen = function() {
//    socket.send("hello");
//}
// Call onopen directly if socket is already open
if (socket.readyState == WebSocket.OPEN) socket.onopen();
$('#addform').on('submit', function(event) {
    var post = {
    	state: 'new',
        body: $('#post_body').val(),
        user: $('#user').val(),
    }
    socket.send(JSON.stringify(post));
    return false;
});


function edited() {
    var post = {
    	state: 'edit',
    	body: $('#afterEdit').val(),
        id: $('#postID').val(),
        user: $('#user').val(),
    }
    socket.send(JSON.stringify(post));
}

function deletePost(postID) {
	var post = {
    	state: 'delete',
    	user: $('#user').val(),
        id: postID,
    }
    socket.send(JSON.stringify(post));	
}

 var isEdit = true;
function callEdit(id){
 	if (isEdit){
 		edit(id); 	
 	}
 	else{
 		cancelEdit(id);
 	}
 }

 function edit(id) {
    var body = $("#"+id);
    postbody = body.html();
    var t = body.text();
    body.replaceWith("<div class='col-md-12 editpost'>"+
    			  "<textarea class='form-control' id='afterEdit' style='height:200px; margin-bottom:30px'>" + t + "</textarea>"+
    			  "<input type='hidden' id='postID' value='"+id+"' />"+
    			  "<div style='float:right'>"+
    			  "<button type='button' class='btn btn-default' onclick='cancelEdit()'>Cancel</button>"+
    			  "<input type='hidden' name='actype' value='edit'>"+
		          " <button type='button' onclick='edited()' class='btn btn-primary'>Edit</button></div></div>");
    isEdit = false;
}

function cancelEdit(id){
	var editpost = $("div.editpost");
	editpost.replaceWith("<div id='"+id+"' class='col-md-11' style='overflow: hide'>"+postbody+"</div>");
	isEdit = true;
}

												