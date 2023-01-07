function solution(id_pw, db) {
	for (let data of db) {
			if (data[0] === id_pw[0]) {
				 if (data[1] === id_pw[1]) return "login";
					else return "wrong pw";
			}
	}
	
	return "fail";
}