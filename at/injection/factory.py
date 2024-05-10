from typing import Callable, Optional, get_type_hints, Type, TypeVar
from dataclasses import dataclass
from at.exceptions import InjectableDefinitionError

# Sentinel to detect undefined function argument.
UNDEFINED_FUNCTION = object()

T = TypeVar('T')


@dataclass
class Dependency:
    type_: Type[T]
    object_: T
    parameters: dict[str, Type]
    alias: str | None = None


class Injectable:
    dependencies = {}

    def __init__(self, func=UNDEFINED_FUNCTION, *, alias: Optional[str] = None):
        self._alias = alias
        self.decorated = UNDEFINED_FUNCTION
        if func is not UNDEFINED_FUNCTION:
            self.decorate(func)     # noqa

    def decorate(self, func: Callable) -> "Injectable":
        if not callable(func):
            raise TypeError(f"Cannot decorate non callable object {func}")
        self.decorated = func
        self.register_dependency()
        return self

    def __call__(self, *args, **kwargs):
        if self.decorated is UNDEFINED_FUNCTION:
            func = args[0]
            if args[1:] or kwargs:
                raise ValueError(
                    "Cannot decorate and setup simultaneously "
                    "with __call__(). Use __init__() for setup. "
                    "Use __call__() or decorate() to decorate."
                )
            self.decorate(func)
            return self
        else:
            self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        return self.decorated(*args, **kwargs)  # noqa

    def register_dependency(self):
        """
        TODO: Raise when dependency has already defined
        TODO: Create an interface (Dependency) for dependencies container.
        """
        hints = get_type_hints(self.decorated)
        if hints.get("return"):
            # We assume the last item is `return`
            _, type_ = hints.popitem()
            kwargs = {}
            for arg, a_type in hints.items():
                if a_type in self.dependencies:
                    kwargs[arg] = self.dependencies[a_type]["object"]
                else:
                    raise InjectableDefinitionError(f"Cannot inject parameter in {arg} in {self.decorated}")
            self.dependencies[type_] = {"object": self.run(**kwargs)}
        else:
            raise InjectableDefinitionError(f"{self.decorated} injectable has not defined type.")


class Autowired:
    def __init__(self, getter, setter=None):
        self._getter = getter
        self._setter = setter
        self.__name__ = getter.__name__
        # TODO: refactor
        dependency = Injectable.dependencies.get(get_type_hints(getter).get("return")) or {}
        self.value = dependency.get("object")

    def __get__(self, instance, owner=None):
        if self._getter(instance):
            raise  # TODO
        return self.value

    def __set__(self, instance, value):
        raise   # TODO
