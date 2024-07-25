from uow.uow.DTO import ClientDTO, ClientEntity, ManagerBindDTO
from uow.uow.uow import AbstractCreatePartnerUoW


class CreatePartnerUseCase:
    """Создание клиента с привязкой менеджера."""

    def __init__(self, unit_of_work: AbstractCreatePartnerUoW)
        self._unit_of_work = unit_of_work

    def execute(self, manager_id: int, client_data: ClientDTO) -> None:
        client = ClientEntity(
            fio=client_data.fio,
            age=client_data.age,
            description=client_data.description,
            mobile=client_data.mobile,
            email=client_data.email,
        )

        with self._unit_of_work as uow:
            uow.client_repository.save(client)
            manager_bind = ManagerBindDTO(
                manager_id=manager_id,
                client_id=client.id,
            )
            uow.manager_bind_repository.save(manager_bind)