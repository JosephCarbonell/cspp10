function randInt(end){
    var randomNumber = Math.random();
    randomNumber = randomNumber * 10;
    randomNumber = Math.round(randomNumber);
    return(randomNumber);
}

function pickRandom(){
    var randomNumber = randInt();
    var randomNumAsStr = randomNumber.toString();
    var startOfString = "Your random number was ";
    alert(startOfString.concat(randomNumAsStr,"."));
    return randomNumber;
}

function checkNumber(randomNumber){
    if (randomNumber < 5){
        return ("Under 5");
    }
    else if (randomNumber > 5){
        return("Over 5");
    }
    else if (randomNumber === 5){
        return("On 5");
    }
}

function getPlayerBet(){
    while (true){
        var player_bet = parseInt(prompt("Would you like to bet on \n 1. Under 5 \n 2. On 5 \n 3. Over 5\n Please choose [1], [2], or [3]"));
        if (player_bet === 1){
            return ("Under 5");
        }
        else if (player_bet === 2){
            return ("On 5");
        }
        else if (player_bet === 3){
            return ("Over 5");
        }
        else{
            alert("That was invalid, please try again while choosing [1], [2], or [3] for your respective choice.");
        }
    }
}

function getPlayerBetMoney(bank){
    while (true){
        var playerBet = prompt("How much money would you like to bet?");
        playerBet = parseInt(playerBet,10);
        if (playerBet > bank){
            alert("That bet is invalid.");
        }
        else {
            break;
        }
    }
    return (playerBet);
}

function finalGame(){
    var bank = 100;
    while (true){
        if (bank <= 0){
            alert("You lose, please refresh the page to play again.");
        }
        else{
            var bankStr = bank.toString();
            alert("You have ".concat(bankStr," dollars."));
            var rangeChoice = getPlayerBet();
            var playerBet = getPlayerBetMoney(bank);
            var chosenNumber = pickRandom();
            var checkedRoll = checkNumber(chosenNumber);
            if (checkedRoll === rangeChoice & rangeChoice === "Over 5" || rangeChoice === "Under 5"){
                alert("You won the roll");
                bank = bank + playerBet;
            }
            else if (checkedRoll === rangeChoice & rangeChoice === "On 5"){
                alert("You won the roll");
                bank = bank + (playerBet * 4);
            }
            else{
                alert("You lost the roll");
                bank = bank - playerBet;
            }
        }
    }
}

finalGame();