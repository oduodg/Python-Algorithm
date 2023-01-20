class minHeap {
	constructor() {
		this.heap = [null];
	}

	push(value) {
		this.heap.push(value);
		let currentIndex = this.heap.length - 1;
		let parentIndex = Math.floor(currentIndex / 2);

		while (parentIndex !== 0 && this.heap[parentIndex] > value) {
			const temp = this.heap[parentIndex];
			this.heap[parentIndex] = value;
			this.heap[currentIndex] = temp;

			currentIndex = parentIndex;
			parentIndex = Math.floor(currentIndex / 2);
		}
	}

	pop() {
		const returnValue = this.heap[1];
		this.heap[1] = this.heap.pop();

		let currentIndex = 1;
		let leftIndex = 2;
		let rightIndex = 3;
		while (
			this.heap[currentIndex] > this.heap[leftIndex] ||
			this.heap[currentIndex] > this.heap[rightIndex]
		) {
			if (this.heap[leftIndex] > this.heap[rightIndex]) {
				const temp = this.heap[currentIndex];
				this.heap[currentIndex] = this.heap[rightIndex];
				this.heap[rightIndex] = temp;
				currentIndex = rightIndex;
			} else {
				const temp = this.heap[currentIndex];
				this.heap[currentIndex] = this.heap[leftIndex];
				this.heap[leftIndex] = temp;
				currentIndex = leftIndex;
			}
			leftIndex = currentIndex * 2;
			rightIndex = currentIndex * 2 + 1;
		}

		return returnValue;
	}
    
    getMin() {
        return this.heap[1] !== null ? this.heap[1] : null;
    }
}

function solution(k, score) {
    // 상위 k번째 이내 -> 명예의 전당
    // k일 까지는 모두 명예의 전당
    // k일 이후부터는 명예의 전당 바뀜
    // 매일 명예의 전당 최하위 점수를 발표
    const heap = new minHeap();
    let ans = [];
    
    score.forEach((v, i) => {
        if (i < k) heap.push(v);
        else {
            if (v > heap.getMin()) {
                heap.pop();
                heap.push(v);
            }
        }
        ans.push(heap.getMin());
    });
    
    return ans;
}