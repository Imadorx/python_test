// ====== Daily Challenge 1
let Sentence = "The movie is not that bad, I like it";
let wordnot =Sentence.indexOf("not");
let wordbad = Sentence.indexOf('bad');
if (wordnot != -1 && wordbad != -1 && wordbad > wordnot){
    let result = Sentence.slice(0, wordNot) + "good" + Sentence.slice(wordBad + 3);
    console.log(result);
} else {
    console.log(sentence);
};
// ====== Daily Challenge 2
for (let i =1 ;i<=6 ; i++ ){
  let stars = '';
  for (let j =1 ; j<= i ; j++){
    stars += '*';
  }
  console.log(stars);
}

