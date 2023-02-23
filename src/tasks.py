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
    if temp_head.next == None:
        if temp_head != None:
            return head
    while temp_head.next != None:
        temp_head = temp_head.next
        list_len += 1
    middle_len = math.ceil(list_len/2)
    for x in range(middle_len):
        head = head.next
        if x == middle_len-1:
            return head
# task 2


def merge_sorted_lists(h1: ListNode, h2: ListNode):
    head1 = h1
    head2 = h2
    all_el = []
    if head1 != None:
        while head1:
            all_el.append(head1.value)
            head1 = head1.next
    if head2 != None:
        while head2:
            all_el.append(head2.value)
            head2 = head2.next
    all_el.sort()
    result = ListNode(all_el[0])
    temp = result
    for i in range(1, len(all_el)):
        result.next = ListNode(all_el[i])
        result = result.next
    return temp
# task 3


def reverse_list(head: ListNode):
    all_el = []
    if head != None:
        while head:
            all_el.append(head.value)
            head = head.next
    else:
        return
    all_el.reverse()
    node = ListNode(all_el[0])
    temp = node
    for x in range(1, len(all_el)):
        node.next = ListNode(all_el[x])
        node = node.next
    return temp
# task 4


def validate_parentheses(expr: str):
    skobi1 = []
    skobi2 = []
    for el in expr:
        if el == '(':
            skobi1.append(el)
        if el == ')':
            skobi2.append(el)
    if len(skobi1) == len(skobi2):
        return True
    else:
        return False


# task 5


def backspace_char(sequence: str):
    stack = Stack()
    ans = ''
    for el in sequence:
        if el != '#':
            stack.push(el)
        else:
            if not stack.is_empty():
                stack.pop()
    while not stack.is_empty():
        ans += stack.pop()
    split = list(ans)
    split.reverse()
    return ("".join(split))
