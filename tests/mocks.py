from nad_ch.domain.entities import DataProvider
from nad_ch.domain.repositories import DataProviderRepository


class MockDataProviderRepository(DataProviderRepository):
    def __init__(self) -> None:
        self._providers = set()

    def add(self, provider: DataProvider) -> None:
        self._providers.add(provider)

    def get_by_name(self, name: str) -> DataProvider:
        return next(p for p in self._providers if p.name == name)

    def get_all(self):
        return list(self._providers)
