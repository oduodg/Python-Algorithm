const solution = (num_list, n) => {
	let arr = [];
	for (let i = 0; i <= num_list.length - n; i+=n) {
			arr.push(num_list.slice(i, i + n));
	}
	return arr;
}