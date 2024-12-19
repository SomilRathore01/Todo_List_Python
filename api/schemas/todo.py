# from pydantic import BaseModel, Field
# from typing import Optional
# from tortoise.contrib.pydantic import pydantic_model_creator
# from api.models.todo import Todo

# GetTodo = pydantic_model_creator(None, name="Todo")

# class PostTodo(BaseModel):
#     task:str = Field(..., max_length=100)
#     done:bool

# class PutTodo(BaseModel):
#     task:Optional[str] = Field(None, max_length=100)
#     done: Optional[bool]

from tortoise.contrib.pydantic import pydantic_model_creator
from api.models.todo import Todo

GetTodo = pydantic_model_creator(Todo, name="TodoGet")
PostTodo = pydantic_model_creator(Todo, name="TodoPost", exclude=("id",))
PutTodo = pydantic_model_creator(Todo, name="TodoPut", exclude=("id",))
