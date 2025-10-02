// ===== Exercise 1
    const h1 = document.querySelector("h1");
    console.log(h1);

    const article = document.querySelector("article");
    article.lastElementChild.remove();

    const h2 = document.querySelector("h2");
    h2.addEventListener("click", () => {
      h2.style.backgroundColor = "red";
    });

    const h3 = document.querySelector("h3");
    h3.addEventListener("click", () => {
      h3.style.display = "none";
    });

    const button = document.getElementById("boldBtn");
    button.addEventListener("click", () => {
      const paragraphs = document.querySelectorAll("article p");
      paragraphs.forEach(p => {
        p.style.fontWeight = "bold";
      });
    });

    h1.addEventListener("mouseover", () => {
      const randomSize = Math.floor(Math.random() * 101);
      h1.style.fontSize = randomSize + "px";
    });

    const secondParagraph = document.querySelectorAll("article p")[1];
    secondParagraph.addEventListener("mouseover", () => {
      secondParagraph.classList.add("fade");
    });
// ===== Exercise 2
let form = document.querySelector("form");
console.log(form)

let input_01 = document.getElementById("fname");
console.log(input_01)

let input_02 = document.getElementById("lname");
console.log(input_02)

let input_1 = document.getElementsByName("firstname");
console.log(input_1)

let input_2 = document.getElementsByName("lastname");
console.log(input_2)

/////////////////
const form = document.querySelector("form");
const  usersAnswer = document.querySelector(".usersAnswer");

form.addEventListener("submit", function(event){
event.preventDefault();
})
 const inputs = document.querySelectorAll("input[type='text']");
inputs.forEach(input =>{
  if(input.value.trim() !== ""){
    const li = document.createElement('li');
    li.textContent = input.value
   usersAnswer.appendChild(li);
   input.value = "" ;
  }
  
})


// ===== Exercise 3

let allBoldItems ;
 function getBoldItems(){
allBoldItems = document.querySelectorAll("strong");
  console.log(allBoldItems);
 }
 function highlight() {
  getBoldItems(); // make sure we collected them first
  allBoldItems.forEach(item => {
    item.style.color = "blue";
  });
}

function highlight() {
  getBoldItems(); t
  allBoldItems.forEach(item => {
    item.style.color = "blue";
  });
}

function returnItemsToDefault(){
    getBoldItems(); 
  allBoldItems.forEach(item => {
    item.style.color = "black";
  });
}

const paragraph = document.getElementById("text");

paragraph.addEventListener("mouseover", highlight);
paragraph.addEventListener("mouseout", returnItemsToDefault);

// ===== Exercise 4

  function calculateVolume(event) {
      event.preventDefault(); 

      let radius = document.getElementById("radius").value;
      radius = parseFloat(radius);

      if (isNaN(radius) || radius <= 0) {
        document.getElementById("volume").value = "Invalid radius!";
        return;
      }

      let volume = (4/3) * Math.PI * Math.pow(radius, 3);


      document.getElementById("volume").value = volume.toFixed(2);
    }
    document.getElementById("MyForm").addEventListener("submit", calculateVolume);
