from dataclasses import dataclass


@dataclass
class ClientDTO:
    fio: str
    age: int
    description: str
    mobile: str
    email: str


@dataclass
class ClientEntity:
    id: int | None
    fio: str
    age: int
    description: str
    mobile: str
    email: str


@dataclass
class ManagerBindDTO:
    manager_id: int
    client_id: int


@dataclass
class ManagerBindEntity:
    id: int | None
    manager_id: int
    client_id: int


