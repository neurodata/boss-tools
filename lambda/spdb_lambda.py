#!/usr/bin/env python3.4
# This lambda tests that it can read from user-data, and access the cache_state_db
# then import spdb and access the compiled c_lib
#
print("in s3_flush_lambda")
import bossutils
import spdb
from spdb.spatialdb import state
print("finished part1 imports")

my_state = state.CacheStateDB({ "cache_state_host": "cache-state.hiderrt1.boss", "cache_state_db": 0 })
my_state.add_cache_misses(["6","4","3"])
print("finished part1")

print("checking c_lib")
from spdb.c_lib import ndlib
print("finished c_lib imports.")
id = ndlib.MortonXYZ(10)
print("results:")
for w in id:
   print(str(w))
print("finished part2")
