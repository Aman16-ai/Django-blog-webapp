function check() {
    let Username = document.getElementById('name_in').value;
    let password = document.getElementById('exampleInputPassword1').value;
    if((Username == "" || Username == " ") && (password == "" || password == " ")) {
        alert("Username and password must be provided");
        return false;
    }
    else if(Username == "" || Username == " ") {
        alert("Username must be entered");
        return false;
    }
    else if(password == "" || password == " ") {
        alert("Password must be entered");
        return false;
    }
    else {
        return true;
    }

}