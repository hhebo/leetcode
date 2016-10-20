# @param {String} haystack
# @param {String} needle
# @return {Integer}
def str_str(haystack, needle)
  return 0 if needle.empty?
  return -1 if haystack && needle && haystack[needle].nil?
  (0...haystack.length).each do |i|
    (0...needle.length).each do |j|
      break if haystack[i + j] != needle[j]
      return i if j == needle.length - 1
    end
  end
end
