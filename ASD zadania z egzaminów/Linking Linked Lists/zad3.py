class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def travel(list):
    curr = list
    next = curr.next
    while next != None:
        curr = next
        next = next.next
    return curr


def add_list(list1, list2, last_el):
    curr = list2
    curr_main_list = list1
    shadow = list1
    while curr != None:
        if last_el.val < curr.val:
            last_el.next = curr
            last_el = curr
            copy_curr = curr
            curr = curr.next
            copy_curr.next = None
        elif curr.val <= curr_main_list.val:
            copy_curr = curr.next
            curr.next = curr_main_list
            curr_main_list = curr
            shadow = curr_main_list
            curr = copy_curr
        else:
            new_curr = curr_main_list
            new_shadow = shadow
            while curr.val > new_curr.val:
                new_shadow = new_curr
                new_curr = new_curr.next
            copy_curr = curr.next
            new_shadow.next = curr
            curr.next = new_curr
            curr = copy_curr

    return curr_main_list, last_el


def order(A):
    n = len(A)
    main_list = A[0]
    last_el = travel(main_list)
    first_element = main_list
    for i in range(1, n):
        first_element, last_el = add_list(first_element, A[i], last_el)

    return first_element


def printer(first_el):
    while first_el != None:
        print(first_el.val)
        first_el = first_el.next


A = Node(0)
B = Node(1)
C = Node(2)
D = Node(4)
E = Node(5)

F = Node(0)
G = Node(10)
H = Node(20)

I = Node(5)
J = Node(15)
K = Node(25)

A.next = B
B.next = C
C.next = D
D.next = E

F.next = G
G.next = H

I.next = J
J.next = K

tab = [A, F, I]

first_el = order(tab)

printer(first_el)