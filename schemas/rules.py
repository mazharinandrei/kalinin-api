from pydantic import BaseModel, Field

from api.v1.api_spec import RuleSpec


class CreateRule(BaseModel):
    triggers: list[str] = Field(
        min_length=1,
        examples=[RuleSpec.CREATE_TRIGGER_EXAMPLES],
    )
    reply_options: list[str] = Field(
        min_length=1,
        examples=[RuleSpec.CREATE_REPLY_OPTIONS_EXAMPLES],
    )


class ExtendRule(BaseModel):
    triggers: list[str] | None = None
    reply_options: list[str] | None = None
