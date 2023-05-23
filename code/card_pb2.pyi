from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateCardRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateCardResponse(_message.Message):
    __slots__ = ["card"]
    CARD_FIELD_NUMBER: _ClassVar[int]
    card: Card
    def __init__(self, card: _Optional[_Union[Card, _Mapping]] = ...) -> None: ...

class Card(_message.Message):
    __slots__ = ["id", "name"]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...

class GetCardsRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCardsResponse(_message.Message):
    __slots__ = ["cards"]
    CARDS_FIELD_NUMBER: _ClassVar[int]
    cards: _containers.RepeatedCompositeFieldContainer[Card]
    def __init__(self, cards: _Optional[_Iterable[_Union[Card, _Mapping]]] = ...) -> None: ...
