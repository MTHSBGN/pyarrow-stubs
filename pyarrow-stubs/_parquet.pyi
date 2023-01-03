from typing import (
    Any,
    ClassVar,
    Generator,
)

import pyarrow.lib
from typing_extensions import Literal

_stringify_path: function
indent: function

class ArrowException(Exception): ...

class ColumnChunkMetaData(pyarrow.lib._Weakrefable):
    def __init__(self) -> None: ...
    def equals(self, other: ColumnChunkMetaData) -> bool: ...
    def to_dict(self) -> Any: ...
    def __eq__(self, other) -> bool: ...
    @property
    def file_offset(self) -> int: ...
    @property
    def file_path(self) -> str | None: ...
    @property
    def physical_type(self) -> str: ...
    @property
    def num_values(self) -> int: ...
    @property
    def path_in_schema(self) -> str: ...
    @property
    def is_stats_set(self) -> bool: ...
    @property
    def statistics(self) -> Statistics: ...
    @property
    def compression(
        self,
    ) -> Literal[
        "UNCOMPRESSED", "SNAPPY", "GZIP", "LZO", "BROTLI", "LZ4", "ZSTD", "UNKNOWN"
    ]: ...
    @property
    def encodings(
        self,
    ) -> tuple[
        Literal[
            "PLAIN",
            "BIT_PACKED",
            "RLE",
            "BYTE_STREAM_SPLIT",
            "DELTA_BINARY_PACKED",
            "DELTA_BYTE_ARRAY",
        ],
        ...,
    ]: ...
    @property
    def has_dictionary_page(self) -> bool: ...
    @property
    def dictionary_page_offset(self) -> int | None: ...
    @property
    def data_page_offset(self) -> int: ...
    @property
    def has_index_page(self) -> bool: ...
    @property
    def index_page_offset(self) -> int: ...
    @property
    def total_compressed_size(self) -> int: ...
    @property
    def total_uncompressed_size(self) -> int: ...

class ColumnSchema(pyarrow.lib._Weakrefable):
    def __init__(self, schema: ParquetSchema, index: int) -> None: ...
    def equals(self, other: ColumnSchema) -> Any: ...
    def __eq__(self, other) -> Any: ...
    @property
    def name(self) -> str: ...
    @property
    def path(self) -> str: ...
    @property
    def max_definition_level(self) -> int: ...
    @property
    def max_repetition_level(self) -> int: ...
    @property
    def physical_type(self) -> str: ...
    @property
    def logical_type(self) -> ParquetLogicalType: ...
    @property
    def converted_type(self) -> str | None: ...
    @property
    def length(self) -> int | None: ...
    @property
    def precision(self) -> int | None: ...
    @property
    def scale(self) -> int | None: ...

class ParquetLogicalType(pyarrow.lib._Weakrefable):
    type: Any
    def to_json(self) -> str: ...

class ParquetReader(pyarrow.lib._Weakrefable):
    _column_idx_map: dict[bytes, int] | None
    closed: bool
    column_paths: Any
    metadata: FileMetaData | None
    num_row_groups: int
    schema_arrow: pyarrow.lib.Schema
    @classmethod
    def __init__(self, memory_pool: pyarrow.lib.MemoryPool) -> None: ...
    def close(self) -> None: ...
    def column_name_idx(self, column_name: str) -> int: ...
    def iter_batches(
        self,
        batch_size: int,
        row_groups: list[int],
        column_indices: list[int] | None = ...,
        use_threads: bool = ...,
    ) -> Generator[pyarrow.lib.RecordBatch, None, None]: ...
    def open(
        self,
        source,
        *,
        use_memory_map: bool = ...,
        read_dictionary: list[str | int] | None = ...,
        metadata: FileMetaData = ...,
        buffer_size: int = ...,
        pre_buffer: bool = ...,
        coerce_int96_timestamp_unit: str | None = ...,
        decryption_properties: FileDecryptionProperties = ...,
        thrift_string_size_limit: int = ...,
        thrift_container_size_limit: int = ...,
    ) -> pyarrow.lib.Table: ...
    def read_all(
        self, column_indices: list[int] | None = ..., use_threads: bool = ...
    ) -> pyarrow.lib.Table: ...
    def read_column(self, column_index: int) -> pyarrow.lib.Array: ...
    def read_row_group(
        self, i: int, column_indices: list[int] | None = ..., use_threads: bool = ...
    ) -> pyarrow.lib.Table: ...
    def read_row_groups(
        self,
        row_groups: list[int],
        column_indices: list[int] | None = ...,
        use_threads: bool = ...,
    ) -> pyarrow.lib.Table: ...
    def scan_contents(
        self, column_indices: list[int] | None = ..., batch_size: int = ...
    ) -> int: ...
    def set_batch_size(self, batch_size: int) -> None: ...
    def set_use_threads(self, use_threads: bool) -> None: ...

class ParquetSchema(pyarrow.lib._Weakrefable):
    names: list[str]
    def __init__(self, container: FileMetaData) -> None: ...
    def column(self, i: int) -> ColumnSchema: ...
    def equals(self, other: ParquetSchema) -> bool: ...
    def to_arrow_schema(self) -> pyarrow.lib.Schema: ...
    def __eq__(self, other) -> bool: ...
    def __getitem__(self, i: int) -> ColumnSchema: ...
    def __len__(self) -> int: ...

class ParquetWriter(pyarrow.lib._Weakrefable):
    allow_truncated_timestamps: Any
    coerce_timestamps: Any
    column_encoding: Any
    compression: str | dict[str, str]
    compression_level: Any
    data_page_size: Any
    data_page_version: Any
    dictionary_pagesize_limit: Any
    encryption_properties: Any
    metadata: FileMetaData
    row_group_size: Any
    use_byte_stream_split: Any
    use_compliant_nested_type: Any
    use_deprecated_int96_timestamps: Any
    use_dictionary: bool | list[str]
    version: Any
    write_batch_size: Any
    write_statistics: Any
    writer_engine_version: Any
    def __init__(
        cls,
        where,
        schema: pyarrow.lib.Schema,
        use_dictionary: bool | list[str] | None = ...,
        compression: str | dict[str, str] = ...,
        version: str | None = ...,
        write_statistics: bool | list[str] | None = ...,
        memory_pool: pyarrow.lib.MemoryPool = ...,
        use_deprecated_int96_timestamps: bool = ...,
        coerce_timestamps: Literal["ms", "us"] | None = ...,
        data_page_size: int | None = ...,
        allow_truncated_timestamps: bool = ...,
        compression_level: int | dict[str, int] | None = ...,
        use_byte_stream_split: bool | list[str] = ...,
        column_encoding: str | dict[str, str] | None = ...,
        writer_engine_version: Literal["V1", "V2"] | None = ...,
        data_page_version: Literal["1.0", "2.0"] | None = ...,
        use_compliant_nested_type: bool = ...,
        encryption_properties: FileDecryptionProperties | None = ...,
        write_batch_size: int | None = ...,
        dictionary_pagesize_limit: int | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def write_table(
        self, table: pyarrow.lib.Table, row_group_size: int | None = ...
    ) -> None: ...

class RowGroupMetaData(pyarrow.lib._Weakrefable):
    __hash__: ClassVar[None] = ...  # type: ignore
    num_columns: Any
    num_rows: Any
    total_byte_size: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def column(self, inti) -> Any: ...
    def equals(self, RowGroupMetaDataother) -> Any: ...
    def to_dict(self) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

class Statistics(pyarrow.lib._Weakrefable):
    __hash__: ClassVar[None] = ...  # type: ignore
    converted_type: Any
    distinct_count: Any
    has_distinct_count: Any
    has_min_max: Any
    has_null_count: Any
    logical_type: Any
    max: Any
    max_raw: Any
    min: Any
    min_raw: Any
    null_count: Any
    num_values: Any
    physical_type: Any
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def equals(self, Statisticsother) -> Any: ...
    def to_dict(self) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state) -> Any: ...

class FileDecryptionProperties:
    def __init__(self, *args, **kwargs) -> None: ...

class FileEncryptionProperties:
    def __init__(self, *args, **kwargs) -> None: ...

class FileMetaData(pyarrow.lib._Weakrefable):
    __hash__: ClassVar[None] = ...  # type: ignore
    created_by: Any
    format_version: Any
    metadata: Any
    num_columns: Any
    num_row_groups: Any
    num_rows: Any
    schema: Any
    serialized_size: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def append_row_groups(self, FileMetaDataother) -> Any: ...
    def equals(self, FileMetaDataother) -> Any: ...
    def row_group(self, inti) -> Any: ...
    def set_file_path(self, path) -> Any: ...
    def to_dict(self) -> Any: ...
    def write_metadata_file(self, where) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...

def _datetime_from_int(int64_tvalue, TimeUnitunit, tzinfo=...) -> Any: ...
def _reconstruct_filemetadata(Bufferserialized) -> Any: ...
def frombytes(*args, **kwargs) -> Any: ...
def tobytes(o) -> Any: ...
