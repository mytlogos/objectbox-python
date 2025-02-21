# Copyright 2019-2021 ObjectBox Ltd. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from objectbox.c import *
from contextlib import contextmanager


@contextmanager
def read(ob: 'ObjectBox'):
    tx = obx_txn_read(ob._c_store)
    try:
        yield
    finally:
        obx_txn_close(tx)


@contextmanager
def write(ob: 'ObjectBox'):
    tx = obx_txn_write(ob._c_store)
    try:
        yield
        obx_txn_success(tx)
    except:
        obx_txn_abort(tx)
        obx_txn_close(tx)
        raise
