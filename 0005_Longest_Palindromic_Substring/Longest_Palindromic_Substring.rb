# @param {String} s
# @return {String}
def longest_palindrome(s)
  return s if s.length <= 1
  left = right = 0
  (0...s.length).each do |i|
    start_ch = end_ch = i
    loop do
      i += 1
      break unless i < s.length && s[start_ch] == s[i]
    end
    end_ch = i - 1
    while start_ch - 1 >= 0 && end_ch + 1 < s.length && s[start_ch - 1] == s[end_ch + 1]
      start_ch -= 1
      end_ch += 1
    end
    if right - left < end_ch - start_ch
      right = end_ch
      left = start_ch
    end
  end
  s[left..right]
end
