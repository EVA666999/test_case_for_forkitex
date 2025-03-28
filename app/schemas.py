from pydantic import BaseModel


class BalanceCreateRequest(BaseModel):
    tron_address: str
