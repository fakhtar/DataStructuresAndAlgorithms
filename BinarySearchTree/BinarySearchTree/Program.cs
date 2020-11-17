using System;

namespace BinarySearchTree
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            binarySearchTree<int> mytree = new binarySearchTree<int>();
            var myNewBST = new binarySearchTree<int>();
            myNewBST.addNode(1);
            myNewBST.addNode(3);
            myNewBST.addNode(2);
            myNewBST.addNode(4);
            int deletedNodeVal = myNewBST.deleteNode(4);
            //mytree.addNode(1);
        }
    }
}
