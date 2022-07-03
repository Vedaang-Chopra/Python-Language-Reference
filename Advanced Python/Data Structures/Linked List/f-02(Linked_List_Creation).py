class Linked_List_Node:
    def __init__(self,data,next) -> None:
        self.data=data
        self.Next=next        

class Linked_List(Linked_List_Node):
    def __init__(self) -> None:
        self.Head=None
        # super().__init__(data, next)
    
    def set_head(self,first_node):
        self.Head=first_node
    
    def set_next_node(self,current_node,new_node):
        current_node.Next=new_node
    
    def linked_list_creation(self,input_data):
        for i in range(0,len(input_data)):
            CURRENT_DATA=input_data[i]
            if CURRENT_DATA==-1:
                break
            else:
                new_node=Linked_List_Node(CURRENT_DATA,None)
                if self.Head==None:
                    self.set_head(new_node)
                else:
                    current_pointer=self.Head
                    while current_pointer.Next!=None:
                        current_pointer=current_pointer.Next
                    self.set_next_node(current_pointer,new_node)

def space_sperated_string_input(input_String):
    input_data=[int(i) for i in input_String.split(' ')]
    return input_data



input_String=input().strip()
input_data=space_sperated_string_input(input_String)

obj=Linked_List()
obj.linked_list_creation(input_data)
print(obj)
curr=obj.Head
print(obj.Head.data)
while curr.Next!=None:
    print(curr.data)
    curr=curr.Next
