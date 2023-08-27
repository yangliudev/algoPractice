//Reverse a string

s = 'hello';

function reverseStr(s) {
    let splitString = str.split("");
    let reverseArray = splitString.reverse();
    let joinArray = reverseArray.join("");
    return joinArray
};

console.log(reverseStr(s))
