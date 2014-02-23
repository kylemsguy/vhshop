var count = 1;

function show_coords(event)
  {
  var elem = document.getElementById("clicker");
  var offset = $(elem).offset();
  var x = event.clientX - offset.left;
  var y = event.clientY - offset.top;
  switch (count)
  {
	case 1: 
		var tid = "set1";
		break;
	case 2: 
		var tid = "set2";
		break;
	case 3: 
		var tid = "set3";
		break;
	case 4: 
		var tid = "set4";
		break;
	default:
		var tid = "null";
		break;
	}
	//document.getElementById(tid).value = "X coords: " + x + ", Y coords: " + y;
	document.getElementById(tid).value =  x + "," + y;
	count += 1;
  //alert("X coords: " + x + ", Y coords: " + y);
  }
  
 function undo(event)
 {
	$('button').on('click', function() 
	{
		var hid = this.id;
		switch (hid)
	{
		case "b1":
			count = 1;
			var fid = "set1";
			break;
		case "b2":
			count = 2;
			var fid = "set2";
			break;
		case "b3":
			count = 3;
			var fid = "set3";
			break;
		case "b4":
			count = 4;
			var fid = "set4";
			break;
		default:
			break;
	}
	document.getElementById(fid).value = "Cleared"; //"lol";
	});
}


