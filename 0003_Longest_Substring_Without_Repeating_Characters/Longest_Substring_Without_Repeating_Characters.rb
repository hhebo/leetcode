# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  return 0 if s.empty?
  hash = {}
  hash[s[0]] = 0
  len = 1
  start = 0
  (1 ... s.length).each do |i|
    if hash[s[i]]
      len = i - start if i - start > len
      start = hash[s[i]] + 1 if hash[s[i]] >= start
      hash[s[i]] =  i
    else
      hash[s[i]] = i
    end
  end
  len = s.length - start if s.length - start > len
  len
end
