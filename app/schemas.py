from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EngagementPostBase(BaseModel):
    tenant_id: int
    description: Optional[str] = None
    created_by: Optional[str] = None

class EngagementPostCreate(EngagementPostBase):
    pass

class EngagementPostUpdate(BaseModel):
    description: Optional[str] = None

class EngagementPostResponse(EngagementPostBase):
    enagement_post_id: int
    number_of_likes: Optional[int] = None
    number_of_shares: Optional[int] = None
    tenant_id: int
    created_on: Optional[datetime] = None
    updated_on: Optional[datetime] = None

    class Config:
        orm_mode = True



class PostContentBase(BaseModel):
    file_type: str
    story_id: int
    url: str
    thumbnail_url: Optional[str] = None
    sequence: Optional[int] = None 

class PostContentCreate(PostContentBase):
    pass

class PostContentResponse(PostContentBase):
    engagement_post_content_id: int

    class Config:
        orm_mode = True



class ProductMappingBase(BaseModel):
    engagement_post_id: int
    product_id: int

class ProductMappingCreate(ProductMappingBase):
    pass

class ProductMappingResponse(ProductMappingBase):
    engagement_post_product_mapping_id: int

    class Config:
        orm_mode = True



class PostProductBase(BaseModel):
    product_name: str
    product_image: Optional[str] = None
    sku: Optional[str] = None

class PostProductCreate(PostProductBase):
    pass

class PostProductResponse(PostProductBase):
    product_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class CollectionBase(BaseModel):
    collection_name: str

class CollectionCreate(CollectionBase):
    pass

class CollectionResponse(CollectionBase):
    collection_id: int

    class Config:
        orm_mode = True



class EngagementPostCollectionBase(BaseModel):
    enagement_post_id: int
    collection_id: int
    duration_in_seconds: Optional[int] = None

class EngagementPostCollectionCreate(EngagementPostCollectionBase):
    pass

class EngagementPostCollectionResponse(EngagementPostCollectionBase):
    engagement_post_collection_id: int

    class Config:
        orm_mode = True



class TopViewedPostResponse(BaseModel):
    tenant_id: int
    description: Optional[str] = None
    created_by: Optional[str] = None
    number_of_likes: Optional[int] = None
    number_of_shares: Optional[int] = None

    class Config:
        orm_mode = True

class TopViewedProductResponse(BaseModel):
    name: Optional[str] = None
    content_url: Optional[str] = None
    duration_in_seconds: float

    class Config:
        orm_mode = True
