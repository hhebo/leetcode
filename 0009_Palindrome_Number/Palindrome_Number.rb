# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
  return false if x < 0
  x.to_s == x.to_s.reverse ? true : false
end
