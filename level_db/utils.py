################################################################################
#                                                                              #
#  ____           _                                                            #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                                        #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                                       #
# |  __/ (_) | (_| | |  | |_| | | | | | |                                      #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|                                      #
#                                                                              #
# Copyright 2021 Podrum Studios                                                #
#                                                                              #
# Permission is hereby granted, free of charge, to any person                  #
# obtaining a copy of this software and associated documentation               #
# files (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,         #
# publish, distribute, sublicense, and/or sell copies of the Software,         #
# and to permit persons to whom the Software is furnished to do so,            #
# subject to the following conditions:                                         #
#                                                                              #
# The above copyright notice and this permission notice shall be included      #
# in all copies or substantial portions of the Software.                       #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
#                                                                              #
################################################################################

import ctypes
import platform
import sys

class utils:
    @staticmethod
    def check_for_error(lib: object, error: str) -> None:
        if bool(error):
            message: str = ctypes.string_at(error)
            lib.leveldb_free(ctypes.cast(error, ctypes.c_void_p))
            raise Exception(message)
        
    @staticmethod
    def set_default_args(lib: object) -> None:
        lib.leveldb_filterpolicy_create_bloom.argtypes = [ctypes.c_int]
        lib.leveldb_filterpolicy_create_bloom.restype = ctypes.c_void_p
        lib.leveldb_filterpolicy_destroy.argtypes = [ctypes.c_void_p]
        lib.leveldb_filterpolicy_destroy.restype = None
        lib.leveldb_cache_create_lru.argtypes = [ctypes.c_size_t]
        lib.leveldb_cache_create_lru.restype = ctypes.c_void_p
        lib.leveldb_cache_destroy.argtypes = [ctypes.c_void_p]
        lib.leveldb_cache_destroy.restype = None
        lib.leveldb_options_create.argtypes = []
        lib.leveldb_options_create.restype = ctypes.c_void_p
        lib.leveldb_options_set_filter_policy.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        lib.leveldb_options_set_filter_policy.restype = None
        lib.leveldb_options_set_create_if_missing.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]
        lib.leveldb_options_set_create_if_missing.restype = None
        lib.leveldb_options_set_error_if_exists.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]
        lib.leveldb_options_set_error_if_exists.restype = None
        lib.leveldb_options_set_paranoid_checks.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]
        lib.leveldb_options_set_paranoid_checks.restype = None
        lib.leveldb_options_set_write_buffer_size.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
        lib.leveldb_options_set_write_buffer_size.restype = None
        lib.leveldb_options_set_max_open_files.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.leveldb_options_set_max_open_files.restype = None
        lib.leveldb_options_set_cache.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        lib.leveldb_options_set_cache.restype = None
        lib.leveldb_options_set_block_size.argtypes = [ctypes.c_void_p, ctypes.c_size_t]
        lib.leveldb_options_set_block_size.restype = None
        lib.leveldb_options_destroy.argtypes = [ctypes.c_void_p]
        lib.leveldb_options_destroy.restype = None
        lib.leveldb_options_set_compression.argtypes = [ctypes.c_void_p, ctypes.c_int]
        lib.leveldb_options_set_compression.restype = None
        lib.leveldb_open.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p]
        lib.leveldb_open.restype = ctypes.c_void_p
        lib.leveldb_close.argtypes = [ctypes.c_void_p]
        lib.leveldb_close.restype = None
        lib.leveldb_put.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p]
        lib.leveldb_put.restype = None
        lib.leveldb_delete.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p]
        lib.leveldb_delete.restype = None
        lib.leveldb_write.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
        lib.leveldb_write.restype = None
        lib.leveldb_get.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_void_p]
        lib.leveldb_get.restype = ctypes.POINTER(ctypes.c_char)
        lib.leveldb_writeoptions_create.argtypes = []
        lib.leveldb_writeoptions_create.restype = ctypes.c_void_p
        lib.leveldb_writeoptions_destroy.argtypes = [ctypes.c_void_p]
        lib.leveldb_writeoptions_destroy.restype = None
        lib.leveldb_writeoptions_set_sync.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]
        lib.leveldb_writeoptions_set_sync.restype = None
        lib.leveldb_readoptions_create.argtypes = []
        lib.leveldb_readoptions_create.restype = ctypes.c_void_p
        lib.leveldb_readoptions_destroy.argtypes = [ctypes.c_void_p]
        lib.leveldb_readoptions_destroy.restype = None
        lib.leveldb_readoptions_set_verify_checksums.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]
        lib.leveldb_readoptions_set_verify_checksums.restype = None
        lib.leveldb_readoptions_set_fill_cache.argtypes = [ctypes.c_void_p, ctypes.c_ubyte]
        lib.leveldb_readoptions_set_fill_cache.restype = None
        lib.leveldb_readoptions_set_snapshot.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        lib.leveldb_readoptions_set_snapshot.restype = None
        lib.leveldb_create_iterator.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        lib.leveldb_create_iterator.restype = ctypes.c_void_p
        lib.leveldb_iter_destroy.argtypes = [ctypes.c_void_p]
        lib.leveldb_iter_destroy.restype = None
        lib.leveldb_iter_valid.argtypes = [ctypes.c_void_p]
        lib.leveldb_iter_valid.restype = ctypes.c_bool
        lib.leveldb_iter_key.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t)]
        lib.leveldb_iter_key.restype = ctypes.c_void_p
        lib.leveldb_iter_value.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_size_t)]
        lib.leveldb_iter_value.restype = ctypes.c_void_p
        lib.leveldb_iter_next.argtypes = [ctypes.c_void_p]
        lib.leveldb_iter_next.restype = None
        lib.leveldb_iter_prev.argtypes = [ctypes.c_void_p]
        lib.leveldb_iter_prev.restype = None
        lib.leveldb_iter_seek_to_first.argtypes = [ctypes.c_void_p]
        lib.leveldb_iter_seek_to_first.restype = None
        lib.leveldb_iter_seek_to_last.argtypes = [ctypes.c_void_p]
        lib.leveldb_iter_seek_to_last.restype = None
        lib.leveldb_iter_seek.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
        lib.leveldb_iter_seek.restype = None
        lib.leveldb_iter_get_error.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        lib.leveldb_iter_get_error.restype = None
        lib.leveldb_writebatch_create.argtypes = []
        lib.leveldb_writebatch_create.restype = ctypes.c_void_p
        lib.leveldb_writebatch_destroy.argtypes = [ctypes.c_void_p]
        lib.leveldb_writebatch_destroy.restype = None
        lib.leveldb_writebatch_clear.argtypes = [ctypes.c_void_p]
        lib.leveldb_writebatch_clear.restype = None
        lib.leveldb_writebatch_put.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t]
        lib.leveldb_writebatch_put.restype = None
        lib.leveldb_writebatch_delete.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
        lib.leveldb_writebatch_delete.restype = None
        lib.leveldb_approximate_sizes.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
        lib.leveldb_approximate_sizes.restype = None
        lib.leveldb_compact_range.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t]
        lib.leveldb_compact_range.restype = None
        lib.leveldb_create_snapshot.argtypes = [ctypes.c_void_p]
        lib.leveldb_create_snapshot.restype = ctypes.c_void_p
        lib.leveldb_release_snapshot.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        lib.leveldb_release_snapshot.restype = None
        lib.leveldb_free.argtypes = [ctypes.c_void_p]
        lib.leveldb_free.restype = None
        
    @staticmethod
    def get_data_folder() -> str:
        return os.path.abspath(os.path.dirname(__file__)) + "/data"
