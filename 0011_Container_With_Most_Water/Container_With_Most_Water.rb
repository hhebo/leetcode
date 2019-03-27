# @param {Integer[]} height
# @return {Integer}
def max_area(height)
  right = height.length - 1
  return 0 if right < 1
  max = 0
  left = 0
  while left < right
    temp = 0
    if height[right] > height[left]
      temp = (right - left) * height[left]
      left += 1
    else
      temp = (right - left) * height[right]
      right -= 1
    end
    max = temp if max < temp
  end
  max
end
