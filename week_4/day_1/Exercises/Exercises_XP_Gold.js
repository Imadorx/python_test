//Exercise 1 
let landscape = function() {

 let result = "";

 let flat = function(x) {
   for(let count = 0; count<x; count++){
     result = result + "_";
   }
 }

 let mountain = function(x) {
   result = result + "/"
   for(let counter = 0; counter<x; counter++){
     result = result + "'"
   }
   result = result + "\\"
 }

 flat(4);
 mountain(4);
 flat(4)

 return result;
}

landscape();


//2
const landscape = () => {

  let result = "";
  const flat = x => {
    for (let count = 0; count < x; count++) {
      result += "_";
    }
  };

  const mountain = x => {
    result += "/";
    for (let counter = 0; counter < x; counter++) {
      result += "'";
    }
    result =result + "\\";
  };

  flat(4);
  mountain(4);
  flat(4);

  return result;
};

landscape();



//Exercise 2 
const addTo = x => y => x + y;
const addToTen = addTo(10);
addToTen(3);



//Exercise 3 
const curriedSum = (a) => (b) => a + b
curriedSum(30)(1)
/


//Exercise 4 

const curriedSum = (a) => (b) => a + b
const add5 = curriedSum(5)
add5(12)


//Exercise 5 

const compose = (f, g) => (a) => f(g(a));
const add1 = (num) => num + 1;
const add5 = (num) => num + 5;
compose(add1, add5)(10)