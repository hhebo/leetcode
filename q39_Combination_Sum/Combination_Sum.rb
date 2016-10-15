# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum(candidates, target)
  result = []
  dfs(candidates, target, 0, 0, [], result)
  result
end

private

# @param {Integer[]} candidates
# @param {Integer} target
# @param {Integer} start
# @param {Integer} sum
# @param {Integer[]} temp
# @param {Integer[][]} result
# @return nil
def dfs(candidates, target, start, sum, temp, result)
  if sum == target
    result.push temp.dup
    return
  end
  (start...candidates.length).each do |i|
    next unless sum + candidates[i] <= target
    temp.push candidates[i]
    dfs(candidates, target, i, sum + candidates[i], temp, result)
    temp.pop
  end
end
