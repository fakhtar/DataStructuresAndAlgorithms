

var disJointSets = class disJointSets {
    constructor(size) {
        if (typeof size === 'undefined') {
            throw new Error('You must pass size to constructor!');
        }
        if (!Number.isInteger(size)) {
            throw new Error('size must be integer');
        }
        this.parent = new Array(size).fill(null);
        this.rank = new Array(size).fill(null);
    }
    makeSet(x){
        if (typeof x === 'undefined') {
            throw new Error('to make a singleton set, you must speciy the element.');
        }
        if (!Number.isInteger(x)) {
            throw new Error('argument must be integer');
        }
        // set the parent element to itself and set the rank element 1
        this.parent[x] = x;
        this.rank[x] = 0;
    }
    find(x){
        if (typeof x === 'undefined') {
            throw new Error('to find an element, you must speciy the element.');
        }
        if (!Number.isInteger(x)) {
            throw new Error('argument must be integer');
        }
        if (x != this.parent[x]){
            this.parent[x] = this.find(this.parent[x]);
        }
        return this.parent[x]
    }
    union (x,y){
        if (typeof x === 'undefined' || typeof y === 'undefined' ) {
            throw new Error('to perform union, please specify both elementss');
        }
        if (x == y) {
            throw new Error('cannot perform a union on the same element');
        }
        if (!Number.isInteger(x) || !Number.isInteger(y)) {
            throw new Error('argument must be integer');
        }
        var x_id = this.find(x);
        var y_id = this.find(y);
        if (x_id == y_id) {
            return;
        }
        if (this.rank[x_id] > this.rank[y_id]){
            this.parent[y_id] = x_id;
        }
        else {
            this.parent[x_id] = y_id;
            if (this.rank[x_id] == this.rank[y_id]){
                this.rank[y_id] = this.rank[y_id] + 1;
            }
        }

    }
}



var mydisJointSets = new disJointSets(7);
mydisJointSets.makeSet(1)
mydisJointSets.makeSet(2)
mydisJointSets.makeSet(3)
mydisJointSets.makeSet(4)
console.log(mydisJointSets.find(4))
mydisJointSets.union(4,1)
console.log(mydisJointSets.find(4))
console.log(mydisJointSets.find(1))
console.log(mydisJointSets.find(4) == mydisJointSets.find(1))

module.exports.disJointSets = disJointSets;