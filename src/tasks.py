import math
from src.common.list_node import ListNode
from src.common.stack import Stack

# task 1


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
    ans = None
    while temp_head.next != None:
        temp_head = temp_head.next
        list_len += 1
    middle_len = math.ceil(list_len/2)
    for x in range(middle_len):
        head = head.next
        if x == middle_len-1:
            return head.value
# task 2


def merge_sorted_lists(h1: ListNode, h2: ListNode):
    raise NotImplementedError()

# task 3


def reverse_list(head: ListNode):
    raise NotImplementedError()

# task 4


def validate_parentheses(expr: str):
    raise NotImplementedError()

# task 5


def backspace_char(sequence: str):
    raise NotImplementedError()
