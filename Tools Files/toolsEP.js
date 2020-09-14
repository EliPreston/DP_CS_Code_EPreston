// Function isEven takes an integer (a >=0) and returns True if even, and False if odd
function isEven(a) {
  if (a % 2 == 0) {
    return true;
  }
  return false;
}

// Test cases for function isEven
for (i = 0; i < 100; i = i + 1) {
  console.log(isEven(i));
}

// Function sumDigits adds the digits of an integer together
function sumDigitsA(a) {
  total = 0;

  while (a > 0) {
    total = total + (a % 10);
    a = parseInt(a / 10);
  }
  return total;
}

// Testing sumDigitsA
console.log(sumDigitsA(123));
console.log(sumDigitsA(13728));

// sumDigitsB doesn't work, error is in the for statement
// function sumDigitsB(a) {
//   var a = toString(a);

//   var total = 0;

//   for (i = 0; length(a); i = i++) {
//     var x = a[i];
//     total = total + parseInt(x);
//   }

//   return total;
// }

// console.log(sumDigitsB(123));
