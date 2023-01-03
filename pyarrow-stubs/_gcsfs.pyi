import collections.abc
import datetime
from typing import (
    Any,
    ClassVar,
)

import pyarrow._fs
import pyarrow.lib

class GcsFileSystem(pyarrow._fs.FileSystem):
    default_bucket_location: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def _expiration_datetime_from_options(self) -> Any: ...
    @classmethod
    def _reconstruct(cls, typecls, kwargs) -> Any: ...
    def __reduce__(self) -> Any: ...

class KeyValueMetadata(pyarrow.lib._Metadata, collections.abc.Mapping):
    __hash__: ClassVar[None] = ...  # type: ignore
    def __init__(self, *args, **kwargs) -> None: ...
    def equals(self, KeyValueMetadataother) -> Any: ...
    def get_all(self, key) -> Any: ...
    def items(self) -> Any: ...
    def key(self, i) -> Any: ...
    def keys(self) -> Any: ...
    def to_dict(self) -> Any: ...
    def value(self, i) -> Any: ...
    def values(self) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __iter__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __len__(self) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class timedelta:
    max: ClassVar[datetime.timedelta] = ...
    min: ClassVar[datetime.timedelta] = ...
    resolution: ClassVar[datetime.timedelta] = ...
    days: Any
    microseconds: Any
    seconds: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def total_seconds(self, *args, **kwargs) -> Any: ...
    def __abs__(self) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __bool__(self) -> Any: ...
    def __divmod__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __floordiv__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mod__(self, other) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __neg__(self) -> Any: ...
    def __pos__(self) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def __rdivmod__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __rfloordiv__(self, other) -> Any: ...
    def __rmod__(self, other) -> Any: ...
    def __rmul__(self, other) -> Any: ...
    def __rsub__(self, other) -> Any: ...
    def __rtruediv__(self, other) -> Any: ...
    def __sub__(self, other) -> Any: ...
    def __truediv__(self, other) -> Any: ...

class timezone(datetime.tzinfo):
    max: ClassVar[datetime.timezone] = ...
    min: ClassVar[datetime.timezone] = ...
    utc: ClassVar[datetime.timezone] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def dst(self, *args, **kwargs) -> Any: ...
    def fromutc(self, *args, **kwargs) -> Any: ...
    def tzname(self, *args, **kwargs) -> Any: ...
    def utcoffset(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __getinitargs__(self) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...

def ensure_metadata(meta, boolallow_none=...) -> KeyValueMetadata: ...
def frombytes(*args, **kwargs) -> Any: ...
def tobytes(o) -> Any: ...
