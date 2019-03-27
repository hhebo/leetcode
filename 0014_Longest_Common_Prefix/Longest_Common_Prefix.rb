# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
  return '' if strs.empty?
  result = strs[0]
  (1...strs.length).each do |i|
    while strs[i].index(result) != 0
      result = result[0...(result.length - 1)]
      return '' if result.nil?
    end
  end
  result
end
