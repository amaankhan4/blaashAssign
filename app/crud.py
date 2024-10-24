from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

# CRUD for EngagementPost
def get_engagement_post(db: Session, tenant_id: int):
    post = db.query(models.EngagementPost).filter(models.EngagementPost.tenant_id == tenant_id).all()
    return post

def create_engagement_post(db: Session, post: schemas.EngagementPostCreate):
    db_post = models.EngagementPost(
        tenant_id=post.tenant_id,
        description=post.description,
        created_by=post.created_by,
        created_on=datetime.now(),
        content_type=post.content_type
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_engagement_post(db: Session, post_id: int, post: schemas.EngagementPostUpdate):
    db_post = db.query(models.EngagementPost).filter(models.EngagementPost.enagement_post_id == post_id).first()
    if db_post:
        db_post.description = post.description
        db_post.updated_on = datetime.now()
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_engagement_post(db: Session, post_id: int):
    db_post = db.query(models.EngagementPost).filter(models.EngagementPost.enagement_post_id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post

# CRUD for PostContent
def get_post_content(db: Session, content_id: int):
    return db.query(models.PostContent).filter(models.PostContent.engagement_post_content_id == content_id).first()

def create_post_content(db: Session, content: schemas.PostContentCreate):
    db_content = models.PostContent(
        file_type=content.file_type,
        story_id=content.story_id,
        url=content.url
    )
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content

# CRUD for ProductMapping
def create_product_mapping(db: Session, mapping: schemas.ProductMappingCreate):
    db_mapping = models.ProductMapping(
        engagement_post_id=mapping.engagement_post_id,
        product_id=mapping.product_id
    )
    db.add(db_mapping)
    db.commit()
    db.refresh(db_mapping)
    return db_mapping

# CRUD for PostProduct
def get_post_product(db: Session, product_id: int):
    return db.query(models.PostProduct).filter(models.PostProduct.product_id == product_id).first()

def create_post_product(db: Session, product: schemas.PostProductCreate):
    db_product = models.PostProduct(
        product_name=product.product_name,
        product_image=product.product_image,
        sku=product.sku,
        created_at=datetime.now()
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# CRUD for Collection
def create_collection(db: Session, collection: schemas.CollectionCreate):
    db_collection = models.Collection(
        collection_name=collection.collection_name
    )
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)

    # Map posts to the collection
    for post_id in collection.post_ids:
        post_collection = models.EngagementPostCollection(
            enagement_post_id=post_id,
            collection_id=db_collection.collection_id,
        )
        db.add(post_collection)
    
    db.commit()
    return db_collection


# CRUD for EngagementPostCollection
def create_engagement_post_collection(db: Session, mapping: schemas.EngagementPostCollectionCreate):
    db_mapping = models.EngagementPostCollection(
        enagement_post_id=mapping.enagement_post_id,
        collection_id=mapping.collection_id,
        duration_in_seconds=mapping.duration_in_seconds
    )
    db.add(db_mapping)
    db.commit()
    db.refresh(db_mapping)
    return db_mapping

def get_top_viewed_posts(db: Session, tenant_id: int):
    return db.query(models.EngagementPost) \
        .filter(models.EngagementPost.tenant_id == tenant_id) \
        .order_by(models.EngagementPost.number_of_likes.desc()) \
        .limit(5) \
        .all()

def get_top_viewed_products(db: Session, tenant_id: int):
    return db.query(models.PostProduct, models.EngagementPostCollection.duration_in_seconds) \
        .join(models.ProductMapping, models.ProductMapping.product_id == models.PostProduct.product_id) \
        .join(models.EngagementPost, models.EngagementPost.enagement_post_id == models.ProductMapping.engagement_post_id) \
        .filter(models.EngagementPost.tenant_id == tenant_id) \
        .order_by(models.EngagementPostCollection.duration_in_seconds.desc()) \
        .limit(5) \
        .all()

