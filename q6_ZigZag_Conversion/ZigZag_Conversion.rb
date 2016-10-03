# @param {String} s
# @param {Integer} num_rows
# @return {String}
def convert(s, num_rows)
  result = ''
  str = []
  i = 0
  while i < s.length
    j = 0
    while j < num_rows && i < s.length
      str[j] =
        if str[j]
          str[j] << s[i]
        else
          s[i]
        end
      j += 1
      i += 1
    end
    k = num_rows - 2
    while k > 0 && i < s.length
      str[k] << s[i]
      k -= 1
      i += 1
    end
  end
  (0...str.length).each do |l|
    result << str[l]
  end
  result
end
