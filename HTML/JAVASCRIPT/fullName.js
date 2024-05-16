/*
let fname = document.getElementById("fName");
let lname = document.getElementById("lName");
let output = document.getElementById("output");
let getResult = document.getElementById("getResult_btn");

function func(){
  let FullName = fname + lname;
  output.innerHTML = FullName;
 
}
*/

/*const profile = { name : "Osborn", age : "20", course: "Computer Science", hobbies : ['gaming', 'coding', 'watching movies'], myFunc : function() { alert("I'm a function in an object")}
  }

const strlen = profile["name"];

console.log(strlen.length)*/

//let c_passwd = getElementById("c_passwd")

//const password =  

function readAge(){
  const age = document.getElementById("inputAge");
  const input_value = age.value;
  
  if (input_value < 18){
    console.log("You are too young to enter");
    alert("You are too young to enter");
  }
  else if (input_value > 99) {
    alert("You are too old to join")
  }
  else{
    console.log("Welcome to the CLUB");
    alert("Welcome to the CLUB");
  }
}