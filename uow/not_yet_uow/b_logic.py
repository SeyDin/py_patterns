from uow.not_yet_uow.DTO import ClientDTO, ClientEntity, ManagerBindDTO

from uow.not_yet_uow.repo import AbstractClientRepository, AbstractManagerBindRepository


class CreatePartnerUseCase:

    def __init__(
            self,
            client_repository: AbstractClientRepository,
            manager_bind_repository: AbstractManagerBindRepository,
    ):
        self._client_repository = client_repository
        self._manager_bind_repository = manager_bind_repository

    def execute(self, manager_id: int, client_data: ClientDTO) -> None:
        client = ClientEntity(
            fio=client_data.fio,
            age=client_data.age,
            description=client_data.description,
            mobile=client_data.mobile,
            email=client_data.email,
        )

        self._client_repository.save(client)
        manager_bind = ManagerBindDTO(manager_id=manager_id, client_id=client.id)
        self._manager_bind_repository.save(manager_bind)
