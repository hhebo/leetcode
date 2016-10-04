# @param {String} s
# @return {Integer}
def roman_to_int(s)
  result = 0
  temp = []
  (0...s.length).each do |i|
    if s[i] == 'I'
      temp[i] = 1
    elsif s[i] == 'V'
      temp[i] = 5
    elsif s[i] == 'X'
      temp[i] = 10
    elsif s[i] == 'L'
      temp[i] = 50
    elsif s[i] == 'C'
      temp[i] = 100
    elsif s[i] == 'D'
      temp[i] = 500
    elsif s[i] == 'M'
      temp[i] = 1000
    else
      return 0
    end
    result =
      if i - 1 >= 0
        if temp[i] <= temp[i - 1]
          result + temp[i]
        else
          result - 2 * temp[i - 1] + temp[i]
        end
      else
        result + temp[i]
      end
  end
  result
end
