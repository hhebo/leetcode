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
def merge_two_lists(l1, l2)
  return l2 if l1.nil?
  return l1 if l2.nil?
  result_node = ListNode.new(0)
  current_node = result_node
  last_node = result_node
  while l1 && l2
    if l1.val <= l2.val
      current_node.val = l1.val
      current_node.next = ListNode.new(0)
      l1 = l1.next
    else
      current_node.val = l2.val
      current_node.next = ListNode.new(0)
      l2 = l2.next
    end
    last_node = current_node
    current_node = current_node.next
  end
  while l1
    current_node.val = l1.val
    current_node.next = ListNode.new(0)
    l1 = l1.next
    last_node = current_node
    current_node = current_node.next
  end
  while l2
    current_node.val = l2.val
    current_node.next = ListNode.new(0)
    l2 = l2.next
    last_node = current_node
    current_node = current_node.next
  end
  last_node.next = nil if current_node.val.zero?
  result_node
end
