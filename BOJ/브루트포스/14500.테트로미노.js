const readline = require("readline").createInterface({
	input: process.stdin,
	output: process.stdout,
});

let input = [];

readline.on("line", (line) => {
	input.push(line);
}).on("close", () => {
	solution(input);
	process.exit();
});

const solution = (input) => {
	const size = input[0].split(" ").map(el => Number(el));
	const n = Number(size[0]);
	const m = Number(size[1]);
	// console.log(`n: ${n}, m: ${m}`)
	const graph = Array.from({ length: n }, () => []);
	let answer = 0;
	
	for (let i = 1; i < input.length; i++) {
		graph[i - 1] = input[i].split(' ').map((el) => Number(el));
	}

	// console.log(graph);

	/* [*][ ][ ][ ] **/
	const tetromino1_1 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [0, 1], [0, 2], [0, 3]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});
		
		return sum;
	};
	
	/*  
	[*]
	[ ]
	[ ]
	[ ]
	**/
	const tetromino1_2 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [1, 0], [2, 0], [3, 0]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/* 
	[*][ ]
	[ ][ ]
	**/
	const tetromino2_1 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [0, 1], [1, 0], [1, 1]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
	[ ]
	[ ]
	[ ][*]
	**/
	const tetromino3_1 = (i, j) => {
		let sum = 0;
		const direction = [[-2, -1], [-1, -1], [0, -1], [0, 0]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
				[*]
	[ ][ ][ ]
	**/
	const tetromino3_2 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [1, 0], [1, -1], [1, -2]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
	[*][ ]
		 [ ]
		 [ ]
	**/
	const tetromino3_3 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [0, 1], [1, 1], [2, 1]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
	[ ][ ][ ]
	[*]
	**/
	const tetromino3_4 = (i, j) => {
		let sum = 0;
		const direction = [[-1, 0], [-1, 1], [-1, 2], [0, 0]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
	[ ][*]
	[ ]
	[ ]
	**/
	const tetromino3_5 = (i, j) => {
		let sum = 0;
		const direction = [[0, -1], [0, 0], [1, -1], [2, -1]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
	 	 [ ]
		 [ ]
	[*][ ]
	**/
	const tetromino3_6 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [0, 1], [-1, 1], [-2, 1]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};
	
	/*  
	[*]
	[ ][ ][ ]
	**/
	const tetromino3_7 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [1, 0], [1, 1], [1, 2]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
	[ ][ ][ ]
				[*]
	**/
	const tetromino3_8 = (i, j) => {
		let sum = 0;
		const direction = [[-1, -2], [-1, -1], [-1, 0], [0, 0]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/* 
	[*] 
	[ ][ ]
		 [ ]
	**/
	const tetromino4_1 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [1, 0], [1, 1], [2, 1]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
		 [ ][ ]
	[*][ ]
	**/
	const tetromino4_2 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [0, 1], [-1, 1], [-1, 2]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/* 
		 [*] 
	[ ][ ]
	[ ]
	**/
	const tetromino4_3 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [1, -1], [1, 0], [2, -1]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
	[*][ ]
		 [ ][ ]
	**/
	const tetromino4_4 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [0, 1], [1, 1], [1, 2]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
	[ ][ ][ ]
		 [*]
	**/
	const tetromino5_1 = (i, j) => {
		let sum = 0;
		const direction = [[-1, -1], [-1, 0], [-1, 1], [0, 0]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	}

	/*  
	[ ]
	[ ][*]
	[ ]
	**/
	const tetromino5_2 = (i, j) => {
		let sum = 0;
		const direction = [[-1, -1], [0, -1], [0, 0], [1, -1]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
		 [*]
	[ ][ ][ ]
	**/
	const tetromino5_3 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [1, -1], [1, 0], [1, 1]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	/*  
		 [ ]
	[*][ ]
	   [ ]
	**/
	const tetromino5_4 = (i, j) => {
		let sum = 0;
		const direction = [[0, 0], [-1, 1], [0, 1], [1, 1]];
		
		direction.forEach((el) => {
			[x, y] = [i + el[0], j + el[1]];

			if (x < 0 || x >= n || y < 0 || y >= m) {
				sum = -1;
				return false;
			}

			sum += graph[x][y];
		});

		return sum;
	};

	for (let i = 0; i < n; i++) {
		for (let j = 0; j < m; j++) {
			answer = Math.max(answer, tetromino1_1(i, j));
			answer = Math.max(answer, tetromino1_2(i, j));
			answer = Math.max(answer, tetromino2_1(i, j));
			answer = Math.max(answer, tetromino3_1(i, j));
			answer = Math.max(answer, tetromino3_2(i, j));
			answer = Math.max(answer, tetromino3_3(i, j));
			answer = Math.max(answer, tetromino3_4(i, j));
			answer = Math.max(answer, tetromino3_5(i, j));
			answer = Math.max(answer, tetromino3_6(i, j));
			answer = Math.max(answer, tetromino3_7(i, j));
			answer = Math.max(answer, tetromino3_8(i, j));
			answer = Math.max(answer, tetromino4_1(i, j));
			answer = Math.max(answer, tetromino4_2(i, j));
			answer = Math.max(answer, tetromino4_3(i, j));
			answer = Math.max(answer, tetromino4_4(i, j));
			answer = Math.max(answer, tetromino5_1(i, j));
			answer = Math.max(answer, tetromino5_2(i, j));
			answer = Math.max(answer, tetromino5_3(i, j));
			answer = Math.max(answer, tetromino5_4(i, j));
		}
	}

	console.log(answer);
};