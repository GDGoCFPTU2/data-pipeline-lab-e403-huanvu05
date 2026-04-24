from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    TODO: Khai báo các trường với kiểu dữ liệu str ở dưới.
    """
    document_id: str = Field(..., description="Unique identifier for the document")
    source_type: str = Field(..., description="Type of source: 'PDF' or 'Video'")
    author: str = Field(..., description="Author or creator of the document")
    category: str = Field(..., description="Category or topic of the document")
    content: str = Field(..., description="Main content of the document")
    timestamp: str = Field(..., description="Timestamp of document creation/publication")
