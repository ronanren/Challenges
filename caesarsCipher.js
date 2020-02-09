function rot13(str) {
  let res = "";
  let rot = "NOPQRSTUVWXYZABCDEFGHIJKLM";
  for(let i = 0; i < str.length; i++){
    if (rot.includes(str[i]))
      res += rot.charAt(str[i].charCodeAt(0) - 65);
    else if (str[i] == " ")
      res += " ";
    else 
      res += str[i];
  }
  return res;
}

rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.");