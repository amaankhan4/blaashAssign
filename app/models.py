from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, ARRAY, BigInteger, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class EngagementPost(Base):
    __tablename__ = "engagement_post"
    enagement_post_id = Column(BigInteger, primary_key=True, index=True,nullable=False)
    tenant_id = Column(BigInteger, nullable=False)
    number_of_likes = Column(BigInteger)
    number_of_shares = Column(BigInteger)
    description = Column(String)
    created_by = Column(String)
    created_on = Column(DateTime(timezone=True))
    updated_by = Column(String)
    updated_on = Column(DateTime(timezone=True))
    customer_interaction_date = Column(DateTime(timezone=True))
    shopping_url = Column(String)
    customers_who_liked = Column(String)
    content_type = Column(String, nullable=False)
    Inflencer_id = Column(BigInteger)
    tags = Column(ARRAY(String))
    thumbnail_url = Column(String)
    thumbnail_title = Column(String)
    product_thumbnail_url = Column(String)
    content_type = Column(String)
    title = Column(String)
    content_url = Column(String)

class PostContent(Base):
    __tablename__ = "engagement_post_content"
    engagement_post_content_id = Column(BigInteger, primary_key=True, index=True,nullable=False)
    file_type = Column(String,nullable=False)
    story_id = Column(BigInteger,nullable=False)
    url = Column(String,nullable=False)
    thumbnail_url = Column(String)
    sequence = Column(Integer)

class ProductMapping(Base):
    __tablename__ = "engagement_post_product_mapping"
    engagement_post_product_mapping_id = Column(BigInteger, primary_key=True, index=True)
    engagement_post_id = Column(BigInteger, ForeignKey("engagement_post.engagement_post_id"), nullable=False)
    product_id = Column(BigInteger, ForeignKey("engagement_post_product.product_id"), nullable=False)

class PostProduct(Base):
    __tablename__ = "engagement_post_product"
    product_id = Column(BigInteger, primary_key=True, index=True)
    product_name = Column(String,nullable=False)
    product_image = Column(String)
    sku = Column(String)
    created_at = Column(DateTime(timezone=True))
    updated_at = Column(DateTime(timezone=True))

class Collection(Base):
    __tablename__ = "collection"
    collection_id = Column(Integer, primary_key=True, index=True)
    collection_name = Column(String)
    engagement_post_collection_id = Column(BigInteger, ForeignKey("engagement_post_collection.engagement_post_collection_id"))
    
class EngagementPostCollection(Base):
    __tablename__ = "engagement_post_collection"
    engagement_post_collection_id = Column(Integer, primary_key=True, index=True)
    enagement_post_id = Column(Integer, ForeignKey("engagement_post.enagement_post_id"))
    collection_id = Column(Integer, ForeignKey("collection.collection_id"))
    duration_in_seconds = Column(BigInteger)
