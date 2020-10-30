var binaryHeapfile = require('./binaryHeap.js');
const assert = require('assert').strict;

  describe("test get parent function", function() {
    it("should get parent or thow error if asked for wrong parent", function() {
      var myHeap = new binaryHeapfile.binaryHeap([]);
      assert.throws( function() { myHeap.getParent(0); }, Error ); // cannot ask for 0s parent
      assert.throws( function() { myHeap.getParent(-1); }, Error ); // cannot as for a negative index parent
      assert.throws( function() { myHeap.getParent("A"); }, Error ); // index must an integer
      assert.strictEqual(myHeap.getParent(1), 0);
      assert.strictEqual(myHeap.getParent(2), 0);
      assert.strictEqual(myHeap.getParent(6), 2);
      assert.strictEqual(myHeap.getParent(5), 2);
    });
  });

  describe("test get right child function", function() {
    it("should get right child and thow error if asked for wrong child asked for", function() {
      var myHeap = new binaryHeapfile.binaryHeap([1,2,3,4,5,6,7,8,9]);
      assert.strictEqual(myHeap.getRightChild(0), 2);
      assert.strictEqual(myHeap.getRightChild(1), 4);
      assert.strictEqual(myHeap.getRightChild(2), 6);
    });
  });

  describe("test get left child function", function() {
    it("should get left child and thow error if asked for wrong child asked for", function() {
      var myHeap = new binaryHeapfile.binaryHeap([1,2,3,4,5,6,7,8,9]);
      assert.strictEqual(myHeap.getLeftChild(0), 1);
      assert.strictEqual(myHeap.getLeftChild(1), 3);
      assert.strictEqual(myHeap.getLeftChild(2), 5);
    });
  });

  describe("test get sift down function", function() {
    it("should sift down until invariant satisfied", function() {
      var myHeap = new binaryHeapfile.binaryHeap([1,3,2]);
      assert.deepStrictEqual(myHeap.siftDown(0), [3,1,2]);
      assert.throws( function() { myHeap.siftDown(3); }, Error ); // cannot sift down an index higher than heap size
      var myZeroHeap = new binaryHeapfile.binaryHeap([0]);
      assert.deepStrictEqual(myZeroHeap.siftDown(0), [0]);
      var myBlankHeap = new binaryHeapfile.binaryHeap([]);
      assert.throws( function() { myBlankHeap.siftDown(0); }, Error ); // cannot sift down an empty heap
      var myValidHeap = new binaryHeapfile.binaryHeap([29,14,7]); // should not change the order because already good
      assert.deepStrictEqual(myValidHeap.siftDown(0), [29,14,7]);
      var myInvalidHeap = new binaryHeapfile.binaryHeap([1,9,8,7,6,5,4]);
      assert.deepStrictEqual(myInvalidHeap.siftDown(0), [9,7,8,1,6,5,4]);
      assert.throws( function() { myHeap.siftDown("A"); }, Error ); // index must be an integer
    });
  });

  describe("test get sift up function", function() {
    it("should sift up until invariant satisfied", function() {
      var myHeap = new binaryHeapfile.binaryHeap([1,3,2]);
      assert.deepStrictEqual(myHeap.siftUp(1), [3,1,2]);
      assert.throws( function() { myHeap.siftUp(3); }, Error ); // cannot sift up an index higher than heap size
      var myZeroHeap = new binaryHeapfile.binaryHeap([0]);
      assert.deepStrictEqual(myZeroHeap.siftUp(0), [0]);
      var myBlankHeap = new binaryHeapfile.binaryHeap([]);
      assert.throws( function() { myBlankHeap.siftUp(0); }, Error ); // cannot sift down an empty heap
      var myValidHeap = new binaryHeapfile.binaryHeap([29,14,7]); // should not change the order because already good
      assert.deepStrictEqual(myValidHeap.siftUp(0), [29,14,7]);
      var myInvalidHeap = new binaryHeapfile.binaryHeap([9,8,7,6,5,4,10]);
      assert.deepStrictEqual(myInvalidHeap.siftUp(6), [10,8,9,6,5,4,7]);
      assert.throws( function() { myHeap.siftUp("A"); }, Error ); // index must be an integer
    });
  });

  describe("test remove element function", function() {
    it("should remove with invariant satisfied", function() {
      var myHeap = new binaryHeapfile.binaryHeap([3,2,1]);
      assert.deepStrictEqual(myHeap.removeElement(1), [3,1]);
      assert.throws( function() { myHeap.removeElement(3); }, Error ); // cannot remove element larger than size of heap
      var myZeroHeap = new binaryHeapfile.binaryHeap([0]);
      assert.deepStrictEqual(myZeroHeap.removeElement(0), []);
      var myBlankHeap = new binaryHeapfile.binaryHeap([]);
      assert.throws( function() { myBlankHeap.removeElement(0); }, Error ); // cannot remove element form an empty heap
      var myInvalidHeap = new binaryHeapfile.binaryHeap([10,9,8,7,6,5,4]);
      assert.deepStrictEqual(myInvalidHeap.removeElement(4), [10,9,8,7,4,5]);
      assert.throws( function() { myHeap.removeElement("A"); }, Error ); // index must be an integer
    });
  });

  describe("test change priority function", function() {
    it("change priority with invariant satisfied", function() {
      var myHeap = new binaryHeapfile.binaryHeap([3,2,1]);
      assert.deepStrictEqual(myHeap.changePriority(1,7), [7,3,1]);
      assert.throws( function() { myHeap.changePriority(3); }, Error ); // cannot change priority larger than size of heap
      var myZeroHeap = new binaryHeapfile.binaryHeap([0]);
      assert.deepStrictEqual(myZeroHeap.changePriority(0,100), [100]);
      var myBlankHeap = new binaryHeapfile.binaryHeap([]);
      assert.throws( function() { myBlankHeap.changePriority(0,8); }, Error ); // cannot change priotiy an empty heap
      var myInvalidHeap = new binaryHeapfile.binaryHeap([10,9,8,7,6,5,4]);
      assert.deepStrictEqual(myInvalidHeap.changePriority(4,21), [21,10,8,7,9,5,4]);
      assert.throws( function() { myHeap.changePriority("A","A"); }, Error ); // index must be an integer
    });
  });
  
  describe("test extract max function", function() {
    it("extract max with invariant satisfied", function() {
      var myHeap = new binaryHeapfile.binaryHeap([3,2,1]);
      assert.deepStrictEqual(myHeap.extractMax(), [2,1]);
      var myZeroHeap = new binaryHeapfile.binaryHeap([0]);
      assert.deepStrictEqual(myZeroHeap.extractMax(), []);
      var myBlankHeap = new binaryHeapfile.binaryHeap([]);
      assert.throws( function() { myBlankHeap.extractMax(); }, Error ); // cannot Extract empty heap
      var myInvalidHeap = new binaryHeapfile.binaryHeap([10,9,8,7,6,5,4]);
      assert.deepStrictEqual(myInvalidHeap.extractMax(4,21), [9,7,8,4,6,5]);
    });
  });

  describe("test insert node function", function() {
    it("insert node with invariant satisfied", function() {
      var myHeap = new binaryHeapfile.binaryHeap([3,2,1]);
      assert.deepStrictEqual(myHeap.insertNode(7), [7,3,1,2]);
      var myZeroHeap = new binaryHeapfile.binaryHeap([0]);
      assert.deepStrictEqual(myZeroHeap.insertNode(10), [10,0]);
      var myInvalidHeap = new binaryHeapfile.binaryHeap([10,9,8,7,6,5,4]);
      assert.deepStrictEqual(myInvalidHeap.insertNode(21), [21,10,8,9,6,5,4,7]);
      assert.throws( function() { myInvalidHeap.insertNode("A"); }, Error ); // cannot insert letter
    });
  });

  describe("test get heap max function", function() {
    it(" no modifiedation are made to the structure ", function() {
      var myHeap = new binaryHeapfile.binaryHeap([3,2,1]);
      assert.strictEqual(myHeap.getHeapMax(), 3);
      var myZeroHeap = new binaryHeapfile.binaryHeap([0]);
      assert.strictEqual(myZeroHeap.getHeapMax(10), 0);
      var myInvalidHeap = new binaryHeapfile.binaryHeap([]);
      assert.throws( function() { myInvalidHeap.getHeapMax(); }, Error ); // cannot get max of empty heap
    });
  });