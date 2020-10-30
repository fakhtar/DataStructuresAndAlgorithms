var binaryHeap = class binaryHeap {
    constructor(myArray) {
        this.arrayRep = myArray;
        this.size = myArray.length;
    }
    getHeapMax() {
        if (this.size == 0) {
            throw new Error('Cannot get max of empty heap.');
        }
        else {
            return this.arrayRep[0]
        }
    }
    insertNode(priority) {
        if (!Number.isInteger(priority)) {
            throw new Error('val must be integer');            
        }
        this.arrayRep.push(priority);
        this.size += 1;
        this.siftUp(this.size-1);
        return this.arrayRep;
    }
    extractMax() {
        var max = this.getHeapMax();
        var tmp = this.arrayRep[this.size -1];
        this.arrayRep[this.size -1] = max;
        this.arrayRep[0] = tmp;
        this.arrayRep.pop();
        this.size -= 1;
        if (this.size > 0){
            this.siftDown(0)
        }
        return this.arrayRep;
        // return max  
    }
    changePriority(indexOfNode, newPriority) {
        if (!Number.isInteger(indexOfNode) || !Number.isInteger(newPriority)) {
            throw new Error('not a number exception');            
        }
        if (indexOfNode > this.size -1) {
            throw new Error('index out of range');
        }
        if (this.arrayRep[indexOfNode] == newPriority) {
            return this.arrayRep
        }
        if (this.size == 1 && indexOfNode == 0) {
            this.arrayRep[indexOfNode] = newPriority;
            return this.arrayRep;
        }
        if (this.arrayRep[this.getParent(indexOfNode)] < newPriority) {
            this.arrayRep[indexOfNode] = newPriority;
            this.siftUp(indexOfNode);
        }
        else{
            this.siftDown(indexOfNode);
        }
        return this.arrayRep;
    }
    removeElement(indexOfNode) {
        if (!Number.isInteger(indexOfNode)) {
            throw new Error('index must be integer');            
        }
        if (indexOfNode > (this.size -1)) {
            throw new Error('index out of range');
        }
        var tmp = this.getHeapMax();
        this.arrayRep[indexOfNode] = tmp + 1;
        this.siftUp(indexOfNode);
        this.extractMax();
        return this.arrayRep;
    }
    siftUp(indexOfNode) {
        if (!Number.isInteger(indexOfNode)) {
            throw new Error('index must be integer');            
        }
        if (indexOfNode > (this.size -1)) {
            throw new Error('index out of range');
        }
        while (indexOfNode > 0 &&  this.arrayRep[this.getParent(indexOfNode)] < this.arrayRep[indexOfNode] )
        {
            var tmp = this.arrayRep[indexOfNode];
            this.arrayRep[indexOfNode] = this.arrayRep[this.getParent(indexOfNode)];
            this.arrayRep[this.getParent(indexOfNode)] = tmp;
            indexOfNode = this.getParent(indexOfNode);        
        }
        return this.arrayRep;
    }
    siftDown(indexOfNode) {
        if (!Number.isInteger(indexOfNode)) {
            throw new Error('index must be integer');            
        }
        if (indexOfNode > (this.size -1)) {
            throw new Error('index out of range');
        }
        while (this.getLeftChild(indexOfNode) <= (this.size - 1) || this.getRightChild(indexOfNode) <= (this.size - 1)) {
            var tmp;
            // this is where the problem is
            // if (this.arrayRep[this.getLeftChild(indexOfNode)] > this.arrayRep[indexOfNode] ) {
            if (this.arrayRep[this.getLeftChild(indexOfNode)] > this.arrayRep[indexOfNode] && this.arrayRep[this.getRightChild(indexOfNode)] > this.arrayRep[indexOfNode] && this.arrayRep[this.getLeftChild(indexOfNode)] > this.arrayRep[this.getRightChild(indexOfNode)] ) {
                tmp = this.arrayRep[this.getLeftChild(indexOfNode)];
                this.arrayRep[this.getLeftChild(indexOfNode)] = this.arrayRep[indexOfNode];
                this.arrayRep[indexOfNode] = tmp;
                indexOfNode = this.getLeftChild(indexOfNode);
            }
            else{
                if (this.arrayRep[this.getRightChild(indexOfNode)] > this.arrayRep[indexOfNode]) {
                    tmp = this.arrayRep[this.getRightChild(indexOfNode)];
                    this.arrayRep[this.getRightChild(indexOfNode)] = this.arrayRep[indexOfNode];
                    this.arrayRep[indexOfNode] = tmp;
                    indexOfNode = this.getRightChild(indexOfNode);
                }
                else {
                    if (this.arrayRep[this.getLeftChild(indexOfNode)] > this.arrayRep[indexOfNode] ) {
                        tmp = this.arrayRep[this.getLeftChild(indexOfNode)];
                        this.arrayRep[this.getLeftChild(indexOfNode)] = this.arrayRep[indexOfNode];
                        this.arrayRep[indexOfNode] = tmp;
                        indexOfNode = this.getLeftChild(indexOfNode);
                    }
                    else {
                        break;
                    }
                }
            }
            if (this.getRightChild(indexOfNode) > this.size - 1 && this.getLeftChild(indexOfNode) > this.size - 1) {
                break;
            }      
        }
        return this.arrayRep;
    }
    getLeftChild(indexOfNode) {
        return (2*indexOfNode) + 1;
    }
    getRightChild(indexOfNode) {
        return (2*indexOfNode) + 2;
    }
    getParent(indexOfNode) {
        if (Number.isInteger(indexOfNode)) {
            if (indexOfNode == 0) {
                throw new Error('0 does not have parent.');
            }
            else {
                if (indexOfNode < 0) {
                    throw new Error('Cannot get parent of negative index.');
                }
            }
        }
        else {
            throw new Error('Argument must be an integer.');
        }
        if (indexOfNode % 2 == 0) {
            return (indexOfNode - 2) /2
        } else {
            return (indexOfNode - 1) /2
        }
        // If, negative, throw error. If not integer, throw error. if zero, throw error, if odd, subtract 1 and then divide by 2. If even, subtract 2 and then divide by 2
    }
}

var myHeap = new binaryHeap([3,2,1]);
myHeap.extractMax()

module.exports.binaryHeap = binaryHeap;