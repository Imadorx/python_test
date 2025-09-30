
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let StudentName = prompt("give me your name : ").toLowerCase();
if (StudentName in guestList){
  console.log("Hi! I'm "  + StudentName + " and I'm from " + guestList[StudentName]);
} else { 
  console.log("Hi! I'm a guest.")
}


// exercice 3
let age = [20,5,12,43,98,55];
let sum =0 ;
for (let i=0 ; i<= age.length-1 ; i++){
  sum = age[i] 
  console.log(sum);
}

let max = age[0];
for (let i=0 ; i<= age.length-1 ; i++){
if (max < age[i]){
  max= age[i];
  console.log(max);
}
}