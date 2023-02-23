from functools import reduce
import math
from common.list_node import ListNode
# from common.stack import Stack

# task 1


def create_linked_list(*values):
    return reduce(lambda prev, curr: ListNode(curr, prev), reversed(values), None)


def find_middle_of_list(head: ListNode):

    # my_stack = Stack()
    # stack_2 = Stack()
    # count = 0
    # while head:
    #     my_stack.push(head)
    #     head = head.next
    #     count += 1
    # for _ in range(math.ceil(count/2)):
    #     stack_2.push(my_stack.pop())

    # return stack_2.peek()
    list_len = 0
    temp_head = head
    while temp_head.next != None:
        temp_head = temp_head.next
        list_len += 1
    middle_len = math.ceil(list_len/2)
    for x in range(middle_len):
        head = head.next
        if x == middle_len-1:
            return head.value


llist = create_linked_list(1, 2, 3, 4, 5)
print(find_middle_of_list(llist))
