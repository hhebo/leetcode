# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Float}
def find_median_sorted_arrays(nums1, nums2)
  len = nums1.length + nums2.length
  nums = []
  i = j = 0
  (0..len).each do |_index|
    if i < nums1.length && j < nums2.length
      if nums1[i] <= nums2[j]
        nums << nums1[i]
        i += 1
      else
        nums << nums2[j]
        j += 1
      end
    elsif i < nums1.length
      nums << nums1[i]
      i += 1
    else
      nums << nums2[j]
      j += 1
    end
  end
  (len % 2).zero? ? (nums[len / 2] + nums[len / 2 - 1]) / 2.0 : nums[len / 2] / 1.0
end
