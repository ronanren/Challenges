function palindrome(str) {
  let str2 = str.replace(/[ \)\(,._-]/gi, "").toLowerCase();
  str = str.replace(/[ \)\(,._-]/gi, "").toLowerCase();
  str2 = str2.slice(Math.round(str2.length/2))
  str2 = str2.split("").reverse().join("");
  if (str.slice(0, str.length/2) === str2){
    return true
  } else 
    return false;
}



palindrome("0_0 (: /-\ :) 0-0");