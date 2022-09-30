console.log(isPalindrome("racecar"))

console.log(largestPalindrome("racecar"))

function isPalindrome(str){
    var reverse = "";
    for (var i=0; i<str.length-1; i++){
        reverse += str[i]
    }
    if (str === reverse){
        return true
    } else {
        return false
    }
}

function largestPalindrome(str){
    var subStrings = []
    for (var i=0; i<str.length-1; i++){
        for (var j=0; j<str.length-1; j++){
            subStrings.push(str.substring(i,j))
        }
    }
    for (var k=0; k<subStrings.length-1; k++){
        if (!isPalindrome(subStrings[k])) {
            subStrings.remove(subStrings[a])
        }
    }
    var max = subStrings[0]
    for (var z=0; z<subStrings.length-1; z++){
        if (subStrings[z].length > max.length){
            max = subStrings[z]
        }
    }
    return max
}
