//validation used in contact.html for all data input fields

function checkFields() {
    var x = document.forms["formName"]["inputName"].value;
    if (x == "") {
        alert("Please fill out this field")
        return false;
        
    var z = document.forms["formName"]["inputEmail"].value;
    if (z == "") {
        alert("Please fill out this field")
        return false;
    }
    
    var y = document.forms["formName"]["inputMes"].value;
    if (y == "") {
        alert("Please fill out this field")
        return false;
    }
    }
}
