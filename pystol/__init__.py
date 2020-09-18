import os
from pystol.util import ModuleNotFoundIgnore

file_sep = os.path.sep

from py2store.util import lazyprop, groupby, regroupby, igroupby
from py2store.trans import add_ipython_key_completions

# Imports to be able to easily get started...
from py2store.base import (
    Collection,
    KvReader,
    KvPersister,
    Reader,
    Persister,
    kv_walk,
)

from py2store.base import Store
from py2store.trans import (
    wrap_kvs,
    disable_delitem,
    disable_setitem,
    mk_read_only,
    kv_wrap,
    cached_keys,
    filt_iter,
    filtered_iter,
    add_path_get,
    insert_aliases,
)

from py2store.caching import (
    mk_cached_store,
    store_cached,
    store_cached_with_single_key,
    ensure_clear_to_kv_store,
    flush_on_exit,
    mk_write_cached_store,
)

from py2store.slib.s_zipfile import (
    ZipReader,
    ZipFilesReader,
    FilesOfZip,
    FlatZipFilesReader,
)


def kvhead(store, n=1):
    """Get the first item of a kv store, or a list of the first n items"""
    if n == 1:
        for k in store:
            return k, store[k]
    else:
        return [(k, store[k]) for i, k in enumerate(store) if i < n]


def ihead(store, n=1):
    """Get the first item of an iterable, or a list of the first n items"""
    if n == 1:
        for item in iter(store):
            return item
    else:
        return [item for i, item in enumerate(store) if i < n]
