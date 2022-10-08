function rotateStr(str,amt){
    let length = str.length
    let letters = str.split('')
    let empty = []
    for (let i=0; i<length; i++){
        empty.push('')
    }
    for (let j=0; j<length; j++){
        empty[(j+amt)%length]=letters[j]
    }
    return empty.join('')
}

function isRotated(str1, str2){
    let length = str1.length
    let combos = []
    for (let i=0; i<length; i++){
        
    }
}

var example1 = "ABCD"
var example2 = "DABC"

console.log(isRotated(example1, example2))