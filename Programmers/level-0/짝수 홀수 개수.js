const solution = (num_list) => {
	let evenArr = [];
	let oddArr = [];
	
	for (let i of num_list) {
			if (i % 2 === 0) evenArr.push(i);
			else oddArr.push(i);
	}
	
	return [evenArr.length, oddArr.length];
}