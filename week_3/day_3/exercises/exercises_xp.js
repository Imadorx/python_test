// exercice 1  

function displayNumbersDivisible() {
  NumbersDivisible = [];
    for (let i = 0 ; i <= 500 ; i++){
      if (i % 23 == 0 ){
         NumbersDivisible.push(i);
      }
    }
     let sum = 0 ;
   for (let number of NumbersDivisible){
    sum += number ;
   }
       console.log(NumbersDivisible);
       console.log(sum);

}
 
displayNumbersDivisible()

// Bounes


function displayNumbersDivisible(n) {
  NumbersDivisible = [];
    for (let i = 0 ; i <= 500 ; i++){
      if (i % n == 0 ){
         NumbersDivisible.push(i);
      }
    }
     let sum = 0 ;
   for (let number of NumbersDivisible){
    sum += number ;
   }
       console.log(NumbersDivisible);
       console.log(sum);

}
 
displayNumbersDivisible(3)


// exercice 2
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
console.log(stock);

shoppingList = ["banana", "orange",  "apple"];
function myBill (){
  let sum = 0;
  for ( let i of shoppingList){
    if (i in stock && stock[i] !== 0 ){
     sum += prices[i];
     stock[i] -= 1 ;
    }
  }
  console.log(sum);
}
myBill();
console.log(stock);


// EXERCICE 3
function changeEnough(itemPrice, amountOfChange) {

  const coinValues = [0.25, 0.10, 0.05, 0.01];


  let totalChange = 0;
  for (let i = 0; i < amountOfChange.length; i++) {
    totalChange += amountOfChange[i] * coinValues[i];
  }

  return totalChange >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0])); 
console.log(changeEnough(14.11, [2, 100, 0, 0])); 
console.log(changeEnough(0.75, [0, 0, 20, 5]));   

// exercice 4

function hotelCost(){
 let nights ;
 while(true){
  nights = prompt("How many nights would you like to stay in the hotel?");
  if (nights !== null && !isNaN(nights) &&  nights.trim() !== ""){
  nights = Number(nights);
  break ;

 } else{
  alert("Please enter a valid number of nights.");
 }
}
  let cost = nights * 140;
  return cost;
}

let total = hotelCost();
console.log(total);


function planeRideCost(){
  let destination ;
  while(true){
    destination = prompt("where are you going") ;
    if(destination !== null && destination.trim() !== ""){
      destination = destination.toLowerCase() ;
      break;
    }else{
      alert("Please enter a valid destination.");
    }
      }
      let price ;
      if (destination === "london"){
        price = "183$";
      }if (destination === "paris"){
         price = "220$";
      }else {
        price = "300$";
      }
      return price ;
};

let destinationPrice = planeRideCost() ;
console.log("your price depending on the location is : $" + destinationPrice );


function rentalCarCost() {
  let numberOfDays;
  while(true){
  numberOfDays = prompt("give me the number of days they would like to rent the car.");
  if(numberOfDays !== null && !isNaN(numberOfDays) && numberOfDays.trim() !== ""){
    numberOfDays = Number(numberOfDays);
    break;
  }else {
    alert("Please enter a valid number of days ");
  }
  };
  let cost ;
  if (numberOfDays >= 10 ){
    cost =( numberOfDays * 40 ) - 2
  }if (numberOfDays < 10){
    cost = numberOfDays * 40
  }
  return cost ;
}
 console.log(rentalCarCost());

function totalVacationCost(){
   let total = hotelCost();
   let destinationPrice = planeRideCost() ;
   let rentalCost = rentalCarCost()

  console.log(
    `The car cost: $${rentalCost}, the hotel cost: $${total}, the plane tickets cost: $${destinationPrice}`
  ); }

// Exercice 5

// <!-- <!DOCTYPE html>
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>Exercice 5</title>
// </head>
// <body>
//     <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>
// <script>
// div = document.getElementById("container");
// console.log(div)
// let changeName = document.querySelectorAll(".list");
// changeName[0].children[1].textContent="Richard";
// changeName[1].children[1].remove();
// for(let ul of changeName){
// ul.children[0].textContent="Imad";
// }
// let lists = document.guerySelectorAll("ul");
// lists.forEach(ul =>{
//   ul.classlist.add("student_list");
// });
// lists[0].classlist.add("university", "attendance");

// console.log(lists[0]);
// console.log(lists[1]);

// let changeColor = document.getElementById("container")
// changeColor.style.backgroundColor = "lightblue";
// changeColor.style.padding = "10 px" ;

// let secondUl = document.querySelectorAll("ul")
// let lastLi = secondUl.lastElementChild;
// if (lastLi.textContent.trim()=== "Dan"){
//     lastLi.style.display = "none";
// }

// let changeBorder = document.querySelectorAll("li");
//  changeBorder.forEach(li =>{
//     if(li.textContent.trim() === "Richard"){
//         li.style.border ="2px solid black";
//     }
//  });
// document.body.style.fontSize = "20px";
// </script>
// </body>
// </html> -->


//  exercice 6 


// <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>
// <script>
//     let changeDiv= document.getElementById("navBar");
//     changeDiv.setAttribute("id","socialNetworkNavigation");
//     let newLi = document.querySelectorAll(ul);
//     newLi.createElement(li)
//     /////////////////////////////
//     let ul = document.querySelector('ul')
//     let Li = document.createElement("li");
//     Li.textContent ="new item";
//     ul.appendChild(li);
//     // :::::::::
//  ul = document.querySelector("ul");
//  newLi = document.createElement("li");
// let textNode = document.createTextNode("Logout");
// newLi.appendChild(textNode);
// ul.appendChild(newLi);
// console.log(ul);
// // :::::::::
//  ul = document.querySelector("ul");
// let firstLi = ul.firstElementChild;
// let lastLi = ul.lastElementChild;
// console.log("First <li> text:", firstLi.textContent);
// console.log("Last <li> text:", lastLi.textContent);

// </script>

EXERCICE 7


    let allBooks = [BookOne={
        title : "knson",
        author : "qfzvlnol",
        image : " kfj vmjl ml m",
        alreadyRead : false 
    },
    BookTow={
        title : "rrkoen",
        author : "kzvnkp",
        image : " kfjkonpknpnmlm",
        alreadyRead : false 
    }
]

let add = document.getElementsByClassName('listBooks');
add.createElement('div')



