function pali(array){
    array = array.toUpperCase()
    
    for(let i=0; i<array.length; i++){
        if( array[i] !== array[array.length - 1 - i]){
            return false
        }
        else{
            return true
        }
    }
}


console.log(pali("anitalaValaina"))