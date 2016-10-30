
var selectId;

<<<<<<< HEAD
var carPicFront = document.getElementById("carPicFront");
var carPicBack = document.getElementById("carPicBack");

function whatClicked(evt) {
	selectId = evt.target.id;
	if(selectId != "imgFront" && selectId != "imgBack") {
		$('#setValue').modal('show');
	}
=======
    var bumper = $("#passenger_side");
    bumper.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0),
        left: img_w - (bumper.width() / 2) + (img_w * 0.6)
    });

    var fl_light = $("#fl_light");
    fl_light.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0.1),
        left: img_w - (bumper.width() / 2) - (img_w * 0.1)
    });

    var fl_light = $("#fr_light");
    fl_light.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0.0),
        left: img_w - (bumper.width() / 2) - (img_w * 0.85)
    });

    var fl_light = $("#roof");
    fl_light.css({
        top: img_h - (bumper.height() / 2) - (img_h * 0.9),
        left: img_w - (bumper.width() / 2) + (img_w * 0.3)
    });

    var fl_light = $("#front_windscreen");
    fl_light.css({
        top: img_h - (bumper.height() / 2) - (img_h * 0.6),
        left: img_w - (bumper.width() / 2) + (img_w * 0)
    });
}

function update_back() {
    var image = $("#target-back");
    var img_w = image.width() / 2;
    var img_h = image.height() / 2;

    var bumper = $("#back");
    bumper.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0.2),
        left: img_w - (bumper.width() / 2) - (img_w * 0.65)
    });

    var bumper = $("#driver_side");
    bumper.css({
        top: img_h - (bumper.height() / 2) + (img_h * 0),
        left: img_w - (bumper.width() / 2) + (img_w * 0.6)
    });

    var fl_light = $("#bl_light");
    fl_light.css({
        top: img_h - (bumper.height() / 2) - (img_h * 0.2),
        left: img_w - (bumper.width() / 2) - (img_w * 0.2)
    });

    var fl_light = $("#br_light");
    fl_light.css({
        top: img_h - (bumper.height() / 2) - (img_h * 0.2),
        left: img_w - (bumper.width() / 2) - (img_w * 0.85)
    });

    // var fl_light = $("#roof");
    // fl_light.css({
    //     top: img_h - (bumper.height() / 2) - (img_h * 0.9),
    //     left: img_w - (bumper.width() / 2) + (img_w * 0.3)
    // });

    var fl_light = $("#back_windscreen");
    fl_light.css({
        top: img_h - (bumper.height() / 2) - (img_h * 0.7),
        left: img_w - (bumper.width() / 2) - (img_w * 0.3)
    });
>>>>>>> 37580a3472014129189f1294ee9d45781f5c474f
}

carPicFront.addEventListener("click", whatClicked, false);
carPicBack.addEventListener("click", whatClicked, false);

function saveData() {

	info[selectId] = Math.floor(parseFloat($('#rate').swidget().value()) * 10);

	$('#setValue').modal('hide');
}

function generateHTML(firstValue, secondValue) {
	return "<tr><td>" + firstValue + "</td><td>" + secondValue + "</td></tr>";
}

function insertItem(firstValue, secondValue) {
	return {"Damage Parts" : firstValue, "Damage Rating" : secondValue.toString() };
}
			
function addItem() {
	if(Object.keys(info).length < 1) {
		return false;
	}
	else {

		var data = [];
		// $("addItemList").empty();
		
		for(var item in info) {
			// var htmlText = generateHTML(item, info[item]);
			// $("addItemList").append(htmlText);
			data.push(insertItem(item, info[item] / 10.0));
		}

		$('#summarise').dataTable().fnClearTable();
		$('#summarise').dataTable().fnAddData(data);

		return true;
	}
}
