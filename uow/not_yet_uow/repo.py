from abc import ABC

from uow.not_yet_uow.DTO import ManagerBindEntity, ClientEntity


class AbstractClientRepository(ABC):

    def save(self, client: ClientEntity) -> None:
        """Создание клиента."""


class AbstractManagerBindRepository(ABC):
    def save(self, manager_bind: ManagerBindEntity) -> None:
        """Создание привязки менеджера к клиенту."""