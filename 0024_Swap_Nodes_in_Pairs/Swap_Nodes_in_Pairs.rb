# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {ListNode}
def swap_pairs(head)
  return head if head.nil? || head.next.nil?
  result = ListNode.new(0)
  current_node = result
  last_node = result
  while head && head.next
    current_node.val = head.next.val
    last_node = current_node
    current_node.next = ListNode.new(0)
    current_node = current_node.next
    current_node.val = head.val
    last_node = last_node.next
    last_node = current_node
    current_node.next = ListNode.new(0)
    current_node = current_node.next
    head = head.next.next
  end
  if head
    current_node.val = head.val
    last_node = current_node
  end
  last_node.next = nil if current_node.val.zero?
  result
end
