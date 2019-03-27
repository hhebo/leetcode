# @param {Integer} x
# @return {Integer}
def reverse(x)
  result = ''
  if x < 0
    x = -x
    flag = true
  end
  while x.nonzero?
    result << (x % 10).to_s
    x /= 10
  end
  result = result.to_i
  result = -result if flag
  return 0 if result > 2_147_483_647 || result < -2_147_483_648
  result
end
