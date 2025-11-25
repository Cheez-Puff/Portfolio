const myText = document.getElementById("myText");
const mySubmit = document.getElementById("mySubmit");
const resultElement = document.getElementById("resultElement");
let age;

mySubmit.onclick = function() {
    age = myText.value;
    age = Number(age);
    if (age >= 100) {
        resultElement.textContent = "Congratulations, you are REALLY old!";
    }
    else if (age < 0) {
        resultElement.textContent = "You haven't been born yet!";
    }
    else if (age >= 18) {
        resultElement.textContent = "You are old enough to vote!";
    } 
    else if (age == 0) {
        resultElement.textContent = "You weren't born today!";
    }
    else if (age < 18) {
        resultElement.textContent = "You are not old enough to vote.";
    }
    else if (isNaN(age)) {
        resultElement.textContent = "Please enter a valid number.";
    }
}