var carPicFront = document.getElementById("carPicFront");
var carPicBack = document.getElementById("carPicBack");

function whatClicked(evt) {
    alert(evt.target.id);
}

carPicFront.addEventListener("click", whatClicked, false);
carPicBack.addEventListener("click", whatClicked, false);