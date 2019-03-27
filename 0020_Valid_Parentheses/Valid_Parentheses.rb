# @param {String} s
# @return {Boolean}
def is_valid(s)
  result = []
  (0...s.length).each do |i|
    case s[i]
    when '[' then result.push s[i]
    when '{' then result.push s[i]
    when '(' then result.push s[i]
    when '}' then return false if result.empty? || result.pop != '{'
    when ']' then return false if result.empty? || result.pop != '['
    when ')' then return false if result.empty? || result.pop != '('
    end
  end
  result.empty?
end
