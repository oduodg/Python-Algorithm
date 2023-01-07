function solution(common) {
	const d = common[1] - common[0]; // 공차
	const r = common[1] / common[0]; // 공비
	
	if (d === common[2] - common[1]) { // 등차수열
			return common[common.length -1] + d;
	} else { // 등비수열
			return common[common.length -1] * r;
	}
}