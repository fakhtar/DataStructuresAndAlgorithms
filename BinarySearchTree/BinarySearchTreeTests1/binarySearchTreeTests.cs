using Microsoft.VisualStudio.TestTools.UnitTesting;
using BinarySearchTree;
using System;
using System.Collections.Generic;
using System.Text;

namespace BinarySearchTree.Tests
{
    [TestClass()]
    public class binarySearchTreeTests
    {
        [TestMethod()]
        public void getHeightTest_EmptyTree_ReturnZero()
        {
            //arrange
            var myBST = new binarySearchTree<String>();
            //act
            //assert
            Assert.AreEqual(0, myBST.getHeight());
        }
        [TestMethod()]
        public void getHeightTest_TwoNode_ReturnTwo()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            myBST.addNode(1);
            myBST.addNode(2);
            //assert
            Assert.AreEqual(2, myBST.getHeight());
        }
        [TestMethod()]
        [ExpectedException(typeof(ArgumentException))]
        public void addNodeTest_duplicateNode_throwError()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            myBST.addNode(1);
            myBST.addNode(1);
            //assert
        }

        [TestMethod()]
        public void addNodeTest_singleNode_returnNode()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            int myTestInt = myBST.addNode(1).val;
            //assert
            Assert.AreEqual(1, myTestInt);
        }

        [TestMethod()]
        public void deleteNodeTest_SingleInt_Returnint()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            myBST.addNode(1);
            myBST.addNode(2);
            myBST.addNode(3);
            myBST.addNode(4);
            int testDeleteNoteVal = myBST.deleteNode(4);
            //assert
            Assert.AreEqual(4, testDeleteNoteVal);
        }
        // delete from empty tree
        [TestMethod()]
        [ExpectedException(typeof(ArgumentException),"Cannot delete non-existent node.")]
        public void deleteNodeTest_emptyTree_throwError()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            myBST.deleteNode(1);
            //assert
        }
        // delete node that does not exist in tree
        [TestMethod()]
        [ExpectedException(typeof(ArgumentException), "Cannot delete non-existent node.")]
        public void deleteNodeTest_NodeThatDoesNotExist_throwError()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            myBST.addNode(2);
            myBST.deleteNode(1);
            //assert
        }
        [TestMethod()]
        public void nodeExistsTest_AddNode_ReturnTrue()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            myBST.addNode(1);
            myBST.addNode(3);
            myBST.addNode(2);
            myBST.addNode(4);
            //assert
            Assert.AreEqual(true, myBST.nodeExists(1));
        }
        [TestMethod()]
        public void nodeExistsTest_Empty_ReturnFalse()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            //assert
            Assert.AreEqual(false, myBST.nodeExists(1));
        }
        [TestMethod()]
        public void breadthFirstSearch_Test_ReturnBreadthFirstStructure()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            myBST.addNode(4);
            myBST.addNode(2);
            myBST.addNode(6);
            myBST.addNode(1);
            myBST.addNode(3);
            myBST.addNode(5);
            myBST.addNode(7);
            int[] myArray = new int[] { 4, 2, 6, 1, 3, 5, 7 };
            //assert
            Assert.AreEqual(myArray, myBST.breadthFirstSearch());
        }
        [TestMethod()]
        public void inorder_Test_Returninorder()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            myBST.addNode(4);
            myBST.addNode(2);
            myBST.addNode(6);
            myBST.addNode(1);
            myBST.addNode(3);
            myBST.addNode(5);
            myBST.addNode(7);
            int[] myArray = new int[] { 4, 2, 1, 3, 6, 5, 7 };
            //assert
            Assert.AreEqual(myArray, myBST.inOrderTraversal());
        }
        [TestMethod()]
        public void preOrder_Test_Returninorder()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            myBST.addNode(4);
            myBST.addNode(2);
            myBST.addNode(6);
            myBST.addNode(1);
            myBST.addNode(3);
            myBST.addNode(5);
            myBST.addNode(7);
            int[] myArray = new int[] { 4, 2, 1, 3, 6, 5, 7 };
            //assert
            Assert.AreEqual(myArray, myBST.preOrderTraversal());
        }
        [TestMethod()]
        public void postOrder_Test_Returninorder()
        {
            //arrange
            var myBST = new binarySearchTree<int>();
            //act
            myBST.addNode(4);
            myBST.addNode(2);
            myBST.addNode(6);
            myBST.addNode(1);
            myBST.addNode(3);
            myBST.addNode(5);
            myBST.addNode(7);
            int[] myArray = new int[] { 4, 2, 1, 3, 6, 5, 7 };
            //assert
            Assert.AreEqual(myArray, myBST.postOrderTraversal());
        }
    }
}