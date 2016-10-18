# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def reverse_k_group(head, k)
    return head if k == 1 || head.nil?
    len = 0
    temp = head
    while temp
        len += 1
        temp = temp.next
    end
    return head if len < k
    result = ListNode.new(0)
    current_node = head
    result.next = head
    last_node = result
    (0...len/k).each do
        (0...k-1).each do
            temp_node = last_node.next
            last_node.next = current_node.next
            current_node.next = current_node.next.next
            last_node.next.next = temp_node
        end
        last_node = current_node;
        current_node = current_node.next;
    end
    result.next
end
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @param {Integer} k
# @return {ListNode}
def reverse_k_group(head, k)
  return head if k == 1 || head.nil?
  len = 0
  temp = head
  while temp
    len += 1
    temp = temp.next
  end
  return head if len < k
  result = ListNode.new(0)
  current_node = head
  result.next = head
  last_node = result
  (0...len / k).each do
    (0...k - 1).each do
      temp_node = last_node.next
      last_node.next = current_node.next
      current_node.next = current_node.next.next
      last_node.next.next = temp_node
    end
    last_node = current_node
    current_node = current_node.next
  end
  result.next
end
