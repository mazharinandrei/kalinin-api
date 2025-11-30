class RuleSpec:
    CREATE_DESCRIPTION = ""
    DETAIL_DESCRIPTION = ""
    LIST_DESCRIPTION = ""
    UPDATE_DESCRIPTION = ""
    EXTEND_DESCRIPTION = ""
    DELETE_DESCRIPTION = ""

    CREATE_TRIGGER_EXAMPLES = [" hi ", " hello ", " hey "]
    CREATE_REPLY_OPTIONS_EXAMPLES = [" hi ", " hello ", " hey "]

    EXTEND_TRIGGER_EXAMPLES = [" hi ", " hello ", " hey "]
    EXTEND_REPLY_OPTIONS_EXAMPLES = [" hi ", " hello ", " hey "]


class UniversalReplySpec:
    CREATE_DESCRIPTION = ""
    DETAIL_DESCRIPTION = ""
    LIST_DESCRIPTION = ""
    UPDATE_DESCRIPTION = ""
    DELETE_DESCRIPTION = ""

    TEXT_EXAMPLE = "Try asking another question"


class ProcessMessageSpec:
    DESCRIPTION = ""
    INPUT_MESSAGE_EXAMPLE = "hi!"
    RESPONSES = {
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "example": {
                        "data": {
                            "id": 1,
                            "text": "Hello, how can I help you?",
                        },
                    },
                },
            },
        },
    }
