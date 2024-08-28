class ConfigConstants:
    DATABASE_URL = "sqlite+aiosqlite:///./Notes.db"


class ErrConstants:
    NAME_IS_BUSY = "This name is already occupied"
    NOT_FOUND = "Not Found"
    PASSWORD_TOO_SHORT = "Password should be at least 3 characters"
    EMAIL_IN_PASSWORD = "Password should not contain e-mail"
