
// rock, paper, scissors game

/*let p_choice = document.getElementById("choices_el").value;*/
let choices = ["rock", "paper", "scissors"];
let result = document.getElementById("result_el");
let lives = 5;

function count_lives() {
  lives -= 1;
  if (lives === 0){
    alert("Game Over")
  }
  
}

let computer = function mk_choice(min, max) {
  let choices_i = Math.floor(Math.random() * (max - min)) + min;
  return choices_i;
}

function p_ChoiceRock() {
  let comp_choice = choices[computer(0, 3)];
  if (comp_choice === "scissors") {
    result.textContent = comp_choice + " " +"Congratulations! You won";
  } else if (comp_choice === "paper") {
    result.textContent = comp_choice + " " +"Oops, You Lose";
  } else { 
    result.textContent = comp_choice + " " + "It's a tie";
  }
}


function p_ChoiceScissors() {
  let comp_choice = choices[computer(0, 3)];
  if (comp_choice === "paper") {
    result.textContent = comp_choice + " " +"Congratulations! You won";
  } else if (comp_choice === "rock") {
    result.textContent = comp_choice + " " +"Oops, You Lose";
  } else { 
    result.textContent = comp_choice + " " + "It's a tie";
  }
}

function p_ChoicePaper() {
  let comp_choice = choices[computer(0, 3)];
  if (comp_choice === "rock") {
    result.textContent = comp_choice + " " + "Congratulations! You won";
  } else if (comp_choice === "scissors") {
    result.textContent = comp_choice + " " + "Oops, You Lose";
  } else { 
    result.textContent = comp_choice + " " + "It's a tie";
  }
}

const bool = 5 < 1

switch (bool) {
  case true:
    console.log("True")
  case false:
    console.log("False")
}
document.write("The barber face get as e be")