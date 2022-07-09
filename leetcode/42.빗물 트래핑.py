def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    ans = 0
    while left < right:
        # max값 갱신
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        #print(left, left_max, right, right_max)

        # 더 높은 쪽으로 이동
        if left_max <= right_max:  # 오른쪽이 더 높은 경우
            ans += left_max - height[left]
            left += 1  # 오른쪽으로 이동
        else:  # 왼쪽이 더 높은 경우
            ans += right_max - height[right]
            right -= 1  # 왼쪽으로 이동
    return ans


# Test Case
print("TC1")
height1 = [4, 2, 0, 3, 2, 5]
print(trap(height1))  # 9

print("TC2")
height2 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height2))  # 6
