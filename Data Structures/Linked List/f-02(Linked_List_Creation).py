class Linked_List_Node:
    def __init__(self,data,next) -> None:
        self.data=data
        self.next=next
        

class Linked_List(Linked_List_Node):
    head=None
    def __init__(self, data, next) -> None:
        super().__init__(data, next)
    
    def set_head(self,Linked_List_Node):
        self.head=Linked_List_Node
        
    def linked_list_creation(self,input_data):
        if self.head==None:
            set_head()
            
        
        for i in range(0,len(input_data)):
            if self.head==None:
                


def space_sperated_string_input(input_String):
    input_data=[int(i) for i in input_String.split(' ')]
    return input_data


input_String=input().strip()
input_data=space_sperated_string_input(input_String)
