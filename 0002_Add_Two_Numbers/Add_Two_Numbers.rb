# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def add_two_numbers(l1, l2)
  result = []
  temp = 0
  while l1 && l2
    result << (l1.val + l2.val + temp) % 10
    temp = (l1.val + l2.val + temp) / 10
    l1 = l1.next
    l2 = l2.next
  end
  while l1
    result << (l1.val + temp) % 10
    temp = (l1.val + temp) / 10
    l1 = l1.next
  end
  while l2
    result << (l2.val + temp) % 10
    temp = (l2.val + temp) / 10
    l2 = l2.next
  end
  result.push temp if temp.nonzero?
  result
end
