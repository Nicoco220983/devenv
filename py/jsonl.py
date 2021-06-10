import json
from contextlib import contextmanager


def read(stream, **kwargs):
    with _as_stream(stream, **kwargs) as _stream:
        for data in (json.loads(l) for l in _stream.readlines()):
            yield data


def write(datas, stream, mode="w"):
    with _as_stream(stream, mode=mode) as _stream:
        for data in datas:
            _stream.write(json.dumps(data, ensure_ascii=False) + "\n")


@contextmanager
def _as_stream(stream, **kwargs):
    if type(stream) is str:
        with open(stream, **kwargs) as res:
            yield res
    else:
        yield stream
