function solution(n, t, m, timetable) {
	// 09:00부터 총 n회 t분 간격, 최대 m명 탑승
	// 23:59에는 리셋
	// 도착한 순간에 바로 출발
	// 같은 시각에 도착하면 대기열에서 제일 뒤에 선다.
	// 제일 늦는 도착 시간 구하기
	// 크루의 도착 시각 HH:MM (00:01 ~ 23:59)
	
	// 일단 버스가 언제 오는지 구하자
	// 콘은 마지막 버스에 타면 된다.
	// 각 버스마다 크루의 도착 시각을 넣어줘 -> 주의할것은 버스 시각 보다 도착 시각이 같거나 작아야함
	// 마지막 버스의 마지막 탑승 크루보다만 1분 일찍 오면됨
	
	// 셔틀버스 출발(도착) 시각 구하기
	let bus = {};
	let hh = 9;
	let mm = 0;
	let time = 0;
	let strTime = '';
	bus['09:00'] = [];
	
	for (let i = 1; i < n; i++) {
			time = hh * 60 + mm + t;
			hh = Math.floor(time / 60);
			mm = time % 60;
			strTime = String(hh).padStart(2, '0').concat(`:${String(mm).padStart(2, '0')}`);
			bus[strTime] = [];
	}
	
	// 버스 시각별로 탑승 가능한 크루의 도착 시각 구하기
	timetable.sort(); // 크루의 도착 시각 오름차순 정렬
	
	for (const crewTime of timetable) {
			for (busTime in bus) {
					if (Number(crewTime.split(':').join('')) 
							<= Number(busTime.split(':').join(''))
						 && bus[busTime].length < m) {
							bus[busTime].push(crewTime);
							break;
					}
			}
	}
	
	let lastBus = Object.keys(bus)[Object.keys(bus).length - 1];
	
	if (bus[lastBus].length < m) return lastBus; // 마지막 버스에 자리가 남아있을 경우
	else {
			let lastCrewTime = bus[lastBus][m - 1].split(':');
			
			time = Number(lastCrewTime[0]) * 60 + Number(lastCrewTime[1]) - 1;
			hh = Math.floor(time / 60);
			mm = time % 60;
			
			return String(hh).padStart(2, '0')
							.concat(`:${String(mm).padStart(2, '0')}`);
	}
}