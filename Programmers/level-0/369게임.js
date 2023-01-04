function solution(order) {
	const getElNum = (arr, el) => arr.reduce((acc, curr) => acc + (curr == el), 0);
	return [3, 6, 9].reduce((acc, curr) => acc + getElNum([...String(order)], curr), 0); 
}