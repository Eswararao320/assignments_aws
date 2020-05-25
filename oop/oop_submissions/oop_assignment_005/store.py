class Item:
    def __init__(self,name,price,category):
        self.name=name
        if price<=0:
            raise ValueError('Invalid value for price, got {}'.format(price))
        self.price=price
        self.category=category
        
    def __str__(self):
        return ('{}@{}-{}'.format(self.name,self.price,self.category))
        
class Query:
    
    operation_list = ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        
    def __init__(self,field,operation,value):
        self.field = field
        self.operation = operation
        self.value = value
        if operation in Query.operation_list:
            self.operation=operation
        else:
            raise ValueError('Invalid value for operation, got {}'.format(operation))
            
    def __str__(self):
        return ('{} {} {}'.format(self.field,self.operation,self.value))

class Store:
    def __init__(self):
        self.items=[]
        
    def add_item(self,item):#composion enduku ante has relation undi kanuka .. store ha an item.. is relation unte inherit chesukovali
        self.items.append(item)
        
    def __str__(self):
        
        if len(self.items)>0:
            return '\n'.join(map(str,self.items))
        else:
            return "No items"
    
    def filter(self,query):
        
        filter_list=Store()
    
        for item in self.items:#item anedi variyable like i laga
            
            field_value=getattr(item,query.field) #getattr function returns the value of the specified attribute from the specified object
                
            if query.operation=='IN' and field_value in query.value:
                filter_list.add_item(item)#filter_list nundi add_item ki call ayyi items loki item append avtundi
                
            elif query.operation=='EQ' and field_value == query.value:
                filter_list.add_item(item)

            elif query.operation=='GT' and field_value > query.value:
                filter_list.add_item(item)
            
            elif query.operation=='GTE' and field_value >= query.value:
                filter_list.add_item(item)
                
            elif query.operation=='LT' and field_value < query.value:
                filter_list.add_item(item)
                
            elif query.operation=='LTE' and field_value <= query.value:
                filter_list.add_item(item)

            elif query.operation=='STARTS_WITH' and field_value.startswith(query.value):
                filter_list.add_item(item)

            elif query.operation=='ENDS_WITH' and field_value.endswith(query.value):
                filter_list.add_item(item)
                
            elif query.operation=='CONTAINS' and query.value in field_value:
                filter_list.add_item(item)


        return filter_list
    
    def count(self):
        return len(self.items)
    
    def exclude(self,query):
        exclude_list=Store()
        filter_query=self.filter(query)
        
        for item in self.items:
            if item not in filter_query.items:
                exclude_list.add_item(item)
        return exclude_list


