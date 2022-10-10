def deleteNode(head,node):
    head.remove(node)
    return head

if __name__ == "__main__":
    deleteNode([4,5,1,9],1)