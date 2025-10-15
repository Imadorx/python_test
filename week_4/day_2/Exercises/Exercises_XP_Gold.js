// ex1 :
//output :
// [2, 4, 6]

// map() loops over each element (1, 2, 3).

// For each number, it checks typeof num === 'number', which is true,
// so it returns num * 2.

// The return; part is never used here, because all elements are numbers.

// Final array: [2, 4, 6].

// ex2 :
//output :
// [1, 2, 0, 1, 2, 3]

// Initial value of accumulator acc = [1, 2]

// First iteration:
// acc = [1, 2], cur = [0, 1]
//  acc.concat(cur) = [1, 2, 0, 1]

// Second iteration:
// acc = [1, 2, 0, 1], cur = [2, 3]
//  [1, 2, 0, 1, 2, 3]

// ex3 :
// Values of i: 0, 1, 2, 3, 4, 5

// ex4 :

const array = [[1],[2],[3],[[[4]]],[[[5]]]];
const result = array.flat(2);
console.log(result); // [1, 2, 3, [4], [5]]

const result = [[1],[2],[3],[[[4]]],[[[5]]]].flat(2);

const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]];
const joined = greeting.map(words => words.join(" "));
console.log(joined);
// ["Hello young grasshopper!", "you are", "learning fast!"]

const sentence = joined.join(" ");
console.log(sentence);
// "Hello young grasshopper! you are learning fast!"

const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]];
const result = trapped.flat(Infinity);
console.log(result); // [3]
