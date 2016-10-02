# @param {Integer} num
# @return {String}
def int_to_roman(num)
  str = %w(M CM D CD C XC L XL X IX V IV I)
  nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  result = ''
  index = 0
  while num > 0
    if num >= nums[index]
      num -= nums[index]
      result << str[index]
    else
      index += 1
    end
  end
  result
end
