# @param {Integer[]} nums
# @return {Integer[][]}
def three_sum(nums)
  result = []
  return result if nums.length <= 2
  nums.sort!
  (0...nums.length - 2).each do |i|
    j = i + 1
    k = nums.length - 1
    while j < k
      if (nums[i] + nums[j] + nums[k]).zero?
        temp = [nums[i], nums[j], nums[k]]
        result << temp
        j += 1
        k -= 1
      elsif nums[i] + nums[j] + nums[k] < 0
        j += 1
      else
        k -= 1
      end
    end
    i += 1 while i < nums.length - 1 && nums[i] == nums[i + 1]
  end
  result.uniq.dup
end
