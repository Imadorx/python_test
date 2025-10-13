let persone ={
  FullName: "imad eddine kaaouane",
  Mass: 95 ,
  Height : 178,
Bmi: function() {
    return this.Mass / (this.Height * this.Height);
  }
};


let personeOne ={
  FullName: "sami hilal",
  Mass: 80 ,
  Height : 175
  Bmi: function() {
    return this.Mass / (this.Height * this.Height);
  }
};

// exercice 2

function calculateAverage(gradesList) {
  let sum = 0;
  for (let i = 0; i < gradesList.length; i++) {
    sum += gradesList[i];
  }
  return sum / gradesList.length;
}

function findAvg(gradesList) {
  let average = calculateAverage(gradesList);
  console.log("Average:", average);

  if (average > 65) {
    console.log("You passed!");
  } else {
    console.log("You failed and must repeat the course");
  }
}


findAvg([80, 90, 70]); 
findAvg([50, 60, 55]); 
