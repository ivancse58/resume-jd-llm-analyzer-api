from pydantic import BaseModel
from typing import Any, Optional, Dict

class ParsedSection(BaseModel):
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    raw_text: Optional[str] = None
    exception: Optional[str] = None

class EvaluationResponse(BaseModel):
    resume_info: ParsedSection
    job_description_info: ParsedSection
    evaluation: ParsedSection
