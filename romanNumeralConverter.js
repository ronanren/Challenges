function convertToRoman(num) {
    let res = "";
    let roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", 
                 "XC", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", "M", "MM", "MMM"];
    let decimal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 
                   300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000]
    for(let i = 30; i > 0; i--){
        if (num/decimal[i-1] >= 1){
            num = num - decimal[i-1];
            res = res + roman[i-1];
        }
    }
    return res;
}

convertToRoman(3999);