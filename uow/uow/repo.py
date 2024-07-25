from abc import ABC

from uow.uow.DTO import ClientEntity, ManagerBindEntity


class AbstractClientRepository(ABC):

    def save(self, client: ClientEntity) -> None:
        """Создание клиента."""


class AbstractManagerRepository(ABC):
    def save(self, manager_bind: ManagerBindEntity) -> None:
        """Создание привязки менеджера к клиенту."""