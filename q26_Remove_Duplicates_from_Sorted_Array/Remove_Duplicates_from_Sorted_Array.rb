# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  return 0 if nums.empty?
  result = 0
  (1...nums.length).each do |i|
    if nums[i] != nums[result]
      result += 1
      nums[result] = nums[i]
    end
  end
  result + 1
end
