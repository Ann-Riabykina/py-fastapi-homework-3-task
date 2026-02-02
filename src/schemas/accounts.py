from pydantic import BaseModel, EmailStr, field_validator

from database import accounts_validators


class MessageResponseSchema(BaseModel):
    message: str


class UserRegistrationRequestSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: EmailStr) -> str:
        return accounts_validators.validate_email(str(v).lower())

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        return accounts_validators.validate_password_strength(v)


class UserRegistrationResponseSchema(BaseModel):
    id: int
    email: EmailStr


class ActivateAccountRequestSchema(BaseModel):
    email: EmailStr
    token: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: EmailStr) -> str:
        return accounts_validators.validate_email(str(v).lower())


class ActivateAccountResponseSchema(BaseModel):
    message: str


class PasswordResetRequestSchema(BaseModel):
    email: EmailStr

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: EmailStr) -> str:
        return accounts_validators.validate_email(str(v).lower())


class PasswordResetRequestResponseSchema(BaseModel):
    message: str


class PasswordResetCompleteRequestSchema(BaseModel):
    email: EmailStr
    token: str
    password: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: EmailStr) -> str:
        return accounts_validators.validate_email(str(v).lower())

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        return accounts_validators.validate_password_strength(v)


class PasswordResetCompleteResponseSchema(BaseModel):
    message: str


class LoginRequestSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: EmailStr) -> str:
        return accounts_validators.validate_email(str(v).lower())


class LoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class RefreshAccessTokenRequestSchema(BaseModel):
    refresh_token: str


class RefreshAccessTokenResponseSchema(BaseModel):
    access_token: str


UserActivationRequestSchema = ActivateAccountRequestSchema
UserActivationResponseSchema = ActivateAccountResponseSchema

PasswordResetTokenRequestSchema = PasswordResetRequestSchema
PasswordResetTokenResponseSchema = PasswordResetRequestResponseSchema

UserLoginRequestSchema = LoginRequestSchema
UserLoginResponseSchema = LoginResponseSchema
