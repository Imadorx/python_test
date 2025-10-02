const form = document.getElementById("libform");
const storySpan = document.getElementById("story");
const shuffleBtn = document.getElementById("shuffle-button");

let currentValues = {};   

const storyTemplates = [
      ({noun, adjective, person, verb, place}) => 
        `One day, ${person} decided to ${verb} with a ${adjective} ${noun} in ${place}.`,
      ({noun, adjective, person, verb, place}) => 
        `In ${place}, a ${adjective} ${noun} forced ${person} to ${verb} all day long.`,
      ({noun, adjective, person, verb, place}) => 
        `${person} found a ${adjective} ${noun} while trying to ${verb} near ${place}.`
    ];

 function generateStory(values) {
      const randomIndex = Math.floor(Math.random() * storyTemplates.length);
      return storyTemplates[randomIndex](values);
    }

form.addEventListener("submit", function(event) {
      event.preventDefault();

      const noun = document.getElementById("noun").value.trim();
      const adjective = document.getElementById("adjective").value.trim();
      const person = document.getElementById("person").value.trim();
      const verb = document.getElementById("verb").value.trim();
      const place = document.getElementById("place").value.trim();

      if (!noun || !adjective || !person || !verb || !place) {
        alert("Please fill in all the fields!");
        return;
      }

      currentValues = { noun, adjective, person, verb, place };

      storySpan.textContent = generateStory(currentValues);

      shuffleBtn.style.display = "inline-block";
    });

    shuffleBtn.addEventListener("click", function() {
      if (Object.keys(currentValues).length > 0) {
        storySpan.textContent = generateStory(currentValues);
      }
    });