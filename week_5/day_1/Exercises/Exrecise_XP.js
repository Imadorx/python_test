//Exercise 1 
const compareToTen = (num) => {
    return new Promise((resolve, reject) => {
    if (num < 10) {
        resolve(`${num} is less than 10`);
    } else if (num === 10) {
        resolve(`${num} is equal to 10`);
    } else {
        reject(`${num} is greater than 10`);
    } 
});
};

compareToTen(15)
  .then(result => console.log(result))
  .catch(error => console.log(error))


compareToTen(8)
  .then(result => console.log(result))
  .catch(error => console.log(error))

compareToTen(10)
  .then(result => console.log(result))
  .catch(error => console.log(error))

//Exercise 2 
function Success() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("success");
    }, 4000);
  });
}

//Exercise 3 

const resolvedPromise = Promise.resolve(3);
const rejectedPromise = Promise.reject("Boo!");

resolvedPromise
  .then(value => console.log("Resolved:", value))
  .catch(error => console.log("Error:", error));

rejectedPromise
  .then(value => console.log("Resolved:", value))
  .catch(error => console.log("Rejected:", error));