# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[][]}
def four_sum(nums, target)
  return [] if nums.length < 4
  nums.sort!
  result = []
  (0...nums.length - 3).each do |i|
    next if i > 0 && nums[i] == nums[i - 1]
    (i + 1...nums.length - 2).each do |j|
      next if j > i + 1 && nums[j] == nums[j - 1]
      k = j + 1
      l = nums.length - 1
      while k < l
        sum = nums[i] + nums[j] + nums[l] + nums[k]
        if target > sum
          k += 1
        elsif target < sum
          l -= 1
        else
          result << [nums[i], nums[j], nums[l], nums[k]]
          loop do
            k += 1
            break unless k < l && nums[k] == nums[k - 1]
          end
          loop do
            l -= 1
            break unless k < l && nums[l] == nums[l + 1]
          end
        end
      end
    end
  end
  result
end
