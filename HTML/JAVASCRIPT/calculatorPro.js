let num1 = 8;
let num2 = 12;

document.getElementById("num1_el").textContent = num1;
document.getElementById("num2_el").textContent = num2;

function add(){
  result = num1 + num2;
  document.getElementById("sum_el").textContent += result;
}

function subtract(){
  result = num1 - num2;
  document.getElementById("sum_el").textContent += result;
}

function mult(){
  result = num1 * num2;
  document.getElementById("sum_el").textContent += result;
}

function divide(){
  result = num1 / num2;
  document.getElementById("sum_el").textContent += result;
}