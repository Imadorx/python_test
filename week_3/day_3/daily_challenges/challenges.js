// ====== Daily Challenge 1
const planets = [
  { name: "Mercury", color: "gray", moons: 0 },
  { name: "Venus", color: "orange", moons: 0 },
  { name: "Earth", color: "blue", moons: 1 },
  { name: "Mars", color: "red", moons: 2 },
  { name: "Jupiter", color: "brown", moons: 79 },
  { name: "Saturn", color: "goldenrod", moons: 82 },
  { name: "Uranus", color: "lightblue", moons: 27 },
  { name: "Neptune", color: "purple", moons: 14 }
];

const section = document.querySelector(".listPlanets");

planets.forEach(planet => {
  const planetDiv = document.createElement("div");
  planetDiv.classList.add("planet");
  planetDiv.style.backgroundColor = planet.color;
  planetDiv.textContent = planet.name; 

  for (let i = 0; i < planet.moons; i++) {
    const moon = document.createElement("div");
    moon.classList.add("moon");
    moon.style.top = `${Math.random() * 80}px`;
    moon.style.left = `${Math.random() * 80}px`;
    planetDiv.appendChild(moon);
  }
  section.appendChild(planetDiv);
});

// ====== Daily Challenge 2

let input = prompt("Give me some words separated by commas:");
let words = input.split(",").map(word => word.trim());
let maxLenght = 0 ;
for (let word of words){
    if(word.length > maxLenght ){
        maxLenght= word.length;
    }
}
console.log("*".repeat(maxLenght + 4));

for(let word of words){
let space = " ".repeat(maxLenght - word.length);
console.log(`* ${word}${space} *`);
}


console.log("*".repeat(maxLenght + 4));
