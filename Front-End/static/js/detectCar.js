var carPicFront = document.getElementById("carPicFront");

function whatClicked(evt) {
	console.log(evt.target);
	console.log(evt.target.id);
    alert(evt.target.id);
}

carPicFront.addEventListener("click", whatClicked, false);