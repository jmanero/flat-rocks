{'targets': [{
    'target_name': 'leveldb'
  , 'variables': {
<<<<<<< ea5999dbd5fddf8f811b6c14162a3282b24ef7a9
        'ldbversion': '1.18.0'
=======
        'ldbversion': 'rocksdb'
>>>>>>> working rocksdb!
    }
  , 'type': 'static_library'
		# Overcomes an issue with the linker and thin .a files on SmartOS
  , 'standalone_static_library': 1
  , 'dependencies': [
        '../snappy/snappy.gyp:snappy'
    ]
  , 'direct_dependent_settings': {
        'include_dirs': [
            'leveldb-<(ldbversion)/include/'
          , 'leveldb-<(ldbversion)/port/'
          , 'leveldb-<(ldbversion)/util'
          , 'leveldb-<(ldbversion)/'
        ]
    }
  , 'defines': [
        'SNAPPY=1'
    ]
  , 'include_dirs': [
        'leveldb-<(ldbversion)/'
      , 'leveldb-<(ldbversion)/include/'
    ]
  , 'conditions': [
        ['OS == "win"', {
            'conditions': [
                ['MSVS_VERSION != "2015" and MSVS_VERSION != "2013"', {
                     'include_dirs': [ 'leveldb-<(ldbversion)/port/win' ]
                }]
            ],
            'include_dirs': [
                'port-libuv/'
            ]
          , 'defines': [
                'LEVELDB_PLATFORM_UV=1'
              , 'NOMINMAX=1'
              , '_HAS_EXCEPTIONS=0'
            ]
          , 'sources': [
                'port-libuv/port_uv.cc'
              , 'port-libuv/env_win.cc'
              , 'port-libuv/win_logger.cc'
            ]
          , 'msvs_settings': {
                'VCCLCompilerTool': {
                    'RuntimeTypeInfo': 'false'
                  , 'EnableFunctionLevelLinking': 'true'
                  , 'ExceptionHandling': '2'
                  , 'DisableSpecificWarnings': [ '4355', '4530' ,'4267', '4244' ]
                }
            }
        }, { # OS != "win"
            'sources': [
                'leveldb-<(ldbversion)/port/port_posix.cc'
              , 'leveldb-<(ldbversion)/port/port_posix.h'
              , 'leveldb-<(ldbversion)/util/env_posix.cc'
            ]
          , 'defines': [
                'ROCKSDB_PLATFORM_POSIX=1'
            ]
          , 'cflags': [
                '-std=gnu++0x'
              , '-fno-omit-frame-pointer'
              , '-momit-leaf-frame-pointer'
              , '-Woverloaded-virtual'
              , '-Wno-ignored-qualifiers'
              , '-Wno-type-limits'
              , '-Wno-unused-variable'
              , '-Wno-format-security'
              , '-fPIC'
            ]
<<<<<<< ea5999dbd5fddf8f811b6c14162a3282b24ef7a9
          , 'cflags': [ '-std=c++0x' ]
          , 'cflags!': [ '-fno-tree-vrp' ]
=======
          , 'cflags!': [
                '-fno-exceptions'
              , '-fno-rtti'
            ]
          , 'cflags_cc!': [
                '-fno-exceptions'
              , '-fno-rtti'
            ]
>>>>>>> working rocksdb!
        }]
      , ['OS != "win"' and 'OS != "freebsd"', {
            'cflags': [
                '-Wno-sign-compare'
              , '-Wno-unused-but-set-variable'
            ]
        }]
      , ['OS == "linux"', {
            'defines': [
                'OS_LINUX=1'
            ]
          , 'libraries': [
                '-lpthread'
            ]
          , 'ccflags': [
                '-pthread'
            ]
        }]
      , ['OS == "freebsd"', {
            'defines': [
                'OS_FREEBSD=1'
              , '_REENTRANT=1'
            ]
          , 'libraries': [
                '-lpthread'
            ]
          , 'ccflags': [
                '-pthread'
            ]
          , 'cflags': [
                '-Wno-sign-compare'
            ]
        }]
      , ['OS == "solaris"', {
            'defines': [
                'OS_SOLARIS=1'
              , '_REENTRANT=1'
            ]
          , 'libraries': [
                '-lrt'
              , '-lpthread'
            ]
          , 'ccflags': [
                '-pthread'
            ]
        }]
      , ['OS == "mac"', {
            'defines': [
                'OS_MACOSX=1'
            ]
          , 'xcode_settings': {
                'WARNING_CFLAGS': [
                    '-Wno-sign-compare'
                  , '-Wno-unused-variable'
                  , '-Wno-unused-function'
                  , '-Wno-ignored-qualifiers'
                ]
              , 'OTHER_CPLUSPLUSFLAGS': [
                    '-mmacosx-version-min=10.7'
                  , '-std=c++11'
                  , '-stdlib=libc++'
                ]
              , 'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
            }
        }]
    ]
  , 'sources': [
<<<<<<< ea5999dbd5fddf8f811b6c14162a3282b24ef7a9
        'leveldb-<(ldbversion)/db/builder.cc'
      , 'leveldb-<(ldbversion)/db/builder.h'
      , 'leveldb-<(ldbversion)/db/db_impl.cc'
      , 'leveldb-<(ldbversion)/db/db_impl.h'
      , 'leveldb-<(ldbversion)/db/db_iter.cc'
      , 'leveldb-<(ldbversion)/db/db_iter.h'
      , 'leveldb-<(ldbversion)/db/filename.cc'
      , 'leveldb-<(ldbversion)/db/filename.h'
      , 'leveldb-<(ldbversion)/db/dbformat.cc'
      , 'leveldb-<(ldbversion)/db/dbformat.h'
      , 'leveldb-<(ldbversion)/db/leveldb_main.cc'
      , 'leveldb-<(ldbversion)/db/log_format.h'
=======
        'leveldb-<(ldbversion)/db/version_set_reduce_num_levels.cc'
      , 'leveldb-<(ldbversion)/db/db_filesnapshot.cc'
      , 'leveldb-<(ldbversion)/db/db_impl_readonly.cc'
      , 'leveldb-<(ldbversion)/db/c.cc'
      , 'leveldb-<(ldbversion)/db/merge_helper.cc'
>>>>>>> working rocksdb!
      , 'leveldb-<(ldbversion)/db/log_reader.cc'
      , 'leveldb-<(ldbversion)/db/repair.cc'
      , 'leveldb-<(ldbversion)/db/table_cache.cc'
      , 'leveldb-<(ldbversion)/db/log_writer.cc'
      , 'leveldb-<(ldbversion)/db/dbformat.cc'
      , 'leveldb-<(ldbversion)/db/write_batch.cc'
      , 'leveldb-<(ldbversion)/db/table_stats_collector.cc'
      , 'leveldb-<(ldbversion)/db/memtablelist.cc'
      , 'leveldb-<(ldbversion)/db/db_impl.cc'
      , 'leveldb-<(ldbversion)/db/memtable.cc'
      , 'leveldb-<(ldbversion)/db/db_stats_logger.cc'
      , 'leveldb-<(ldbversion)/db/version_edit.cc'
      , 'leveldb-<(ldbversion)/db/version_set.cc'
      , 'leveldb-<(ldbversion)/db/builder.cc'
      , 'leveldb-<(ldbversion)/db/merge_operator.cc'
      , 'leveldb-<(ldbversion)/db/filename.cc'
      , 'leveldb-<(ldbversion)/db/db_iter.cc'
      , 'leveldb-<(ldbversion)/db/transaction_log_impl.cc'
      , 'leveldb-<(ldbversion)/helpers/memenv/memenv.cc'
<<<<<<< ea5999dbd5fddf8f811b6c14162a3282b24ef7a9
      , 'leveldb-<(ldbversion)/helpers/memenv/memenv.h'
      , 'leveldb-<(ldbversion)/include/leveldb/cache.h'
      , 'leveldb-<(ldbversion)/include/leveldb/comparator.h'
      , 'leveldb-<(ldbversion)/include/leveldb/db.h'
      , 'leveldb-<(ldbversion)/include/leveldb/dumpfile.h'
      , 'leveldb-<(ldbversion)/include/leveldb/env.h'
      , 'leveldb-<(ldbversion)/include/leveldb/filter_policy.h'
      , 'leveldb-<(ldbversion)/include/leveldb/iterator.h'
      , 'leveldb-<(ldbversion)/include/leveldb/options.h'
      , 'leveldb-<(ldbversion)/include/leveldb/slice.h'
      , 'leveldb-<(ldbversion)/include/leveldb/status.h'
      , 'leveldb-<(ldbversion)/include/leveldb/table.h'
      , 'leveldb-<(ldbversion)/include/leveldb/table_builder.h'
      , 'leveldb-<(ldbversion)/include/leveldb/write_batch.h'
      , 'leveldb-<(ldbversion)/port/port.h'
      , 'leveldb-<(ldbversion)/table/block.cc'
      , 'leveldb-<(ldbversion)/table/block.h'
      , 'leveldb-<(ldbversion)/table/block_builder.cc'
      , 'leveldb-<(ldbversion)/table/block_builder.h'
=======
      , 'leveldb-<(ldbversion)/port/stack_trace.cc'
      , 'leveldb-<(ldbversion)/table/merger.cc'
>>>>>>> working rocksdb!
      , 'leveldb-<(ldbversion)/table/filter_block.cc'
      , 'leveldb-<(ldbversion)/table/block_based_table_factory.cc'
      , 'leveldb-<(ldbversion)/table/block_based_table_reader.cc'
      , 'leveldb-<(ldbversion)/table/block_builder.cc'
      , 'leveldb-<(ldbversion)/table/flush_block_policy.cc'
      , 'leveldb-<(ldbversion)/table/iterator.cc'
      , 'leveldb-<(ldbversion)/table/format.cc'
      , 'leveldb-<(ldbversion)/table/block.cc'
      , 'leveldb-<(ldbversion)/table/two_level_iterator.cc'
      , 'leveldb-<(ldbversion)/table/block_based_table_builder.cc'
      , 'leveldb-<(ldbversion)/util/bloom.cc'
      , 'leveldb-<(ldbversion)/util/slice.cc'
      , 'leveldb-<(ldbversion)/util/build_version.cc'
      , 'leveldb-<(ldbversion)/util/vectorrep.cc'
      , 'leveldb-<(ldbversion)/util/env_posix.cc'
      , 'leveldb-<(ldbversion)/util/env.cc'
      , 'leveldb-<(ldbversion)/util/statistics.cc'
      , 'leveldb-<(ldbversion)/util/histogram.cc'
      , 'leveldb-<(ldbversion)/util/arena_impl.cc'
<<<<<<< d72f77a4e566adec983696428cf9ebb4029d180a
<<<<<<< 58e2a4fd0478c0ab31828237278e56cacb659e44
      , 'leveldb-<(ldbversion)/util/ldb_tool.cc'
=======
<<<<<<< HEAD
=======
      , 'leveldb-<(ldbversion)/util/ldb_tool.cc'
>>>>>>> working rocksdb!
>>>>>>> working rocksdb!
=======
      , 'leveldb-<(ldbversion)/util/ldb_tool.cc'
>>>>>>> @0.0.0-a04 remove ldb_tool.cc from build
      , 'leveldb-<(ldbversion)/util/coding.cc'
      , 'leveldb-<(ldbversion)/util/perf_context.cc'
      , 'leveldb-<(ldbversion)/util/hash.cc'
      , 'leveldb-<(ldbversion)/util/logging.cc'
<<<<<<< d72f77a4e566adec983696428cf9ebb4029d180a
<<<<<<< 58e2a4fd0478c0ab31828237278e56cacb659e44
      , 'leveldb-<(ldbversion)/util/ldb_cmd.cc'
=======
<<<<<<< HEAD
=======
      , 'leveldb-<(ldbversion)/util/ldb_cmd.cc'
>>>>>>> working rocksdb!
>>>>>>> working rocksdb!
=======
      , 'leveldb-<(ldbversion)/util/ldb_cmd.cc'
>>>>>>> @0.0.0-a04 remove ldb_tool.cc from build
      , 'leveldb-<(ldbversion)/util/hash_skiplist_rep.cc'
      , 'leveldb-<(ldbversion)/util/auto_roll_logger.cc'
      , 'leveldb-<(ldbversion)/util/blob_store.cc'
      , 'leveldb-<(ldbversion)/util/transformrep.cc'
      , 'leveldb-<(ldbversion)/util/filter_policy.cc'
      , 'leveldb-<(ldbversion)/util/murmurhash.cc'
      , 'leveldb-<(ldbversion)/util/cache.cc'
      , 'leveldb-<(ldbversion)/util/comparator.cc'
      , 'leveldb-<(ldbversion)/util/env_hdfs.cc'
      , 'leveldb-<(ldbversion)/util/skiplistrep.cc'
      , 'leveldb-<(ldbversion)/util/status.cc'
      , 'leveldb-<(ldbversion)/util/options.cc'
      , 'leveldb-<(ldbversion)/util/crc32c.cc'
      , 'leveldb-<(ldbversion)/util/string_util.cc'
    ]
}]}
