function Space (divID, spaceName, occupied, redID, greenID, orangeID) {
	this.divID = divID;
	this.spaceName = spaceName;
	this.occupied = occupied;
	this.redID = redID;
	this.greenID = greenID;
	this.orangeID = orangeID;
}

var e1 = new Space("e1", null, false, "e1Red", "e1Green", "e1Orange");
var e2 = new Space("e2", null, false, "e2Red", "e2Green", "e2Orange");
var e3 = new Space("e3", null, false, "e3Red", "e3Green", "e3Orange");
var e4 = new Space("e4", null, false, "e4Red", "e4Green", "e4Orange");
var e5 = new Space("e5", null, false, "e5Red", "e5Green", "e5Orange");
var e6 = new Space("e6", null, false, "e6Red", "e6Green", "e6Orange");
var d1 = new Space("d1", null, false, "d1Red", "d1Green", "d1Orange");
var d2 = new Space("d2", null, false, "d2Red", "d2Green", "d2Orange");
var d3 = new Space("d3", null, false, "d3Red", "d3Green", "d3Orange");
var d4 = new Space("d4", null, false, "d4Red", "d4Green", "d4Orange");
var d5 = new Space("d5", null, false, "d5Red", "d5Green", "d5Orange");
var d6 = new Space("d6", null, false, "d6Red", "d6Green", "d6Orange");
var c1 = new Space("c1", "COMP31", false, "c1Red", "c1Green", "c1Orange");
var c2 = new Space("c2", "COMP32", false, "c2Red", "c2Green", "c2Orange");
var c3 = new Space("c3", "COMP33", false, "c3Red", "c3Green", "c3Orange");
var c4 = new Space("c4", "COMP34", false, "c4Red", "c4Green", "c4Orange");
var c5 = new Space("c5", "COMP35", false, "c5Red", "c5Green", "c5Orange");
var c6 = new Space("c6", "COMP36", false, "c6Red", "c6Green", "c6Orange");
var b1 = new Space("b1", "COMP21", false, "b1Red", "b1Green", "b1Orange");
var b2 = new Space("b2", "COMP22", false, "b2Red", "b2Green", "b2Orange");
var b3 = new Space("b3", "COMP23", false, "b3Red", "b3Green", "b3Orange");
var b4 = new Space("b4", "COMP24", false, "b4Red", "b4Green", "b4Orange");
var b5 = new Space("b5", "COMP25", false, "b5Red", "b5Green", "b5Orange");
var b6 = new Space("b6", null, false, "b6Red", "b6Green", "b6Orange");
var a1 = new Space("a1", null, false, "a1Red", "a1Green", "a1Orange");
var a2 = new Space("a2", "COMP12", false, "a2Red", "a2Green", "a2Orange");
var a3 = new Space("a3", "COMP13", false, "a3Red", "a3Green", "a3Orange");
var a4 = new Space("a4", "COMP14", false, "a4Red", "a4Green", "a4Orange");
var a5 = new Space("a5", null, false, "a5Red", "a5Green", "a5Orange");
var a6 = new Space("a6", null, false, "a6Red", "a6Green", "a6Orange");

console.log(document.getElementById("e1Red").style.display);
function occupancyStatus(spaceID) {
	if (spaceID.spaceName == null) {
		document.getElementById(spaceID.orangeID).style.display = "none";
		document.getElementById(spaceID.greenID).style.display = "none";
		document.getElementById(spaceID.redID).style.display = "none";
		document.getElementById(spaceID.divID).style.display = "none";
	} else {
		document.getElementById(spaceID.divID).innerHTML = spaceID.spaceName;
		if (spaceID.occupied == true) {
			document.getElementById(spaceID.orangeID).style.display = "none";
			document.getElementById(spaceID.greenID).style.display = "none";
			document.getElementById(spaceID.redID).style.dislay = "block";
		} 
		if (spaceID.occupied == false) {
			document.getElementById(spaceID.orangeID).style.display = "none";
			document.getElementById(spaceID.greenID).style.display = "block";
			document.getElementById(spaceID.redID).style.display = "none";
		}
	}
}
	
occupancyStatus(e1);
occupancyStatus(e2);
occupancyStatus(e3);
occupancyStatus(e4);
occupancyStatus(e5);
occupancyStatus(e6);
occupancyStatus(d1);
occupancyStatus(d2);
occupancyStatus(d3);
occupancyStatus(d4);
occupancyStatus(d5);
occupancyStatus(d6);
occupancyStatus(c1);
occupancyStatus(c2);
occupancyStatus(c3);
occupancyStatus(c4);
occupancyStatus(c5);
occupancyStatus(c6);
occupancyStatus(b1);
occupancyStatus(b2);
occupancyStatus(b3);
occupancyStatus(b4);
occupancyStatus(b5);
occupancyStatus(b6);
occupancyStatus(a1);
occupancyStatus(a2);
occupancyStatus(a3);
occupancyStatus(a4);
occupancyStatus(a5);
occupancyStatus(a6);