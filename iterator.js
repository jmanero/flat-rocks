const Util = require('util');
const AbstractIterator = require('abstract-leveldown').AbstractIterator;
const fastFuture = require('fast-future');

function Iterator(db, options) {
  AbstractIterator.call(this, db);

  this.binding = db.binding.iterator(options);
  this.cache = null;
  this.finished = false;
  this.fastFuture = fastFuture();
}
Util.inherits(Iterator, AbstractIterator);

Iterator.prototype.seek = function(key) {
  if (typeof key !== 'string')
    throw new Error('seek requires a string key');
  this.cache = null;
  this.binding.seek(key);
};

Iterator.prototype._next = function(callback) {
  var that = this;
  var key, value;

  if (this.cache && this.cache.length) {
    key = this.cache.pop();
    value = this.cache.pop();

    this.fastFuture(function() {
      callback(null, key, value);
    });

  } else if (this.finished) {
    this.fastFuture(function() {
      callback();
    });
  } else {
    this.binding.next(function(err, array, finished) {
      if (err) return callback(err);

      that.cache = array;
      that.finished = finished;
      that._next(callback);
    });
  }

  return this;
};

Iterator.prototype._end = function(callback) {
  delete this.cache;
  this.binding.end(callback);
};

module.exports = Iterator;
