
# Tree questions

## Given the root of a binary tree, flatten the tree into a "linked list."

## Given the root of a binary tree, invert the tree, and return its root.
## Given the root of a binary tree, return its maximum depth.
## Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
## Given the root of a binary tree, return the pre-order traversal of its nodes' values.
## Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

## Binary tree in-order traversal
```
public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
}
```

Time complexity: O(n)

Space complexity: O(n)

## Symmetric tree

Given a binary tree, check whether it is a mirror of itself.


Iterative Approach:

Algorithm for checking whether a binary tree is a mirror of itself using an iterative approach and a stack:

Create a stack and push the root node onto it twice.
While the stack is not empty, repeat the following steps:
    a. Pop two nodes from the stack, say node1 and node2.
    b. If both node1 and node2 are null, continue to the next iteration.
    c. If one of the nodes is null and the other is not, return false as it is not a mirror.
    d. If both nodes are not null, compare their values. If they are not equal, return false.
    e. Push the left child of node1 and the right child of node2 onto the stack.
    f. Push the right child of node1 and the left child of node2 onto the stack.
If the loop completes successfully without returning false, return true as it is a mirror.

```
// Java program to check if a given Binary Tree is symmetric
// or not
import java.util.*;

// A Binary Tree Node
class Node {
  int key;
  Node left, right;
  // Constructor
  Node(int item)
  {
    key = item;
    left = right = null;
  }
}

public class GFG 
{
  
  // Returns true if a tree is symmetric i.e. mirror image
  // of itself
  static boolean isSymmetric(Node root)
  {
    
    // If the root is null, then the binary tree is
    // symmetric.
    if (root == null) {
      return true;
    }
    
    // Create a stack to store the left and right
    // subtrees
    // of the root.
    Stack<Node> stack = new Stack<>();
    stack.push(root.left);
    stack.push(root.right);

    // Continue the loop until the stack is empty.
    while (!stack.empty()) {
      // Pop the left and right subtrees from the
      // stack.
      Node node1 = stack.pop();
      Node node2 = stack.pop();

      // If both nodes are null, continue the loop.
      if (node1 == null && node2 == null) {
        continue;
      }

      // If one of the nodes is null, the binary tree
      // is not symmetric.
      if (node1 == null || node2 == null) {
        return false;
      }

      // If the values of the nodes are not equal, the
      // binary tree is not symmetric.
      if (node1.key != node2.key) {
        return false;
      }

      // Push the left and right subtrees of the left
      // and right nodes onto the stack in the
      // opposite order.
      stack.push(node1.left);
      stack.push(node2.right);
      stack.push(node1.right);
      stack.push(node2.left);
    }

    // If the loop completes, the binary tree is
    // symmetric.
    return true;
  }

  // Driver code
  public static void main(String[] args)
  {
    // Let us construct the Tree shown in the above
    // figure
    Node root = new Node(1);
    root.left = new Node(2);
    root.right = new Node(2);
    root.left.left = new Node(3);
    root.left.right = new Node(4);
    root.right.left = new Node(4);
    root.right.right = new Node(3);

    if (isSymmetric(root))
      System.out.println("Symmetric");
    else
      System.out.println("Not symmetric");
  }
}
```

## Maximum depth of binary tree

Given the root of a binary tree, return its max depth where max depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

```
var maxDepth = function(root) {
    if(!root) return 0
    return 1 + Math.max(depth(root.left), depth(root.right))
  }
```

## Convert sorted array to binary search tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST

The mid value of the given sorted array would represent the root of one possible BST.

```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        
       return helper(nums, 0, nums.length - 1);
    }
    
    private TreeNode helper(int[] nums, int low, int high) {
        if(low > high) {
            return null;
        }
        
        int mid = low + (high - low)/2;
        //center val of sorted array as the root of the bst
        TreeNode head = new TreeNode(nums[mid]);
        
        //left of the mid value should go to the left of this root node to satisfy bst
        head.left = helper(nums, low, mid - 1);
        //right of the mid value should go to the right of this root node to satisfy bst
        head.right = helper(nums, mid + 1, high);
        return head;
        
    }
    
    //T O(log n) S O(n) recursion stack space
}
```

Complexity Analysis:

Since we perform binary search on the array elements, splitting the input size by half through each recursion, therefore the time complexity that would be incurred from the aforementioned algorithm would be same as that incurred in binary search, that of T O(log n).

Space complexity due to recursion stack space would incur in the worst case of S O(n).

## Invert binary tree

An inverted form of a Binary Tree is another Binary Tree with left and right children of all non-leaf nodes interchanged.

```
// Iterative Function to invert given binary Tree using stack
void invertBinaryTree(TreeNode root) 
{
    // base case: if tree is empty
    if (root is null) 
        return
    // create an empty stack and push root node
    stack S
    S.push(root)
    // iterate until the stack is not empty
    while (S is not empty)
    {
        // pop top node from stack
        TreeNode curr = S.top()
        S.pop()
        // swap left child with right child
        swap(curr.left, curr.right)
        // push right child of popped node to the stack
        if (curr.right)
            S.push(curr.right)
        // push left child of popped node to the stack
        if (curr.left)
            S.push(curr.left)
    }
}
```

For each node in the tree, we are performing push() and pop() operation only once. Total no of stack operations = 2n 

Time complexity: O(n), where n is the total number of nodes.

Space Complexity: O(n)

## Minimum depth of binary tree

The minimum depth of a binary tree is the number of nodes from the root node to the nearest leaf node.

```
public class Solution {
    public int minDepth(TreeNode root) {
        if(root == null) return 0;
        int left = minDepth(root.left);
        int right = minDepth(root.right);
        return (left == 0 || right == 0) ? left + right + 1: Math.min(left,right) + 1;
       
    }
}
```

## Sum of left leaves

Given a Binary Tree, find the sum of all left leaves in it.

The idea is to traverse the tree, starting from root. For every node, check if its left subtree is a leaf. If it is, then add it to the result. 

```
// Java program to find sum of all left leaves
class Node 
{
    int data;
    Node left, right;
  
    Node(int item) 
    {
        data = item;
        left = right = null;
    }
}
  
class BinaryTree 
{
    Node root;
  
    // A utility function to check if a given node is leaf or not
    boolean isLeaf(Node node) 
    {
        if (node == null)
            return false;
        if (node.left == null && node.right == null)
            return true;
        return false;
    }
  
     // This function returns sum of all left leaves in a given
     // binary tree
    int leftLeavesSum(Node node) 
    {
        // Initialize result
        int res = 0;
  
        // Update result if root is not NULL
        if (node != null) 
        {
            // If left of root is NULL, then add key of
            // left child
            if (isLeaf(node.left))
                res += node.left.data;
            else // Else recur for left child of root
                res += leftLeavesSum(node.left);
  
            // Recur for right child of root and update res
            res += leftLeavesSum(node.right);
        }
  
        // return result
        return res;
    }
  
    // Driver program
    public static void main(String args[]) 
    {
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(20);
        tree.root.left = new Node(9);
        tree.root.right = new Node(49);
        tree.root.left.right = new Node(12);
        tree.root.left.left = new Node(5);
        tree.root.right.left = new Node(23);
        tree.root.right.right = new Node(52);
        tree.root.left.right.right = new Node(12);
        tree.root.right.right.left = new Node(50);
  
        System.out.println("The sum of leaves is " + 
                                       tree.leftLeavesSum(tree.root));
    }
}
```

# Graph questions

# Arrays questions

# String questions

## Remove Vowels from a String 

```

import java.util.Scanner; 
  
public class Practice { 
  
    public static void main(String[] args) 
    { 
        Scanner sc = new Scanner(System.in); 
        String s = sc.nextLine(); 
        for (int i = 0; i < s.length(); i++) { 
            if (s.charAt(i) == 'a' || s.charAt(i) == 'e'
                || s.charAt(i) == 'i' || s.charAt(i) == 'o'
                || s.charAt(i) == 'u' || s.charAt(i) == 'A'
                || s.charAt(i) == 'E' || s.charAt(i) == 'I'
                || s.charAt(i) == 'O'
                || s.charAt(i) == 'U') { 
                continue; 
            } 
            else { 
                System.out.print(s.charAt(i)); 
            } 
        } 
    } 
}

```

## First Unique Character in a String

If you have read about hashmaps then, you would know that the lookup time of a key is constant.

We could use the hashmap to store the frequency of each character of the string and that could be done in a single pass of the string.

In another pass of the string, we may look for the first character with value in the map equal to 1. 

```
int firstUniqChar(String s) {
    Create a Hashmap freq
    n = s.length()
    // build hash map : character and how often it appears
    for (int i = 0 to i < n) {
        c = s[i]
        freq[c] = freq[c] + 1
    }   
    // find the index
    for (int i = 0 to i < n) {
        if (freq[s[i]] == 1) 
            return i
    }
    return -1
}
```

## Reverse a string in Java

```
import java.io.*;
import java.util.Scanner;

class GFG {
    public static void main (String[] args) {
      
        String str= "Geeks", nstr="";
        char ch;
      
      System.out.print("Original word: ");
      System.out.println("Geeks"); //Example word
      
      for (int i=0; i<str.length(); i++)
      {
        ch= str.charAt(i); //extracts each character
        nstr= ch+nstr; //adds each character in front of the existing string
      }
      System.out.println("Reversed word: "+ nstr);
    }
}
```

## Valid Anagram

An anagram of a word is basically another word that uses the same letters with the same frequency, just in a different order.

```
class Solution {
    public boolean isAnagram(String S, String T) {
        int len = S.length();
        int[] fMap = new int[123];
        if (T.length() != len) return false;
        for (int i = 0; i < len; i++)
            fMap[S.codePointAt(i)]++;
        for (int i = 0; i < len; i++)
            if (--fMap[T.codePointAt(i)] < 0) return false;
        return true;
    }
}
```

## Valid Palindrome

A palindrome is a string that's written the same forward as backward.

```
var isPalindrome = function(s) {

    let leftIdx = 0;
    let rightIdx = s.length - 1;

    while(leftIdx < rightIdx){
        if (s[leftIdx] !== s[rightIdx]) return false

        rightIdx --
        leftIdx ++ 

    }
    return true
};
```


## Valid Parentheses

Declare a character stack (say temp).
Now traverse the string exp. 
    If the current character is a starting bracket ( ‘(‘ or ‘{‘  or ‘[‘ ) then push it to stack.
    If the current character is a closing bracket ( ‘)’ or ‘}’ or ‘]’ ) then pop from the stack and if the popped character is the matching starting bracket then fine.
    Else brackets are Not Balanced.
After complete traversal, if some starting brackets are left in the stack then the expression is Not balanced, else Balanced.

```
import java.util.*;

public class BalancedBrackets {

    // function to check if brackets are balanced
    static boolean areBracketsBalanced(String expr)
    {
        // Using ArrayDeque is faster than using Stack class
        Deque<Character> stack
            = new ArrayDeque<Character>();

        // Traversing the Expression
        for (int i = 0; i < expr.length(); i++) {
            char x = expr.charAt(i);

            if (x == '(' || x == '[' || x == '{') {
                // Push the element in the stack
                stack.push(x);
                continue;
            }

            // If current character is not opening
            // bracket, then it must be closing. So stack
            // cannot be empty at this point.
            if (stack.isEmpty())
                return false;
            char check;
            switch (x) {
            case ')':
                check = stack.pop();
                if (check == '{' || check == '[')
                    return false;
                break;

            case '}':
                check = stack.pop();
                if (check == '(' || check == '[')
                    return false;
                break;

            case ']':
                check = stack.pop();
                if (check == '(' || check == '{')
                    return false;
                break;
            }
        }

        // Check Empty Stack
        return (stack.isEmpty());
    }

    // Driver code
    public static void main(String[] args)
    {
        String expr = "([{}])";

        // Function call
        if (areBracketsBalanced(expr))
            System.out.println("Balanced ");
        else
            System.out.println("Not Balanced ");
    }
}
```

## Roman to Integer

```
class Solution:
def romanToInt(self, s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]

```

## Longest Substring Without Repeating Characters

## Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

```
class Solution {
    public int removeElement(int[] nums, int val) {
        int result = 0 ;
        int lastNotVal = nums.length-1 ;
        for ( int i=0; i<nums.length; i++ ) {
            if ( nums[i] == val ) {
                nums[i] = 0 ;
                // find not val 
                while( lastNotVal >=0 ) {
                    if ( nums[lastNotVal] != val ) {
                        nums[i] = nums[lastNotVal] ;
                        lastNotVal -- ;
                        break ;
                    }
                    lastNotVal -- ;
                }
            } else {
                result ++ ;
            }
        }
        return result ;
    }
}
```

## Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

```
class Solution {
    public int removeDuplicates(int[] nums) {
        if ( nums.length == 0 ) return 0 ;
        int indexToInsert = 1 ;
        for( int i=1; i< nums.length; i++ ) {
            if( nums[i-1] != nums[i]) {
                nums[indexToInsert++] = nums[i] ;
 //               System.out.println( nums[i] ) ;
            }
        }
        return indexToInsert ;
    }
}
```

## Remove Duplicates from Sorted Array II


Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

```
class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <=2 ) return nums.length ;
        int result = nums.length ;

        int lastIndex = 2 ;
        for ( int i = 2; i<nums.length; i++ ) {
            if ( nums[lastIndex-2] == nums[lastIndex-1] && nums[lastIndex-1] == nums[i] ) {
                result -- ;
            } else {
                nums[lastIndex] = nums[i] ;
                lastIndex ++ ;
            }
        }
        return result ;
    }
}
```

## Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

```
class Solution {
    public void rotate(int[] nums, int k) {
        if ( nums.length <= 1 ) return ;
        if ( k<0 ) return ;

        if ( k > nums.length) k = k % nums.length ;

        int[] result = new int[nums.length] ;
        for( int i = k; i<nums.length; i++ ) {
            result[i] = nums[i-k] ;
        }
        for( int i = 0; i<k; i++ ) {
            result[i] = nums[nums.length-k+i] ;
        }
        for ( int i=0; i<nums.length; i++ ) {
            nums[i]= result[i] ;
        }
    }
}
```

## Best Time to Buy and Sell Stock II

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

```
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length<2) return 0 ;

        int i = 0 ;
        int lo = prices[0] ;
        int hi = prices[0] ;
        int profit = 0 ;
        int n = prices.length ;

        while (i<n-1) {
            // where to buy
            while ( i<(n-1) && prices[i] >= prices[i+1] ) {
                i++ ;
            }
            lo = prices[i] ;

            // where to sell
            while ( i<(n-1) && prices[i] <= prices[i+1] ) {
                i++ ;
            }
            hi = prices[i] ;

            profit += hi-lo ;
        }

        return profit ;
    }
}

```

## Jump Game

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

```
class Solution {
    public boolean canJump(int[] nums) {

        int goal_post = nums.length - 1;

        for (int i = nums.length - 1; i >= 0; i--) {
            int jump_distance = i + nums[i];
            if (jump_distance >= goal_post) {
                goal_post = i;
            }
        }

        return (goal_post == 0) ? true : false;
    }
}
```

## H-Index

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

```
import java.lang.* ;

class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort( citations );
        if ( citations.length == 0 ) return 0;
        if ( citations.length == 1 && citations[0] == 0 ) return Math.min( citations[0], 1 );
        int result = citations[citations.length-1] ;
        for( int i=citations.length-1; i >=0 ; i-- ) {
            if ( citations[i] < (citations.length-i) ) {
                result = citations.length-i-1 ;
                break ;
            }
        }
        return Math.min( result, citations.length) ;
    }
}
```

or

```
class Solution {
    public int hIndex(int[] citations) {

        // Sorting an int[] in reverse in Java is annoying
        // We first sort normally then reverse the array
        Arrays.sort(citations);

        for (int i = 0; i < citations.length/2; i++) {
            int tmp = citations[i];
            citations[i] = citations[citations.length-1-i];
            citations[citations.length-1-i] = tmp;
        }
        int h = 0;
        while (h < citations.length && citations[h] >= h+1) {
            h++;
        }
        return h;
    }
}
```

## Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

```import java.util.* ;

class Solution {
    public int maxArea(int[] height) {
        int result = 0 ;
        int left = 0 ;
        int right = height.length-1;
        int lefth = 0 ;
        int righth = 0 ;
        int minh = 0 ;
        int area = 0 ;
        while( true) {
            lefth = height[ left ] ;
            righth = height[ right ] ;

            // calculate the area
            minh = Math.min( lefth, righth ) ;
            area = minh * (right-left) ;

            result = Math.max( result, area ) ;

            // advance
            if ( lefth <= righth )  left ++ ;
            else right -- ;

            // exit
            if ( left >= right ) break ;

        }
        return result ;
    }
}
```

## Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

```
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if ( s.length() < 1 ) return 0 ;
        int i = 0 ;
        int j = 1 ;
        int result = 1 ;
        while( j<s.length() ) {
//            System.out.println( "i="+i+" j="+j ) ;
            String fullSubstring = s.substring( i, j ) ;
//            System.out.println( "    fullSubstring="+fullSubstring ) ;
            String next = s.substring( j, j+1 ) ;
            if ( fullSubstring.indexOf( next ) < 0 ) {
                j++ ;
                result = Math.max( result, j-i ) ;
 //               System.out.println( "    result="+result ) ;
            } else {
                i++ ;
            }
        }
        return result ;
    }
}
```

## Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

```
class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set[] columns = new TreeSet[9];
        Set[] rows = new TreeSet[9];
        Set[][] rectangles = new TreeSet[3][3];

        // initialize
        for( int x=0; x<9; x++ ) {
            columns[x] = new TreeSet() ;
            rows[x] = new TreeSet() ;
        }
        for( int x=0; x<3; x++ ) {
            for( int y=0; y<3; y++ ) {
                rectangles[x][y] = new TreeSet() ;
            }
        }

        // solve
        boolean result = true ;
        for( int x=0; x<9; x++ ) {
            for( int y=0; y<9; y++ ) {
                char c = board[y][x] ;
                if ( c != '.' ) {
                    int value = c - '0';
 //                   System.out.println( "x="+x+" y="+y+" value="+value ) ;

                    // columns
                    if ( columns[y].contains( value ) ) {
                        result = false ;
 //                       System.out.println( "1 x="+x+" y="+y+" value="+value ) ;
                        break ;
                    }
                    columns[y].add( value ) ;

                    // rows
                    if ( rows[x].contains( value ) ) {
                        result = false ;
//                        System.out.println( "2 x="+x+" y="+y+" value="+value ) ;
                        break ;
                    }
                    rows[x].add( value ) ;

                    // rectangles
                    int recX = (int)Math.floor(x/3) ;
                    int recY = (int)Math.floor(y/3) ;
                    if ( rectangles[recX][recY].contains(value) ) {
 //                       System.out.println( "3 x="+x+" y="+y+" value="+value ) ;
                        result = false ;
                        break ;
                    }
                    rectangles[recX][recY].add(value) ;
                }   
            }
            if ( ! result ) {
                break ;
            }
        }
        return result ;
    }
}

```

## Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

```
class Solution {
    public boolean isAnagram(String s, String t) {
        if ( s.length() != t.length() ) return false ;

        // turn t to Map
        char[] tArray = new char[256] ;
        for ( int i=0; i<t.length(); i++ ) {
            char c = t.charAt(i) ;
            int index = c - '0' ;
//            System.out.println( "char="+c+" index = "+index) ;
            tArray[index]++ ;
        }

        // find s characters
        for ( int i=0; i<s.length(); i++ ) {
            char c = s.charAt(i) ;
            int index = c - '0' ;
 //           System.out.println( "char="+c+" index = "+index) ;
            if ( tArray[index] == 0 ) {
                return false ;
            } else {
                tArray[index]-- ;
            }
        }
        return true ;
    }
}
```

## Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

```
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<List<String>>() ;

        for( int i=0; i<strs.length; i++ ) {
            boolean found = false ;
            Iterator<List<String>> iterator = result.iterator() ;
            while( iterator.hasNext() ) {
                List<String> list = iterator.next() ;
                String anagram = list.get(0) ;
//                System.out.println( "i="+i+" strs[i]="+strs[i]+" anagram="+anagram) ;
                if ( isAnagram( anagram, strs[i] ) ) {
//                    System.out.println( "add" ) ;
                    list.add( strs[i] ) ;
                    found = true ;
                    break ;
                }
            }
            if ( ! found ) {
                // add first element
//                System.out.println( "add new" ) ;
                List<String> list = new ArrayList<String>() ;
                list.add( strs[i] ) ;
                result.add( list ) ;
            }
        }
        return result ;
    }

    public boolean isAnagram(String s, String t) {
        if ( s.length() != t.length() ) return false ;

        // turn t to Map
        char[] tArray = new char[256] ;
        for ( int i=0; i<t.length(); i++ ) {
            char c = t.charAt(i) ;
            int index = c - '0' ;
            tArray[index]++ ;
        }

        // find s characters
        for ( int i=0; i<s.length(); i++ ) {
            char c = s.charAt(i) ;
            int index = c - '0' ;
            if ( tArray[index] == 0 ) {
                return false ;
            } else {
                tArray[index]-- ;
            }
        }
        return true ;
    }
}
```

OR

```
class Solution {
  public List<List<String>> groupAnagrams(String [] strs ) {
	if ( strs.length == 0 ) return new ArrayList() ;
	Map<String, Lists> ans = new HashMap<String, List>() ;
	for( String s: strs ) {
		char[] ca = s.toCharArray() ;
		Arrays.sort( ca ) ;
		String key = String.valueOf( ca ) ;
		if ( ! ans.containsKey( key )) ans.put( key, new ArrayList() ) ;
		ans.get( key ).add( s ) ;
	}
	return new ArrayList( ans.values() ) ;
  }
}
```

## Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

```
public static List<int[]> mergeOverlap(int[][] arr) {
      
        // Sort intervals based on start values
        Arrays.sort(arr, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> res = new ArrayList<>();
        res.add(arr[0]);

        for (int i = 1; i < arr.length; i++) {
            int[] last = res.get(res.size() - 1);
            int[] curr = arr[i];

            // If current overlaps with the last merged, merge them
            if (curr[0] <= last[1]) {
                last[1] = Math.max(last[1], curr[1]);
            } else {
                // Add current to the result
                res.add(curr);
            }
        }

        return res;
    }
```

## Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

```
class Solution {
    private static final Map<String,String> operations = new HashMap<String,String>() ;
    static {
        operations.put("+","+") ;
        operations.put("*","*") ;
        operations.put("-","-") ;
        operations.put("/","/") ;
    }
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<Integer>();
        Integer result = new Integer(0) ;
        for( String token : tokens ) {
            if ( operations.containsKey(token) ) {
                String operation = token ;
                Integer val2 = stack.pop() ;
                Integer val1 = stack.pop() ;
                if ( operation.equals("+") ) {
                    result = new Integer( val1.intValue() + val2.intValue() ) ;
                    stack.push( result ) ;
                } else if ( operation.equals("*") ) {
                    result = new Integer( val1.intValue() * val2.intValue() ) ;
                    stack.push( result ) ;
                } else if ( operation.equals("-") ) {
                    result = new Integer( val1.intValue() - val2.intValue() ) ;
                    stack.push( result ) ;
                } else if ( operation.equals("/") ) {
                    result = new Integer( val1.intValue() / val2.intValue() ) ;
                    stack.push( result ) ;
                }
            } else {
                result = new Integer( Integer.parseInt( token)) ;
                stack.push( result ) ;
            }
        }
        return result;
    }
}
```

## Reverse Linked List 

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

```
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null || left == right) return head;
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;
        
        for (int i = 0; i < left - 1; ++i) {
            prev = prev.next;
        }
        
        ListNode current = prev.next;
        
        for (int i = 0; i < right - left; ++i) {
            ListNode nextNode = current.next;
            current.next = nextNode.next;
            nextNode.next = prev.next;
            prev.next = nextNode;
        }
        
        return dummy.next;
    }
}
```

## Maximum number of overlapping Intervals

The idea is to store coordinates in a new vector of pair mapped with characters ‘x’ and ‘y’, to identify coordinates.

Sort the vector.

Traverse the vector, if an x coordinate is encountered it means a new range is added, so update count and if y coordinate is encountered that means a range is subtracted.

Update the value of count for every new coordinate and take maximum.

```
static class pair
{
    int first;
    char second;
    
    pair(int first, char second)
    {
        this.first = first;
        this.second = second;
    }
}

// Function that print maximum 
// overlap among ranges 
static void overlap(int[][] v) 
{ 
    
    // Variable to store the maximum 
    // count 
    int ans = 0; 
    int count = 0; 
    ArrayList<pair> data = new ArrayList<>(); 
    
    // Storing the x and y 
    // coordinates in data vector 
    for(int i = 0; i < v.length; i++)
    { 
        
        // Pushing the x coordinate 
        data.add(new pair(v[i][0], 'x')); 
  
        // pushing the y coordinate 
        data.add(new pair(v[i][1], 'y')); 
    } 
    
    // Sorting of ranges 
    Collections.sort(data, (a, b) -> a.first - b.first); 
  
    // Traverse the data vector to 
    // count number of overlaps 
    for(int i = 0; i < data.size(); i++) 
    { 
        
        // If x occur it means a new range 
        // is added so we increase count 
        if (data.get(i).second == 'x') 
            count++; 
  
        // If y occur it means a range 
        // is ended so we decrease count 
        if (data.get(i).second == 'y') 
            count--; 
  
        // Updating the value of ans 
        // after every traversal 
        ans = Math.max(ans, count); 
    } 
  
    // Printing the maximum value 
    System.out.println(ans); 
}

// Driver code
public static void main(String[] args) 
{
    int[][] v = { { 1, 2 }, 
                  { 2, 4 }, 
                  { 3, 6 } }; 
    overlap(v); 
}
}
```

## Merge Intervals

```
class Solution {
    public int[][] merge(int[][] intervals) {
        if ( intervals == null || intervals.length ==1 ) return intervals ;

        List<int[]> result = new ArrayList<int[]>() ;
        // sort
        Arrays.sort( intervals, (a1,a2) -> a2[0] > a1[0] ? -1 : a2[0] == a1[0]? a1[1]-a2[1] : 1 ) ;
        
        int[] current = null ;
        // iterate
        for( int i=0; i<intervals.length; i++ ) {
            int[] interval = intervals[i];
            // set current interval
            if ( current == null ) {
                current = interval ;
            } else {
                System.out.println( "i="+i+" current: ["+current[0]+","+current[1]+"]"+" interval: ["+interval[0]+","+interval[1]+"]");
                if ( current[1] >= interval[0] ) {
                    // if new interval overlaps with next then merge
                    if ( interval[1] > current[1] ) {
                        current[1] = interval[1] ;
                    }
                    System.out.println( "  yes  i="+i+" ["+current[0]+","+current[1]+"]");
                    if ( i == (intervals.length-1) ) {
                        result.add( current ) ;
                    }
                } else {
                    System.out.println( "  no  i="+i+" ["+current[0]+","+current[1]+"]");
                    // else set new current interval
                    result.add( current ) ;
                    if ( i == (intervals.length-1) ) {
                        result.add( interval ) ;
                    } else {
                        current = interval ;
                    }
                }
            }
            System.out.println( " i="+i+" ["+current[0]+","+current[1]+"]");
        }
        int[][] result2 = new int[result.size()][2] ;
        for ( int i=0; i<result.size(); i++) {
            result2[i] = result.get(i) ;
        }
        return result2;
    }
}
```

OR

```
class Solution {
    public int[][] merge(int[][] intervals) {
        
        Arrays.sort(intervals,(a,b)->a[0]-b[0]);

        int [][]merged=new int[intervals.length][2];
        int i=0;

        merged[i]=intervals[0];

        for(int j=1;j<intervals.length;j++){
            if(merged[i][1]>=intervals[j][0]){
                merged[i][1]=Math.max(merged[i][1],intervals[j][1]);
            }
            else{
                i++;
                merged[i]=intervals[j];
            }
        }
        return Arrays.copyOf(merged,i+1);
    }
}
```

##  Invert Binary Tree

```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if ( root == null ) return null ;

        TreeNode newRight = root.right ;
        root.right = root.left ;
        root.left = newRight ;

       invertTree( root.right ) ;
       invertTree( root.left ) ;

       return root ;
    }
}

```

## Flatten Binary Tree to Linked List

```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    Queue<TreeNode> queue = new LinkedList<>();
    public void addToQueue(TreeNode root){
        if(root == null){
            return;
        }
        queue.add(root);         
        addToQueue(root.left);
        addToQueue(root.right);
    }
    public void flatten(TreeNode root) {
        addToQueue(root);
        while(!queue.isEmpty()){   
            TreeNode temp = queue.poll();
            temp.right = queue.peek();
            temp.left = null;
        }
    }
}
```

OR

```
class Solution {
    public void flatten(TreeNode root) {
        TreeNode head = null, curr = root;
        while (head != root) {
            if (curr.right == head) curr.right = null;
            if (curr.left == head) curr.left = null;
            if (curr.right != null) curr = curr.right;
            else if (curr.left != null) curr = curr.left;
            else {
                curr.right = head;
                head = curr;
                curr = root;
            }
        }
    }
}
```

## Sum Root to Leaf Numbers

You are given the root of a binary tree containing digits from 0 to 9 only. Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.

Return the total sum of all root-to-leaf numbers.

```
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private List<Integer> allNumbers = new ArrayList<Integer>() ;
    public int sumNumbers(TreeNode root) {
        if ( root == null ) return 0 ;
        if ( root.left == null && root.right == null ) return root.val ;

        int result = 0 ;
        if ( root.left != null ) {
            sumNumbers( root.left, root.val ) ;
        }
        if ( root.right != null ) {
            sumNumbers( root.right, root.val ) ;
        }
        
        // add all
        Iterator<Integer> it = allNumbers.iterator() ;
        while( it.hasNext() ) {
            int val = it.next() ;
            result += val ;
        }

        return result ;
    }
    public void sumNumbers(TreeNode root, int number ) {
        if ( root.left == null && root.right == null ) {
            allNumbers.add( number * 10 + root.val ) ;
            return ;
        }

        if ( root.left != null ) {
            sumNumbers( root.left, number * 10 + root.val ) ;
        }
        if ( root.right != null ) {
            sumNumbers( root.right, number * 10 + root.val ) ;
        } ;
        
    }
}
```

## Find K Pairs with Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

```

```

# References

https://igotanoffer.com/blogs/tech/amazon-software-development-engineer-interview