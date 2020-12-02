var disJointSetsfile = require('./disjointsets.js');
const assert = require('assert').strict;

  describe("test constructor", function() {
    it("test constructor function", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { new disJointSetsfile.disJointSets(); }, Error ); // you must specify size in the constructor
    });
  });

  describe("test constructor with string size", function() {
    it("test constructor with string size", function() {
      assert.throws( function() { new disJointSetsfile.disJointSets('7'); }, Error ); // size cannot be string
    });
  });

  
  describe("test makeSet", function() {
    it("test makeset function", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { mydisJointSets.makeSet(); }, Error ); // errror is you make set without specifying an element
      mydisJointSets.makeSet(1);
      assert.strictEqual(mydisJointSets.find(1), 1); // after you makeset, the element is its own parent.
    });
  });

  describe("test makeSet with non integer element", function() {
    it("test makeSet with non integer element function", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { mydisJointSets.makeSet({}); }, Error ); // errror is you make set non integer 
      assert.throws( function() { mydisJointSets.makeSet([]); }, Error ); //errror is you make set non integer 
      assert.throws( function() { mydisJointSets.makeSet('123'); }, Error ); // errror is you make set non integer 
    });
  });


  describe("test find", function() {
    it("test find function", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { mydisJointSets.find(); }, Error ); // error if you don't specify an element to find
      mydisJointSets.makeSet(1);
      mydisJointSets.makeSet(2);
      mydisJointSets.union(1,2);
      assert.strictEqual(mydisJointSets.find(1), mydisJointSets.find(2)); // once a union is performed, find should reutnr the id of the same parent
    });
  });

  describe("test find non existent element", function() {
    it("test find function with non existent element", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { mydisJointSets.find(1); }, Error ); // find a non existent element
    });
  });

  
  describe("test find non integer element", function() {
    it("test find function non integer element ", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { mydisJointSets.find('1'); }, Error ); // find a non integer element
      assert.throws( function() { mydisJointSets.find({}); }, Error ); // find a non integer element
      assert.throws( function() { mydisJointSets.find([]); }, Error ); // find a non integer element
    });
  });

  describe("test union with missing arguments", function() {
    it("test union with missing arguments", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { mydisJointSets.union(); }, Error ); // error if union is missing both arguments
      assert.throws( function() { mydisJointSets.union(1); }, Error ); // error if union is missing one argument
      });
  });


  describe("test union of same element", function() {
    it("test union of same element", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { mydisJointSets.union(1,1); }, Error ); // cannot perform union of eleemnt on itself
      });
  });
  
  describe("test union of non existent element", function() {
    it("test union of non existent element", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { mydisJointSets.union(1,2); }, Error ); // cannot perform union of non-existent element
      });
  });

  describe("test union of element greater than size of array", function() {
    it("test union of element greater than size of array", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { mydisJointSets.union(9,12); }, Error ); // cannot perform union of elements greater than size
      });
  });
  
  describe("test union of non integer elements", function() {
    it("test union of non integer elements", function() {
      var mydisJointSets = new disJointSetsfile.disJointSets(7);
      assert.throws( function() { mydisJointSets.union("9","12"); }, Error ); // cannot perform union of elements greater than size
      assert.throws( function() { mydisJointSets.union(9,"12"); }, Error ); // cannot perform union of elements greater than size
      assert.throws( function() { mydisJointSets.union("9",12); }, Error ); // cannot perform union of elements greater than size
      assert.throws( function() { mydisJointSets.union([],12); }, Error ); // cannot perform union of elements greater than size
      });
  });