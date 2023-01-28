const readline = require("readline").createInterface({
	input: process.stdin,
	output: process.stdout,
});

let input = [];

readline
	.on("line", (line) => {
		input.push(line);
	})
	.on("close", () => {
		solution(input);
		process.exit();
	});


// 연구소는 세로 N x 가로 M , 빈 칸(0) & 벽(1) & 바이러스(2)
// 바이러스는 상하좌우로 퍼져나감
// 새롭게 새울 수 있는 벽의 개수는 3개. 꼭 3개를 다 세워야함.
// 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳 => 안전 영역
// 안전 영역 크기의 최댓값을 return

const solution = (input) => {
	const size = input[0].split(" ").map(el => Number(el));
	const n = size[0]; // 세로
	const m = size[1]; // 가로
	const graph = Array.from({ length: n }, () => []);
	let answer = 0;

	for (let i = 1; i < input.length; i++) {
		graph[i - 1] = input[i].split(" ").map(el => Number(el));
	}

	/* 바이러스 전파 후 안전 영역의 크기 구하기 */
	const bfs = () => {
		let lab = graph.map(el => [...el]); // 2차원 배열 깊은 복사
		let q = [];
		let safeAreaCount= 0;
		const dx = [0, 0, -1, 1];
		const dy = [-1, 1, 0, 0];

		for (let i = 0; i < n; i++) {
			for (let j = 0; j < m; j++) {
				if (lab[i][j] === 2) { // 바이러스인 경우
					q.push([i, j]); // 바이러스의 위치를 q에 push
				}
			}
		}

		while (q.length > 0) {
			[x, y] = q.shift();

			for (let i = 0; i < 4; i++) {
				const nx = x + dx[i];
				const ny = y + dy[i];

				if (0 <= nx && nx < n
					&& 0 <= ny && ny < m) {
					if (lab[nx][ny] === 0) {
						lab[nx][ny] = 2; // 바이러스 전파
						q.push([nx, ny]);
					}
				}
			}
		}

		lab.forEach(row => {
			row.forEach(col => {
				if (col === 0) { // 안전영역인 경우
					safeAreaCount += 1;
				}
			});
		});

		answer = Math.max(answer, safeAreaCount);
	};

	/* 3개의 벽 세우기 */
	const makeWall = (wallCount) => {
		if (wallCount === 3) {
			bfs();
			return;
		}

		for (let i = 0; i < n; i++) {
			for (let j = 0; j < m; j++) {
				if (graph[i][j] === 0) { // 빈 칸인 경우
					graph[i][j] = 1; // 벽 세우기
					makeWall(wallCount + 1); // 다음 벽 세우기
					graph[i][j] = 0; // 다음 시뮬레이션을 위해 원상복귀
				}
			}
		}
	};

	makeWall(0);
	console.log(answer);
};