
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel

class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str, Enum):
    admin = "admin"
    user = "user"
    
class User(BaseModel): # ユーザー情報
    id: Optional[UUID] = uuid4() # ランダムに出力
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[str]
    gender: Gender
    roles: Optional[List[Role]]

class UpdateUser(BaseModel): # ユーザー情報の更新
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[str]
    roles: Optional[List[Role]]