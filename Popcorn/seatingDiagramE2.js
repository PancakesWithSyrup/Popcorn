"use strict";
function Space (divID, spaceName, occupied, redID, greenID, orangeID) {
	this.divID = divID;
	this.spaceName = spaceName;
	this.occupied = occupied;
	this.redID = redID;
	this.greenID = greenID;
	this.orangeID = orangeID;
}

var e1 = new Space("e1", "COMP51", false, "e1Red", "e1Green", "e1Orange");
var e2 = new Space("e2", "COMP52", false, "e2Red", "e2Green", "e2Orange");

var d1 = new Space("d1", "COMP41", false, "d1Red", "d1Green", "d1Orange");
var d2 = new Space("d2", "COMP42", false, "d2Red", "d2Green", "d2Orange");

var c1 = new Space("c1", "COMP31", false, "c1Red", "c1Green", "c1Orange");
var c2 = new Space("c2", "COMP32", false, "c2Red", "c2Green", "c2Orange");

var b1 = new Space("b1", "COMP21", false, "b1Red", "b1Green", "b1Orange");
var b2 = new Space("b2", "COMP22", false, "b2Red", "b2Green", "b2Orange");

var a1 = new Space("a1", "COMP11", false, "a1Red", "a1Green", "a1Orange");
var a2 = new Space("a2", "COMP12", false, "a2Red", "a2Green", "a2Orange");


console.log(document.getElementById("e1Red").style.display);
function occupancyStatus(spaceID) {
	//If the spaceName is null then nothing will show in the box for that space
	if (spaceID.spaceName == null) {
		document.getElementById(spaceID.orangeID).style.display = "none";
		document.getElementById(spaceID.greenID).style.display = "none";
		document.getElementById(spaceID.redID).style.display = "none";
		document.getElementById(spaceID.divID).style.display = "none";
		console.log(spaceID.spaceName);
	// else the spaceName of the object is published and then the corresponding color image as well
	} else {
		document.getElementById(spaceID.divID).innerHTML = spaceID.spaceName;
		if (spaceID.occupied == true) {
		document.getElementById(spaceID.orangeID).style.display = "none";
		document.getElementById(spaceID.greenID).style.display = "none";
		document.getElementById(spaceID.redID).style.display = "block";
		} else if (spaceID.occupied == false) {
		document.getElementById(spaceID.orangeID).style.display = "none";
		document.getElementById(spaceID.greenID).style.display = "block";
		document.getElementById(spaceID.redID).style.display = "none";
		}
	}
}
// Methods invoked to perform the logic of the HTML	
occupancyStatus(e1);
occupancyStatus(e2);

occupancyStatus(d1);
occupancyStatus(d2);

occupancyStatus(c1);
occupancyStatus(c2);
;
occupancyStatus(b1);
occupancyStatus(b2);

occupancyStatus(a1);
occupancyStatus(a2);
