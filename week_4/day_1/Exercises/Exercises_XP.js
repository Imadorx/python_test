//Exercise 1 : Scope

// 1
function funcOne() {
    const a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}


funcOne()


//2

let a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}


funcThree() 
funcTwo()   
funcThree() /
//3
function funcFour() {
    window.a = "hello";
}

function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

funcFour() 
funcFive() 

// 4
let a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}


funcSix()

// 5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);


//Exercise 2 :
function winBattle(){
    return true;
}

// 1
const winBattle = () => true;
//2 & 3
let experiencePoints = winBattle() ? 10 : 1;
//4
console.log(experiencePoints);



//Exercise 3 : 
const isString = (value) => typeof value === "string";

console.log(isString('hello')); 
console.log(isString([1, 2, 4, 0])); 
console.log(isString(2378)); 
console.log(isString('monday')); 



//Exercise 4 : 
const sum = (num1, num2) => num1 + num2;
console.log(sum(18, 7));
console.log(sum(6, 9));



//Exercise 5 : 
//1
function kgToGramsdec(kg) {
    return kg * 1000;
}
console.log(kgToGramsdec(6));
//2
const kgToGramsExpr = function(kg) {
    return kg * 1000;
};
console.log(kgToGramsExpr(7));
//4
const kgToGramsArrow = kg => kg * 1000;
console.log(kgToGramsArrow(8)); 



//Exercise 6 
//1
(function(numchildren, partnername, location, job){
//2
    const sentence = `You will be a ${job} in ${location}, and married to ${partnername} with ${numchildren} kids.`;
    const div = document.createElement("div");
    div.textContent = sentence;
    document.body.appendChild(div);
})(1, "gans", "Casa", "Software Engineer");



//Exercise 8 
//Part I
//1
function makeJuice(size) {
    //2:
   function addIngredients (ingredient1, ingredient2, ingredient3){
     const sentence = `The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, ${ingredient3}".`
       
      const p = document.createElement('p');
        p.textContent = sentence;
        document.body.appendChild(p);
   }
   //3:
   addIngredients("apple", "banana", "orange");
  }
  makeJuice("small");

//Part II:
//1
function makeJuice(size) {
    const ingredients = [];
//2
    function addIngredients(ingredient1, ingredient2, ingredient3) {
        ingredients.push(ingredient1, ingredient2, ingredient3);
    }
//3
    function displayJuice() {
        const sentence = `The client wants a ${size} juice, containing ${ingredients.join(', ')}.`;
        const p = document.createElement('p');
        p.textContent = sentence;
        document.body.appendChild(p);
    }
//4
    addIngredients("apple", "banana", "orange");
    addIngredients("strawberry", "mango", "ananas");
    displayJuice();
}

makeJuice("large");