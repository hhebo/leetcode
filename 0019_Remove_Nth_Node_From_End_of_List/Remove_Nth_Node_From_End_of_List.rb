# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @param {Integer} n
# @return {ListNode}
def remove_nth_from_end(head, n)
  temp = head
  result = []
  while n > 0 && temp
    temp = temp.next
    n -= 1
  end
  while temp
    temp = temp.next
    result << head.val
    head = head.next
  end
  head = head.next
  while head
    result << head.val
    head = head.next
  end
  result
end
