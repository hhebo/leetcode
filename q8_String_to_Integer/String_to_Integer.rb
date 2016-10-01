# @param {String} str
# @return {Integer}
def my_atoi(str)
  return 0 if str.nil?
  flag = true
  index = 0
  result = ''
  (0...str.length).each do |i|
    if str[i] == '-'
      flag = false
      index = i + 1
      break
    end
    if str[i] == '+'
      index = i + 1
      break
    end
    next if str[i] == ' '
    if str[i] && str[i].to_i && str[i].to_i.to_s && str[i].to_i.to_s == str[i]
      index = i
      break
    else
      return 0
    end
  end
  (index...str.length).each do |i|
    if str[i] && str[i].to_i && str[i].to_i.to_s && str[i].to_i.to_s == str[i]
      result << str[i]
    else
      break
    end
  end
  result = result.to_i
  if result >= 2_147_483_648
    result = 2_147_483_648
    result = 2_147_483_647 if flag
  end
  flag ? result : -result
end
