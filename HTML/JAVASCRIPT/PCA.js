let count_El = document.getElementById("count_el")
let save_El = document.getElementById("save_el")
let count = 0

function increment(){
  count += 1;
  count_El.textContent = count;
}

function decrease(){
  count -= 1;
  count_El.textContent = count;
}

function save(){
  if (count > 0){
    let prev_en = " - " + count
    save_El.textContent += prev_en
  }
  
  if (count < 0){
    let prev_en0 = "-" + "(" + count + ")"
    save_El.textContent += prev_en0
  }
  count -= count
  count_El.textContent = count
  /* Teachers Example: 
  countEl.textContent = 0
  count = 0 */ 
  /*Leant: JavaScript take notes of the last
  value assigned to a var (count), so the teacher
  reassigned it to 0. but I simply subtracted count
  from itself to get 0*/
  console.log(count)
}

for (let i = 0; i < 10; i++){
  console.log(i)
}

