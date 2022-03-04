//Determine if a string is a palindrome WITHOUT string slicing or using libraries

let s = 'racecar';

function palindrome(s) {
    i = 0
    j = s.length
    for (i; i < j; i++) {
        if (s[i] == j[i]) {
            i++
            j--
        }
        else {
            return false
        }
    }

};

console.log(palindrome(s));