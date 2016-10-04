# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
  r = /#{p}/.match(s)
  r && r[0] == s || false
end
