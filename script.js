const cells = document.querySelectorAll(".cell");
const turnText = document.getElementById("turn");

const resultScreen = document.getElementById("resultScreen");
const resultText = document.getElementById("resultText");

let currentPlayer = "X";
let board = ["","","","","","","","",""];
let gameActive = true;

const winPatterns = [

[0,1,2],
[3,4,5],
[6,7,8],
[0,3,6],
[1,4,7],
[2,5,8],
[0,4,8],
[2,4,6]

];

cells.forEach(cell=>{
cell.addEventListener("click",cellClick);
});

function cellClick(){

const index = this.dataset.index;

if(board[index] !== "" || !gameActive){
return;
}

board[index] = currentPlayer;
this.innerText = currentPlayer;

checkWinner();

}

function checkWinner(){

let won = false;

for(let pattern of winPatterns){

const [a,b,c] = pattern;

if(board[a] && board[a] === board[b] && board[a] === board[c]){

won = true;
break;

}

}

if(won){

showResult(`Player ${currentPlayer} Wins!`);
gameActive = false;
return;

}

if(!board.includes("")){

showResult("Game Draw!");
gameActive = false;
return;

}

currentPlayer = currentPlayer === "X" ? "O" : "X";
turnText.innerText = `Player ${currentPlayer} Turn`;

}

function showResult(message){

resultText.innerText = message;
resultScreen.style.display = "flex";

}

function newGame(){

board = ["","","","","","","","",""];
gameActive = true;
currentPlayer = "X";

cells.forEach(cell=>{
cell.innerText="";
});

turnText.innerText = "Player X Turn";
resultScreen.style.display = "none";

}