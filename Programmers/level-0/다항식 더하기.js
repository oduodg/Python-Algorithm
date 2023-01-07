function solution(polynomial) {
	const arr = polynomial.split(' ');
	let sumX = 0;
	let sumNum = 0;
	const hasX = arr.filter(v => v.includes("x"))
									.map(v => {
											if (v === "x") sumX++;
											else sumX += parseInt(v);
									});
	const num = arr.filter(v => !v.includes("x") && v !== "+")
								 .map(v => sumNum += parseInt(v));
	
	if (sumX === 0 && sumNum === 0) return 0;
	if (sumX === 0) return sumNum.toString();
	
	if (sumX === 1) {
			sumX = "x";
	} else {
			sumX = sumX.toString() + "x";
	}
	
	if (sumNum === 0) {
			return sumX;
	}
	
	sumNum = sumNum.toString();

	return sumX + " + " + sumNum;
}