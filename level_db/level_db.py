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

def get_data_folder() -> str:
    return os.path.abspath(os.path.dirname(__file__)) + "/data"

class level_db:
    def __init__(self, db_path: str) -> None:
        if sys.platform == "win32":
            if platform.machine() == "x86":
                self.lib: object = ctypes.cdll.LoadLibrary(get_data_folder() + "/level_db_win_x86_32.dll")
            elif platform.machine() == "x86_64":
                self.lib: object = ctypes.cdll.LoadLibrary(get_data_folder() + "/level_db_win_x86_64.dll")
        elif sys.platform == "linux":
            if platform.machine() == "x86_64":
                self.lib: object = ctypes.cdll.LoadLibrary(get_data_folder() + "/level_db_linux_x86_64.so")
        else:
            raise Exception("Unknown OS or architecture")
        level_db.set_default_args(self.lib)
        filter_policy = self.lib.leveldb_filterpolicy_create_bloom(10)
        cache = self.lib.leveldb_cache_create_lru(40 * 1024 * 1024)
        options = self.lib.leveldb_options_create()
        self.lib.leveldb_options_set_compression(options, 4)
        self.lib.leveldb_options_set_filter_policy(options, filter_policy)
        self.lib.leveldb_options_set_create_if_missing(options, False)
        self.lib.leveldb_options_set_write_buffer_size(options, 4 * 1024 * 1024)
        self.lib.leveldb_options_set_cache(options, cache)
        self.lib.leveldb_options_set_block_size(options, 163840)
