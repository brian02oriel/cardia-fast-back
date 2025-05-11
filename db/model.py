from typing import Annotated, Any, Optional

from bson import ObjectId
from pydantic import BaseModel, BeforeValidator, Field

def object_id_to_str(v: Any) -> str:
    if isinstance(v, ObjectId):
        return str(v)
    return v

ObjectIdAnnotation = Annotated[str, BeforeValidator(object_id_to_str)]

class MongoBaseModel(BaseModel):   
    id: Optional[ObjectIdAnnotation] = Field(
        default_factory=ObjectId, 
        alias="_id",
        serialization_alias="id"  # tells Pydantic to use "id" as the field name when serializing the model to JSON
    )
    
    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
    }
