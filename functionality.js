var numberOfIps = 0;

function login() {
	var username = document.getElementById("user").value;
	var password = document.getElementById("pw").value;

	if(username == "admin" && password == "admin") {
		document.getElementById("demo").style.color = "green";
		document.getElementById("demo").innerHTML = "ACCESS GRANTED";

		document.getElementById("login").innerHTML = "";

        document.getElementById("plusBtn").style.display = "block";
        document.getElementById("saveBtn").style.display = "block";

        displayIPList();            
	}
    else {
		document.getElementById("demo").style.color = "red";
		document.getElementById("demo").innerHTML = "ACCESS DENIED";
	}
}   

function addFields(title, index) {
    if(title != "") {
        var newdiv = document.createElement('div');
        newdiv.innerHTML = "<input type='text' id='field" + index + "' value='" + title + "'>";
        document.getElementById("ipForm").appendChild(newdiv);
    } 
}

function addEmptyField() {
    numberOfIps++;

    var newdiv = document.createElement('div');
    newdiv.innerHTML = "<input type='text' id='field" + numberOfIps + "'>";
    document.getElementById("ipForm").appendChild(newdiv);
}

function displayIPList() {
    numberOfIps = ips.length-1

    for (var i = 0; i < ips.length; i++) {
        addFields(ips[i], i);
    }
}	

function save() {
    var result = "var ips =[\n";

    for (var i = 0; i <= numberOfIps; i++) {

        var id = "field" + i;
        result += "\"" + document.getElementById(id).value + "\"";
        if(i != numberOfIps) {
            result += ",\n"
        }
    }
    result += "\n];";


    var newdiv = document.createElement('div');
    newdiv.innerHTML = "<input type='text' id='ips" + result + "'>";
    document.getElementById("submitForm").appendChild(newdiv);

    document.getElementById("submitForm").submit();
}
