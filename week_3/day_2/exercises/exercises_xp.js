const people = ["Greg", "Mary", "Devon", "James"];
console.log(people);
console.log(people.shift())
console.log (people[2]="jason");
console.log(people);
console.log (people.push("imad"));
console.log(people);
console.log(people.indexOf("Mary"));
const newPeople = people.slice(1,3);
console.log(newPeople);
console.log(newPeople.indexOf('foo'));
// 6 :  JavaScript returns -1 to signal “not found”.
let last = newPeople[1];
console.log(last)

// part 2
for (let i = 0 ; i<= people.length-1 ; i++){
    console.log(people[i])
}



for(let i=0 ; i<= people.length-1 ; i++){
    console.log(people[i])
    if (people[i]= "devon"){
        break;
    }

}

// exercice 2

const colors =[ "red" , "blue" , "green" , "yellow" , "purpel"];
for (let i=0 ; i<= colors.length-1 ; i++){
    console.log( "My " + (i + 1 )+ " choice is " +  colors[i]);
}


// Exercise 3 

let number = prompt('give me a number');
number = Number(number);
console.log("Type is:", typeof number);

while (number < 10) {
  number = prompt("Number is too small, please enter a new number");
  number = Number(number);
}

// Exercice 4

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor);
console.log(building.numberOfAptByFloor.thirdFloor);
console.log(building.nameOfTenants[1]);
console.log(building.numberOfRoomsAndRent.dan[0])

const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
    console.log("Dan's rent increased to:", building.numberOfRoomsAndRent.dan[1]);
} else {
    console.log("No change in Dan's rent:", danRent);
}


// Exercice 5
const family = {
  father: "Ahmed",
  mother: "Fatima",
  son: "Youssef",
  daughter: "Sara",
};

for (let key in family) {
  console.log(key);
}
for (let key in family) {
  console.log(family[key]);
}

// Exercice 6
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
};

let sentence = "";

for (let key in details) {
  sentence += key + " " + details[key] + " ";
}

console.log(sentence.trim());
// Exercice 7

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

const firstLetters = names.map(name => name[0]);
firstLetters.sort();
const secretName = firstLetters.join('');

console.log(secretName);

