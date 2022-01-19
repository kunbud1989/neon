from pydantic import BaseModel
from typing import List, Dict

class Postgres(BaseModel):
    host: str ='172.17.0.3'
    port: int = 5432
    username: str ='postgres'
    password: str ='neonB'
    db: str ='postgres'

class Salt(BaseModel):
    salt: str = ''

class ConfigApps(BaseModel):
    ENVIRONMENT: str = ''
    APPS_INFORMATION: Dict = {}
    ALLOWED_HOSTS: List[str] = []
    ALLOW_METHODS: List[str]  = []
    API_TOKEN: List[str]  = []
    DATABASE: Postgres
    SALT: Salt