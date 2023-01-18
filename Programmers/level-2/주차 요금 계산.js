function solution(fees, records) {
	// 차량별로 주차 요금 계산
	// 출차 내역이 없다면 23:59에 출차된 것
	// 누적 주차 시간 <= 기본 시간 이면 기본 요금 청구
	// 초과하면 기본 요금 + 단위 시간(올림) 당 단위 요금
	// fees: 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
	// records: 시각(시:분) (00:00 ~ 23:59), 차량 번호(0~9), 내역(IN, OUT)
	// 시각을 기준으로 오름차순 정렬
	// 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 배열에 담아서 return
	
	let logs = new Map();
	let ans = [];
	
	// 차량 번호별로 입출차 시각 기록하기
	records.forEach((v) => {
			[time, no, inout] = v.split(" ");
			if (logs.has(no)) {
					logs.get(no).push(time);
			} else {
					logs.set(no, [time]);
			}
	});
	
	// 차량 번호가 작은 순으로 정렬하기
	logs = new Map([...logs].sort());
	
	logs.forEach((value, key) => {
			let cumulTime = 0;
			let inTime = '';
			let outTime = '';
			
			if (value.length % 2 == 1) { // 23:59에 출차한 경우 먼저 계산
					inTime = value[value.length - 1].split(":");
					cumulTime += (23 - Number(inTime[0])) * 60 + (59 - Number(inTime[1]));
					value.pop(); // 마지막 시각 제거
			}

			for (let i = 0; i < value.length; i += 2) {
					inTime = value[i].split(":");
					outTime = value[i + 1].split(":");
					cumulTime += ((Number(outTime[0]) - Number(inTime[0])) * 60) + (Number(outTime[1] - Number(inTime[1])));
			}
			
			if (cumulTime <= fees[0]) { //누적 주차 시간 <= 기본 시간
					ans.push(fees[1]); // 기본 요금 부과
			} else {
					const overTime = cumulTime - fees[0]; // 초과 시간
					const overCharge = Math.ceil(overTime / fees[2]) * fees[3];
					ans.push(fees[1] + overCharge);
			}
	});
	
 return ans;
}