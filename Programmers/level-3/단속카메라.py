# 단속용 카메라를 한 번은 만나도록 카메라를 설치
# 최소 카메라 수 return

def solution(routes):
    # 진출순으로 오름차순 정렬
    routes.sort(key=lambda x: x[1])
    
    # 처음으로 진출하는 차량의 진출 지점에 카메라 설치
    camera_number = routes[0][1]
    count_camera = 1
    
    for route in routes:
        # 설치된 카메라 위치가 진입 지점과 진출 지점 사이에 있으면 continue
        if route[0] <= camera_number <= route[1]:
            continue
        
        else:
            # 카메라를 진출 지점에 설치한다.
            camera_number = route[1]
            count_camera += 1
    
    return count_camera