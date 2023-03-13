from typing import TypeVar, Generic, List

T = TypeVar('T')

class ICRUD(Generic[T]):
    def create_async(self,obj:T):
        pass
    def delete_async(self,id:int):
        pass
    def update_async(self,obj:T):
        pass
    def get_async(self,id:int):
        pass