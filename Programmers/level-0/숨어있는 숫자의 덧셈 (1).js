const solution = (my_string) => {
	return my_string.match(/\d/g).reduce((acc, curr) => acc + parseInt(curr), 0);
}