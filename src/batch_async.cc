/* Copyright (c) 2012-2016 LevelDOWN contributors
 * See list at <https://github.com/level/leveldown#contributing>
 * MIT License <https://github.com/level/leveldown/blob/master/LICENSE.md>
 */


#include <rocksdb/write_batch.h>
#include "batch.h"
#include "batch_async.h"

namespace flat_rocks {

/** NEXT WORKER **/

BatchWriteWorker::BatchWriteWorker (
    Batch* batch
  , Nan::Callback *callback
) : AsyncWorker(NULL, callback)
  , batch(batch)
{};

BatchWriteWorker::~BatchWriteWorker () {}

void BatchWriteWorker::Execute () {
  SetStatus(batch->Write());
}

} // namespace flat_rocks
