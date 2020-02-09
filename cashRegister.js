function checkCashRegister(price, cash, cid) {
  var change = {};
  var savecid = []; 
  for(let i = 0; i <= 8; i++){
    savecid.push(cid[i].slice(0));
  }
  
  change.status = "OPEN";
  change.change = [];
  var prix = cash - price;
  var currency = [0.01, 0.05, 0.1, 0.25, 1, 5, 10, 20, 100];
  for(let i = 8; i >= 0; i--){
    if (prix > currency[i]){
        if (currency[i] * Math.floor(prix / currency[i]) <= cid[i][1]){
          change.change.push([cid[i][0], currency[i] * Math.floor(prix / currency[i])]);
          prix -= currency[i] * Math.floor(prix / currency[i]);
          cid[i][1] = 0;
        } else {
          change.change.push([cid[i][0], cid[i][1]]);
          prix -= cid[i][1];
        }
        
    }
    prix = Math.round(prix*100)/100;
  }
  if (prix != 0){
    change.status = "INSUFFICIENT_FUNDS";
    change.change = [];
  }
  var test = false;
  let i = 0;
  while (test == false && i <= 8){
    if (cid[i][1] != 0){
      test = true;
    }
    i++;
  }
  if (test === false){
    change.status = "CLOSED";
    change.change = savecid;
  }
  return change;
}


checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);