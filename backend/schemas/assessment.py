from pydantic import BaseModel


class AssessmentResponse(BaseModel):
    emotional_state: str
    consciousness_level: int
    confidence: float
    reasoning: str