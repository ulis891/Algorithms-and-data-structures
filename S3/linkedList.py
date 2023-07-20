class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def append(self, val):
        end = Node(val)
        n = self
        while (n.next):
            n = n.next
        n.next = end


head = Node(123)
head.append(321)
head.append(456)
head.append(654)



def print_list(head, end='\n'):
    while head:
        print(head.data, end=' -> ' if head.next else '')
        head = head.next
    print(end=end)


def reverse_list(head, tail=None):
    while head:
        head.next, tail, head = tail, head, head.next
    return tail

print_list(head)
print_list(reverse_list(head))

