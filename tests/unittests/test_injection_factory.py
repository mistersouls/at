import pytest

from at.exceptions import InjectableDefinitionError
from at.injection.factory import Injectable, Autowired


class MyService:
    ...


class MyService2:
    ...


def test_injectable():
    """
    TODO: Comment and refactor this test
    :return:
    """
    @Injectable(alias="yourfunction")
    def func_with_alias() -> MyService:
        return MyService()

    @Injectable
    def func_without_alias() -> MyService:
        return MyService()

    @Injectable
    def func2() -> MyService2:
        return MyService2()

    @Injectable
    def func_with_valid_args(s2: MyService2) -> MyService:
        return MyService()

    with pytest.raises(InjectableDefinitionError):
        @Injectable
        def func_with_args(a: str, b: int) -> MyService:
            return MyService()

    with pytest.raises(InjectableDefinitionError):
        @Injectable
        def func_without_type():
            return MyService()

    assert MyService in Injectable.dependencies
    assert MyService2 in Injectable.dependencies


def test_autowired():
    @Injectable
    def my_service() -> MyService:
        return MyService()

    class MyInjectedClass:
        @Autowired
        def service(self) -> MyService:
            ...

    injected = MyInjectedClass()
    assert isinstance(injected.service, MyService)
