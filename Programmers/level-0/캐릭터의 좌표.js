function solution(keyinput, board) {
	let answer = [0, 0];
	
	for (let arrow of keyinput) {
			if (arrow === "left") {
					if (answer[0] === Math.trunc(board[0] / 2) * -1) continue;
					answer[0]--;
			} else if (arrow === "right") {
					if (answer[0] === Math.trunc(board[0] / 2)) continue;
					answer[0]++;
			} else if (arrow === "up") {
					if (answer[1] === Math.trunc(board[1] / 2)) continue;
					answer[1]++;
			} else { // "down"
					if (answer[1] === Math.trunc(board[1] / 2) * -1) continue;
					answer[1]--;
			}
	}
	
	return answer;
}