# @param {Integer[]} nums
# @param {Integer} val
# @return {Integer}
def remove_element(nums, val)
  result = 0
  (0...nums.length).each do |i|
    if nums[i] != val
      nums[result] = nums[i]
      result += 1
    end
  end
  result
end
