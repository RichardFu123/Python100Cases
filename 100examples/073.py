class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

class List:

    def __init__(self, head):
        self.head = head

    def is_empty(self): 
        return self.get_len() == 0

    def get_len(self):  
        length = 0
        temp = self.head
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def append(self, node):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def delete(self, index): 
        if index < 1 or index > self.get_len():
            print("给定位置不合理")
            return
        if index == 1:
            self.head = self.head.next
            return
        temp = self.head
        cur_pos = 0
        while temp is not None:
            cur_pos += 1
            if cur_pos == index-1:
                temp.next = temp.next.next
            temp = temp.next

    def insert(self, pos, node):
        if pos < 1 or pos > self.get_len():
            print("插入结点位置不合理")
            return
        temp = self.head
        cur_pos = 0
        while temp is not Node:
            cur_pos += 1
            if cur_pos == pos-1:
                node.next = temp.next
                temp.next =node
                break
            temp = temp.next

    def reverse(self, head):
        if head is None and head.next is None:
            return head
        pre = head
        cur = head.next
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        head.next = None
        return pre

    def print_list(self, head):
        init_data = []
        while head is not None:
            init_data.append(head.get_data())
            head = head.next
        return init_data

if __name__=='__main__':
    head=Node('head')
    link=List(head)
    for i in range(10):
        node=Node(i)
        link.append(node)
    print(link.print_list(head))
    print(link.print_list(link.reverse(head)))
