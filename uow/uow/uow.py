from abc import ABC, abstractmethod

from uow.uow.repo import AbstractClientRepository, AbstractManagerRepository


class AbstractCreatePartnerUoW(ABC):
    @property
    @abstractmethod
    def client_repository(self) -> AbstractClientRepository:
        raise NotImplementedError()

    @property
    @abstractmethod
    def manager_bind_repository(self) -> AbstractManagerRepository:
        raise NotImplementedError()

    @abstractmethod
    def __enter__(self) -> AbstractCreatePartnerUoW:
        raise NotImplementedError()

    @abstractmethod
    def __exit__(exc_type, exc_val, traceback) -> bool:
        raise NotImplementedError


