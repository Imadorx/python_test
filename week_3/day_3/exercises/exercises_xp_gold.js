// exercice 1
function isBlank(str) {
  return str.trim().length === 0;
}

console.log(isBlank(''));      
console.log(isBlank('abc'));   
console.log(isBlank('   '));   

// exercice 2
function abbrevName(str) {
  let parts = str.split(" "); 
  if (parts.length > 1) {
    return parts[0] + " " + parts[1][0] + ".";
  }
  return parts[0]; 
}

console.log(abbrevName("Robin Singh")); 
console.log(abbrevName("Imad Kaaouane")); 
console.log(abbrevName("Mona")); 
// exercice 3
function swaps (str){
    let result = "";
    for (let char of str){
        if (char === char.toUpperCase()){
            result += char.toLowerCase();
        } else {
            result += char.toUpperCase();
        }
    }
      return result;
}
console.log(swapCase("The Quick Brown Fox")); 

// exercice 4

function isOmnipresent(arr, val) {
  for (let sub of arr) {
    if (!sub.includes(val)) {
      return false; 
    }
  }
  return true; 
}

console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1));
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6)); 

// exercice 5

let table = document.body.firstElementChild;

for (let i = 0; i < table.rows.length; i++) {
  table.rows[i].cells[i].style.backgroundColor = 'red';
}
