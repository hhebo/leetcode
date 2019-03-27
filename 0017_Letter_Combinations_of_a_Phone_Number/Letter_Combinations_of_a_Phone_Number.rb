Letters =
  ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxzy'].map do |letter|
    letter.split('')
  end

# @param {String} digits
# @return {String[]}
def letter_combinations(digits)
  return [] if digits.empty?
  result = []
  digits = digits.split('').map(&:to_i)
  generate(result, '', 0, digits)
  result
end

# @param {String[]} result
# @param {String} temp
# @param {Integer} index
# @param {Array[]} digits
def generate(result, temp, index, digits)
  if index == digits.length
    result.push(temp)
    return
  end
  (0...Letters[digits[index]].length).each do |i|
    generate(result, temp + Letters[digits[index]][i], index + 1, digits)
  end
end
