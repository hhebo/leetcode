# @param {Integer} n
# @return {String[]}
def generate_parenthesis(n)
  result = []
  generate(result, '', 0, 0, n)
  result
end

private

# @param {String[]} result
# @param {String} str
# @param {Integer} left
# @param {Integer} right
# @param {Integer} n
def generate(result, str, left, right, n)
  if str.length == 2 * n
    result.push(str)
    return
  end
  generate(result, str + '(', left + 1, right, n) if left < n
  generate(result, str + ')', left, right + 1, n) if right < left
end
