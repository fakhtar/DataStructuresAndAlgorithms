using System;
using System.Collections.Generic;
using System.Text;

namespace BinarySearchTree
{
    public class _Node
    {
        public int val  // property
        { get; set; }
        public _Node leftChild  // property
        { get; set; }
        public _Node rightChild  // property
        { get; set; }
    }
    public class binarySearchTree<T>
    {
        public _Node root;
        public binarySearchTree()
        {
            this.root = null;
        }

        public _Node addNode(int nodeVal)
        {
            // write helper function that recursivelys adds node. Continue from here.
            if (this.root == null)
            {
                _Node newNode = new _Node();
                newNode.val = nodeVal;
                this.root = newNode;
                return newNode;
            }
            else
            {
                _Node newNode = _addNodeHelper(this.root, nodeVal);
                return newNode;
            }
        }
        public int getHeight()
        {
            return _getHeightHelper(this.root);
        }

        private int _getHeightHelper(_Node node)
        {
            if (node == null)
            {
                return 0;
            }
            else
            {
                return 1 + Math.Max(this._getHeightHelper(node.leftChild), this._getHeightHelper(node.rightChild));
            }
        }

        private _Node _addNodeHelper(_Node myNode, int nodeVal)
        {
            if (myNode.val == nodeVal)
            {
                System.ArgumentException argEx = new System.ArgumentException("Cannot add duplicate item.");
                throw argEx;
                //throw new System.ArgumentException("Cannot add duplicate item.");
            }
            else
            {
                // if nodeVal is less than myNode.val and if left child is null
                // If it is null then attach to left child. Otherwise recursively call function with left child
                if (nodeVal < myNode.val && myNode.leftChild == null)
                {
                    _Node newNode = new _Node();
                    newNode.val = nodeVal;
                    myNode.leftChild = newNode;
                    return newNode;
                }
                else
                {
                    if (nodeVal < myNode.val && myNode.leftChild != null)
                    {
                        _addNodeHelper(myNode.leftChild, nodeVal);
                    }
                }

                if (nodeVal > myNode.val && myNode.rightChild == null)
                {
                    _Node newNode = new _Node();
                    newNode.val = nodeVal;
                    myNode.rightChild = newNode;
                    return newNode;
                }
                else
                {
                    if (nodeVal > myNode.val && myNode.rightChild != null)
                    {
                        _addNodeHelper(myNode.rightChild, nodeVal);
                    }
                }
            }
            return myNode;
        }
        public int deleteNode(int nodeVal)
        {
            //first find the node. If the node does not exist, then throw an error.
            //if the node has no children, then simply delete the node.
            // if the node has 1 child then set parent value to the deleted node value and delete the node.
            // if both right and left children are not null then find the min of the right subtree of the node, set the node value to the min of the right subtree and delete the min node
            var deletedNodeCall = _findNodeHelper(this.root,null,nodeVal);
            _Node deletedNode = deletedNodeCall.Item1;
            _Node parentNode = deletedNodeCall.Item2;
            if (deletedNode.rightChild == null & deletedNode.leftChild == null)
            {
                if (parentNode.rightChild.val == nodeVal)
                {
                    parentNode.rightChild = null;
                }
                else
                {
                    parentNode.leftChild = null;
                }
            }
            else if ((deletedNode.rightChild == null & deletedNode.leftChild != null)) {
                deletedNode.val = deletedNode.leftChild.val;
                deletedNode.leftChild = null;
            }
            else if ((deletedNode.rightChild != null & deletedNode.leftChild == null))
            {
                deletedNode.val = deletedNode.rightChild.val;
                deletedNode.rightChild = null;
            }
            else if ((deletedNode.rightChild != null & deletedNode.leftChild != null))
            {
                // find the min of the right subtree.
                _Node minNode = _findMinNodeHelper(deletedNode.rightChild);
                deletedNode.val = minNode.val;
                var deletedNodeCallMin = _findNodeHelper(deletedNode, parentNode, nodeVal);
                _Node deletedNodeMin = deletedNodeCallMin.Item1;
                _Node parentNodeMin = deletedNodeCallMin.Item2;
                if (deletedNodeMin.rightChild == null)
                {
                    parentNodeMin.leftChild = null;
                }
                else {
                    parentNodeMin.leftChild = deletedNodeMin.rightChild;
                }
            }
            return deletedNode.val;
        }
        private _Node _findMinNodeHelper(_Node node) {
            if (node.leftChild == null)
            {
                return node;
            }
            else {
                return _findMinNodeHelper(node.leftChild);
            }
        }
        private (_Node,_Node) _findNodeHelper(_Node node,_Node parent, int nodeVal)
        {
            if (node == null)
            {
                System.ArgumentException argEx = new System.ArgumentException("Cannot delete non - existent node.");
                throw argEx;
            }
            if (node.val == nodeVal)
            {
                return (node, parent);
            }
            else {
                if (node.val < nodeVal) {
                    return _findNodeHelper(node.rightChild,node, nodeVal);
                }
                else {
                    return _findNodeHelper(node.leftChild,node, nodeVal);
                }
            }
        }
        public bool nodeExists(int nodeVal)
        {
            return false;
        }
        public T[] breadthFirstSearch()
        {
            T[] myArray = new T[] { };
            return myArray;
        }
        public T[] inOrderTraversal()
        {
            T[] myArray = new T[] { };
            return myArray;
        }
        public T[] preOrderTraversal()
        {
            T[] myArray = new T[] { };
            return myArray;
        }
        public T[] postOrderTraversal()
        {
            T[] myArray = new T[] { };
            return myArray;
        }
    }
}
