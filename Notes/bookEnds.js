var test1 = [1, 2, 10, 11, 12, 15, 30, 31, 35]

function bookEnds(num){
    var temp = num[0];
    var str = "";
    for (var i=0; i<num.length; i++){
        if (num[i+1]-num[i]===1){
            continue
        } else {
            if (num[i] === temp){
                str += temp
                if (i === num.length-1){
                    continue
                } else {
                    str += ","
                    temp = num[i+1]
                }
            } else {
                str += temp
                str += "-"
                str += num[i]
                str += ","
                temp = num[i+1]
            }
        }
    }
    console.log(str)
} 

bookEnds(test1)