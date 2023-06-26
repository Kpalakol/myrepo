// append value to the input box
function appendToResult(value) {
  document.getElementById("result").value += value;
}

// clear the last character from the input box
function clearLast() {
  var result = document.getElementById("result").value; // replace "result" with the ID of your result element
  document.getElementById("result").value = result.slice(0, -1);
}

// calculate result of the expression in the input box
function calculateResult() {
  let result = document.getElementById("result").value;

  if (result) {
    if (result.endsWith("%")) {
      let num;

      if (result.includes("*")) {
        result = result.slice(0, -1);
        let [numStr, percent] = result.split("*");
        num = parseFloat(numStr);
        result = num * (parseFloat(percent) / 100);
      } else {
        num = parseFloat(result.slice(0, -1));
        result = num / 100;
      }
    } else if (result.includes("√")) { // added condition for square root evaluation
      if (result.startsWith("√")) {
        let num = parseFloat(result.slice(1));
        result = Math.sqrt(num);
      } else {
        let index = result.indexOf("√");
        let operator = "+";

        if (index - 1 >= 0) {
          operator = result[index - 1];
        }

        let num = parseFloat(result.slice(0, index));
        let innerNum = 1;

        if (result[index + 1]) {
          innerNum = parseFloat(result.slice(index + 1));
        }

        let root = Math.sqrt(num);
        let computedVal = 0;

        switch (operator) {
          case "+":
            computedVal = num + innerNum * root;
            break;
          case "-":
            computedVal = num - innerNum * root;
            break;
          case "*":
            computedVal = num * root * innerNum;
            break;
          case "/":
            computedVal = num / (root * innerNum);
            break;
          default:
            computedVal = num * root * innerNum;
            break;
        }

        result = computedVal;
      }
    } else if (result.includes("^")) { // added condition for exponentiation
        let [base, exponent] = result.split("^");
        let numBase = parseFloat(base);
        let numExponent = parseFloat(exponent);
        result = Math.pow(numBase, numExponent);
      } else {
      result = eval(result);
    }

    document.getElementById("result").value = result;
  }
}

// clear the input box
function clearAll() {
  document.getElementById("result").value = ""; // replace "result" with the ID of your result element
}

// calculate sin, cos and tan functions
function calculateTrigFunction(trigFunction) {
  let resultElement = document.getElementById("result");
  let radians = parseFloat(resultElement.value) * (Math.PI / 180);
  let result = Math[trigFunction](radians);
  resultElement.value = result;
}
