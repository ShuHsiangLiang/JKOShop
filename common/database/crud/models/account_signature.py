from pydantic import BaseModel


class AccountSignatureBase(BaseModel):
    pass


class AccountSignatureCreate(AccountSignatureBase):
    AccountID: str
    Status: int
    Token: str
    PKCS7Signatures: str
    PKCS7CAResults: str
    CreateTime: str


class AccountSignatureUpdate(AccountSignatureBase):
    pass
