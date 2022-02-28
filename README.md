# Tree-Data-Structure

1. [Preorder Traversal (Recursive)](#1-preorder-traversal-recursive)
2. [Inorder Traversal (Recursive)](#2-inorder-traversal-recursive)
3. [Postorder Traversal (Recursive)](#3-postorder-traversal-recursive)
4. [Level Order Traversal](#4-level-order-traversal)
5. [Preorder Traversal (Iterative)](#5-preorder-traversal-iterative)
6. [Inorder Traversal (Iterative)](#6-inorder-traversal-iterative)
7. [Postorder Traversal (Iterative)](#7-postorder-traversal-iterative)
8. [Pre, In, Post Order Traversals in One Traversal](#8-pre-in-post-order-traversals-in-one-traversal)
9. [Maximum Depth in Binary Tree](#9-maximum-depth-in-binary-tree)
10. [Check for Balanced Binary Tree](#10-check-for-balanced-binary-tree)
11. [Diameter of Binary Tree](#11-diameter-of-binary-tree)
12. [Maximum Path Sum in Binary Tree](#12-maximum-path-sum-in-binary-tree)
13. [Check if two trees are identical or not](#13-check-if-two-trees-are-identical-or-not)
14. [Zig-Zag or Spiral Traversal in Binary Tree](#14-zig-zag-or-spiral-traversal-in-binary-tree)
15. [Boundary Traversal in Binary Tree](#15-boundary-traversal-in-binary-tree)
16. [Vertical Order Traversal](#16-vertical-order-traversal)
17. [Top View of Binary Tree](#17-top-view-of-binary-tree)
18. [Bottom View of Binary Tree](#18-bottom-view-of-binary-tree)
19. [Left/Right View of Binary Tree (Right Side)](#19-leftright-view-of-binary-tree-right-side)
20. [Check for Symmetrical Binary Tree](#20-check-for-symmetrical-binary-tree)
21. [Print Root to Node Path in Binary Tree](#21-print-root-to-node-path-in-binary-tree)
22. [Lowest Common Ancestor in Binary Tree](#22-lowest-common-ancestor-in-binary-tree)
23. [Maximum Width of Binary Tree](#23-maximum-width-of-binary-tree)
24. [Children Sum Property in Binary Tree](#24-children-sum-property-in-binary-tree)
25. [Print all Nodes at a distance of K in Binary Tree](#25-print-all-nodes-at-a-distance-of-k-in-binary-tree)
26. [Minimum Time Taken to BURN the Binary Tree](#26-minimum-time-taken-to-burn-the-binary-tree)
27. [Count Total Nodes in Binary Tree](#27-count-total-nodes-in-binary-tree)
28. [Requirements Needed to Construct a Unique Binary Tree](#28-requirements-needed-to-construct-a-unique-binary-tree)
29. [Construct a Binary Tree from PREORDER and INORDER Traversal](#29-construct-a-binary-tree-from-preorder-and-inorder-traversal)
30. [Construct a Binary Tree from POSTORDER and INORDER Traversal](#30-construct-a-binary-tree-from-postorder-and-inorder-traversal)
31. [Serialize and De-Serialize Binary Tree](#31-serialize-and-de-serialize-binary-tree)
32. [Morris Traversal Preorder Inorder](#32-morris-traversal--preorder--inorder)
33. [Flatten a Binary Tree to Linked List](#33-flatten-a-binary-tree-to-linked-list)
34. [Search in BST](#34-search-in-bst)
35. [Ceil in BST](#35-ceil-in-bst)
36. [Floor in BST](#36-floor-in-bst)
37. [Insert a Given Node in BST](#37-insert-a-given-node-in-bst)
38. [Delete a Node in BST](#38-delete-a-node-in-bst)
39. [K-th Smallest and largest Element in BST](#39-k-th-smallest-and-largest-element-in-bst)
40. [Check if a Tree is BST or Not](#40-check-if-a-tree-is-bst-or-not)
41. [Lowest Common Ancestor in BST](#41-lowest-common-ancestor-in-bst)
42. [Construct BST from PREORDER Traversal](#42-construct-bst-from-preorder-traversal)
43. [Inorder Successor/Predecessor in BST](#43-inorder-successorpredecessor-in-bst)
44. [BST Iterator](#44-bst-iterator)
45. [Two Sum in BST Check If There Exists a Pair with Sum K](#45-two-sum-in-bst--check-if-there-exists-a-pair-with-sum-k)
46. [Recover BST Correct BST with Two Nodes Swapped](#46-recover-bst--correct-bst-with-two-nodes-swapped)
47. [Largest BST in Binary Tree](#47-largest-bst-in-binary-tree)
---

## 1. Preorder Traversal (Recursive)

`Root` ` Left ` `Right`

```cpp

void preorder(TreeNode* root) {
    if(root == NULL) return;
    
    cout<<root->val;
    preorder(root->left);
    preorder(root->right);
}

```

## 2. Inorder Traversal (Recursive)

`Left` ` Root ` `Right`

```cpp

void inorder(TreeNode* root) {
    if(root == NULL) return;
    
    inorder(root->left);
    cout<<root->val;
    inorder(root->right);
}

``` 
 
## 3. Postorder Traversal (Recursive)

`Left` ` Right ` `Root`

```cpp

void postorder(TreeNode* root) {
    if(root == NULL) return;
    
    postorder(root->left);
    postorder(root->right);
    cout<<root->val;
}

``` 
 
## 4. Level Order Traversal

1. `Queue` data structure is used (store root first)

```cpp

vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> ans; 
    if(root == NULL) return ans;

    queue<TreeNode*> q; 
    q.push(root); 
    while(!q.empty()) {
        int size = q.size();
        vector<int> level; 
        for(int i = 0;i<size;i++) {
            TreeNode *node = q.front(); 
            q.pop(); 
            if(node->left != NULL) q.push(node->left); 
            if(node->right != NULL) q.push(node->right); 
            level.push_back(node->val); 
        }
        ans.push_back(level); 
    }
    return ans; 
}

``` 
 
## 5. Preorder Traversal (Iterative)

1. `Stack` data structure is used 
2. Although Pre means Root, Left, Right but add as Root, RIGHT, LEFT in stack

```cpp

vector<int> preorderTraversal(TreeNode* root) {
    vector<int> preorder;
    if(root == NULL) return preorder; 
    
    stack<TreeNode*> st; 
    st.push(root);
    while(!st.empty()){
        root = st.top();
        st.pop(); 
        preorder.push_back(root->val); 
        if(root->right != NULL){
            st.push(root->right);
        }
        if(root->left!= NULL){
            st.push(root->left);
        }
    }
    return preorder; 
}

``` 
 
## 6. Inorder Traversal (Iterative)

1. `Stack` data structure is used 
2. Create a TreeNode* node = root
2. while(true)
    - if(node != NULL)
        - Add node's val in stack and keep going left
    - else
        - if(st.empty()) break; 
        - pop the top from stack and store it
        - then go right

```cpp

vector<int> inorderTraversal(TreeNode* root) {
    stack<TreeNode*> st; 
    TreeNode* node = root;
    vector<int> inorder; 
    while(true) {
        if(node != NULL) {
            st.push(node); 
            node = node->left; 
        }
        else {

            if(st.empty() == true) break; 
            node = st.top(); 
            st.pop(); 
            inorder.push_back(node->val); 
            node = node->right; 
        }  
    }
    return inorder; 
}

``` 
 
## 7. Postorder Traversal (Iterative)

1. `Stack` data structure is used 
2. Create a TreeNode* current = root
2. while(true)
    - if(node != NULL)
        - Add node's val in stack and keep going left
    - else
        - if(st.empty()) break; 
        - pop the top from stack and store it
        - then go right

```cpp

vector<int> postorderTraversal(TreeNode* root) {
    vector<int> postorder;
    if(root == NULL) return postorder;

    stack<TreeNode*> st1;
    TreeNode* current = root;  

    while(current != NULL || !st1.empty()) {
        if(current != NULL){
            st1.push(current);
            current = current->left;
        } else {
            TreeNode* temp = st1.top()->right;
            if (temp == NULL) {
                temp = st1.top();
                st1.pop(); 
                postorder.push_back(temp->val);
                while (!st1.empty() && temp == st1.top()->right) {
                    temp = st1.top();
                    st1.pop(); 
                    postorder.push_back(temp->val);
                }
            } else {
                current = temp;
            }
        }
    }
    return postorder;
}

``` 
 
## 8. Pre, In, Post Order Traversals in One Traversal

1. `Stack` data structure is used 
2. Create a stack pair of `stack<node*,int>`
3. Pre: 1, In: 2, Post: 3
4. while(stack isn't empty)
    - auto it = st.top(); 
    - st.pop(); 
    - if(it.second == 1): 
        - add value to array
        - increment it.second
        - st.push(it)
        - if (left != NULL): push {it.first->left, 1}
    - if(it.second == 2): 
        - add value to array
        - increment it.second
        - st.push(it)
        - if (right != NULL): push {it.first->right, 1}
    - if(it.second == 3): 
        - add value to array

```cpp

vector<int> postorderTraversal(TreeNode* root) {
    stack<pair<TreeNode*,int>> st; 
    st.push({root, 1}); 

    vector<int> pre, in, post;
    if(root == NULL) return post;

    while(!st.empty()) {
        auto it = st.top(); 
        st.pop(); 

        // this is part of pre
        // increment 1 to 2 
        // push the left side of the tree
        if(it.second == 1) {
            pre.push_back(it.first->val); 
            it.second++; 
            st.push(it); 

            if(it.first->left != NULL) {
                st.push({it.first->left, 1}); 
            }
        }

        // this is a part of in 
        // increment 2 to 3 
        // push right 
        else if(it.second == 2) {
            in.push_back(it.first->val); 
            it.second++; 
            st.push(it); 

            if(it.first->right != NULL) {
                st.push({it.first->right, 1}); 
            }
        }
        // don't push it back again 
        else {
            post.push_back(it.first->val); 
        }
    } 

    return post; 
}

``` 
 
## 9. Maximum Depth in Binary Tree

1. Find `lh = root -> left`
2. Find `lh = root -> right`
3. `Height = 1 + max(lh, rh)`

```cpp

int height(TreeNode* root) {
    if(root == NULL) return 0; 
    
    int lh = height(root->left); 
    int rh = height(root->right); 
    
    return 1 + max(lh, rh); 
}

``` 
 
## 10. Check for Balanced Binary Tree

1. **Condition:** height(left) - height(right) <= 1
2. Find `lh = root -> left`
    - If lh == -1, return -1
3. Find `lh = root -> right`
    - If rh == -1, return -1
4. Check if lh - rh > 1
5. return height of tree

```cpp

int height(TreeNode *root) {
    if (root == NULL) return 0;
    
    // Left Hight as usual
    int lh = height(root -> left);
    if(lh == -1) return -1;

    // Right Hight as usual
    int rh = height(root -> right);
    if(rh == -1) return -1;
    
    if(abs(lh - rh) > 1)  return -1;

    return 1 + max(lh, rh);
}

bool isBalanced(TreeNode* root) {
    return height(root) != -1;
}

``` 
 
## 11. Diameter of Binary Tree

1. The maximum of lh + rh will be the diameter

```cpp

int height(TreeNode* node, int& diameter) {
    if(root == NULL) return 0;

    int lh = height(node->left, diameter);
    int rh = height(node->right, diameter);

    diameter = max(diameter, lh + rh);
    return 1 + max(lh, rh);
}

int diameterOfBinaryTree(TreeNode* root) {
    int diameter = 0;
    height(root, diameter);
    return diameter;
}

``` 
 
## 12. Maximum Path Sum in Binary Tree

1. Find `max` in lh i.e. `lh = max(0, solve(root->left, maxi))`
2. Find `max` in rh i.e. `rh = max(0, solve(root->right, maxi))`
3. Maximum path sum will be max(maxi, lh + rh + root->val)

```cpp

int maxPathDown(TreeNode* root, int &maxi) {
    if (root == NULL) return 0;

    int lh = max(0, maxPathDown(root->left, maxi));
    int rh = max(0, maxPathDown(root->right, maxi));

    maxi = max(maxi, lh + rh + root->val);
    return root->val + max(lh, rh);
}

int maxPathSum(TreeNode* root) {
    int maxi = INT_MIN; 
    maxPathDown(root, maxi); 
    return maxi;  
}

``` 
 
## 13. Check if two trees are identical or not

1. Iterate both trees together
2. If A is null - check if B is null too?
3. If B is null - check if A is null too?
4. Go left of both and then right of both

```cpp

bool isSameTree(TreeNode* A, TreeNode* B) {
        if(A == NULL) return (B == NULL);
        if(B == NULL) return (A == NULL);

        return  (A->val == B->val) 
                && isSameTree(A->left, B->left)
                && isSameTree(A->right, B->right);
    }

``` 
 
## 14. Zig-Zag or Spiral Traversal in Binary Tree

1. 
2. 
3. 

```cpp

vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (root == NULL) {
        return result;
    }

    queue<TreeNode*> nodesQueue;
    nodesQueue.push(root);
    bool leftToRight = true;

    while ( !nodesQueue.empty()) {
        int size = nodesQueue.size();
        vector<int> row(size);
        for (int i = 0; i < size; i++) {
            TreeNode* node = nodesQueue.front();
            nodesQueue.pop();

            // find position to fill node's value
            int index = (leftToRight) ? i : (size - 1 - i);

            row[index] = node->val;
            if (node->left) {
                nodesQueue.push(node->left);
            }
            if (node->right) {
                nodesQueue.push(node->right);
            }
        }
        // after this level
        leftToRight = !leftToRight;
        result.push_back(row);
    }
    return result;
}

``` 
 
## 15. Boundary Traversal in Binary Tree

1. 
2. 
3. 

```cpp



``` 
 
## 16. Vertical Order Traversal

1. 
2. 
3. 

```cpp



``` 
 
## 17. Top View of Binary Tree

1. Create a map `map<line, val>`
2. Append `val` tp `mp[line]` if mp.find(line) == mp.end()
3. Move left and make line - 1
4. Move right and make line + 1

```cpp

vector<int> topView(Node *root)
{
    vector<int> ans; 
    if(root == NULL) return ans; 

    map<int,int> mp; 
    queue<pair<Node*, int>> q; 

    q.push({root, 0}); 
    while(!q.empty()) {
        auto it = q.front(); 
        q.pop(); 

        Node* node = it.first; 
        int line = it.second; 

        // Only add value if it doesn't exists in map
        if(mp.find(line) == mp.end()) mp[line] = node->data; 
        
        if(node->left != NULL) {
            q.push({node->left, line-1}); 
        }
        if(node->right != NULL) {
            q.push({node->right, line + 1}); 
        }
    }
    
    for(auto it : mp) {
        ans.push_back(it.second); 
    }

    return ans; 
}

``` 
 
## 18. Bottom View of Binary Tree

1. Same as top view but `just add the latest node-val to map[line]`

```cpp

vector <int> bottomView(Node *root) {
    vector<int> ans; 
    if(root == NULL) return ans;

    map<int,int> mp; 
    queue<pair<Node*, int>> q; 

    q.push({root, 0}); 
    while(!q.empty()) {
        auto it = q.front(); 
        q.pop(); 

        Node* node = it.first; 
        int line = it.second; 

        mp[line] = node->data; 
        
        if(node->left != NULL) {
            q.push({node->left, line-1}); 
        }
        if(node->right != NULL) {
            q.push({node->right, line + 1}); 
        }
        
    }
    
    for(auto it : mp) {
        ans.push_back(it.second); 
    }
    return ans;  
}

``` 
 
## 19. Left/Right View of Binary Tree (Right Side)

1. Make a level variable for level order traversal
2. Add root->val if arr.size() == level
3. Now change position to left to add underlying elements

```cpp

void recursion(TreeNode *root, int level, vector<int> &res) {
    if(root==NULL) return;

    if(res.size() == level) res.push_back(root->val);

    recursion(root->right, level+1, res);
    recursion(root->left, level+1, res);
}

vector<int> rightSideView(TreeNode *root) {
    vector<int> res;
    recursion(root, 0, res);
    return res;
}

``` 
 
## 20. Check for Symmetrical Binary Tree

1. Iterate both trees together
2. If A is null - check if B is null too?
3. If B is null - check if A is null too?
4. Go `left - A and right - B` &&  `right - A and left - B`

```cpp

bool solve(TreeNode *A, TreeNode* B) {
    if(A == NULL) return (B == NULL);
    if(B  == NULL) return (A == NULL);

    return (A->val == B->val) 
           && solve(A->left, B->right)
           && solve(A->right, B->left);
}

bool isSymmetric(TreeNode* root) {
    if(root == NULL) return true;

    return solve(root->left, root->right);
}

``` 
 
## 21. Print Root to Node Path in Binary Tree

1. Add root->val to array
2. Check if root->val == x
3. Go `left || right`
4. Pop out the root->val because it hasn't been found

```cpp

@param int x == Node till where the path is to be known

bool getPath(TreeNode *root, vector<int> &arr, int x) {
    if (root == NULL)
        return false;
    
    arr.push_back(root->val);   
     
    if (root->val == x)   
        return true;
     

    if (getPath(root->left, arr, x) || getPath(root->right, arr, x))
        return true;
     

    arr.pop_back();
    return false;  
}

``` 
 
## 22. Lowest Common Ancestor in Binary Tree

1. If root == null or root == any given node p or q - return root
2. Find left by recursion to root->left
3. Find right by recursion to root->right
4. if left == null: return right 

```cpp

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    //base case
    if (root == NULL || root == p || root == q) {
        return root;
    }

    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);

    //result
    if(left == NULL) {
        return right;
    } else if(right == NULL) {
        return left;
    } else { 
        return root;
    }
}

``` 
 
## 23. Maximum Width of Binary Tree

1. `Queue<TreeNode*, int>` is used
2. 
3. 

```cpp

int widthOfBinaryTree(TreeNode* root) {
    if(root == NULL) return 0;

    int ans = 0;
    queue<pair<TreeNode*, int>> q;
    q.push({root,0});

    while(!q.empty()){
        int size = q.size();
        int min_index = q.front().second;    //to make the id starting from zero
        int first,last;

        for(int i=0; i<size; i++){
            int cur_id = q.front().second - min_index; // 2 - 1 = 0
            TreeNode* node = q.front().first;
            q.pop();

            if(i==0) first = cur_id;
            if(i == size-1) last = cur_id;

            if(node->left)
                q.push({node->left, cur_id*2+1});
            if(node->right)
                q.push({node->right, cur_id*2+2});
        }

        ans = max(ans, last-first+1);
    }
    return ans;
}

``` 
 
## 24. Children Sum Property in Binary Tree

1. 
2. 
3. 

```cpp



``` 
 
## 25. Print all Nodes at a distance of K in Binary Tree

1. 
2. 
3. 

```cpp



``` 
 
## 26. Minimum Time Taken to BURN the Binary Tree

1. 
2. 
3. 

```cpp



``` 
 
## 27. Count Total Nodes in Binary Tree

1. 
2. 
3. 

```cpp



``` 
 
## 28. Requirements Needed to Construct a Unique Binary Tree

1. 
2. 
3. 

```cpp



``` 
 
## 29. Construct a Binary Tree from PREORDER and INORDER Traversal

1. 
2. 
3. 

```cpp



``` 
 
## 30. Construct a Binary Tree from POSTORDER and INORDER Traversal

1. 
2. 
3. 

```cpp



``` 
 
## 31. Serialize and De-Serialize Binary Tree

1. 
2. 
3. 

```cpp



``` 
 
## 32. Morris Traversal | Preorder | Inorder

1. 
2. 
3. 

```cpp



``` 
 
## 33. Flatten a Binary Tree to Linked List

```cpp



```

1. 
2. 
3. 

```cpp



``` 

# Binary Search Tree
 
## 34. Search in BST

```cpp

TreeNode* searchBST(TreeNode* root, int k) {
    
    while(root != NULL && root->val != k) {
        if(k > root->val) {
            root = root->right;
        } else {
            root = root->left;
        }
    }
    return root;
}

``` 
 
## 35. Ceil in BST
 
Given a BST and a node k, find the minimum value greater than k.

```cpp

int findCeil(BinaryTreeNode<int> *root, int k){
	int ceil = -1; //Initialize to anything

    while (root) {
        //If k is found, add to ceil
        if (root->data == k) {
            ceil = root->data;
            return ceil;
        }
 
        // k > val, move to right
        if (k > root->data) {
            root = root->right;
        }
        else {
            ceil = root->data; 
            root = root->left;
        }
    }
    return ceil; 
}

``` 
 
## 36. Floor in BST

Given a BST and a node k, find the maximum value smaller than k.

```cpp

int findFloor(BinaryTreeNode<int> *root, int k){
	int floor = -1; //Initialize to anything

    while (root) {
        //If k is found, add to ceil
        if (root->data == k) {
            floor = root->data;
            return floor;
        }
 
        // k > val, move to right
        if (k > root->data) {
            floor = root->data; 
            root = root->right;
        }
        else {
            root = root->left;
        }
    }
    return floor; 
}

``` 
 
## 37. Insert a Given Node in BST

1. If the root is null, return `new Treenode(k)`
2. If `k <= cur->val`
    1. Move left if not null
    2. If null = `cur->left =  new Treenode(k)`
3. If `k > cur->val`
    1. Move right if not null
    2. If null = `cur->right =  new Treenode(k)`

```cpp

TreeNode* insertIntoBST(TreeNode* root, int k) {
    if(root == NULL) return new TreeNode(k);

    TreeNode *cur = root;
    while(true) {
        if(cur->val <= k) {
            if(cur->right != NULL) cur = cur->right;
            else {
                cur->right = new TreeNode(k);
                break;
            }
        } else {
            if(cur->left != NULL) cur = cur->left;
            else {
                cur->left = new TreeNode(k);
                break;
            }
        }
    }
    return root;
}

``` 
 
## 38. Delete a Node in BST

1. Find the `key` in BST
2. Attach it to parent's left/right respectively
3. Find the key's child Last Right Child and attach the leftover Tree

```cpp

TreeNode* findLastRight(TreeNode* root) {
    if (root->right == NULL) {
        return root;
    }
    return findLastRight(root->right);
}

TreeNode* helper(TreeNode* root) {
    if (root->left == NULL) 
    {
        return root->right;
    } 
    else if (root->right == NULL)
    {
        return root->left;
    } 
    TreeNode* rightChild = root->right;
    TreeNode* lastRight = findLastRight(root->left);
    lastRight->right = rightChild;
    return root->left;
}

TreeNode* deleteNode(TreeNode* root, int key) {
    if (root == NULL) {
        return NULL;
    }
    if (root->val == key) {
        return helper(root);
    }
    TreeNode *dummy = root;
    while (root != NULL) {
        if (root->val > key) {
            if (root->left != NULL && root->left->val == key) {
                root->left = helper(root->left);
                break;
            } else {
                root = root->left;
            }
        } else {
            if (root->right != NULL && root->right->val == key) {
                root->right = helper(root->right);
                break;
            } else {
                root = root->right;
            }
        }
    }
    return dummy;
}

``` 
 
## 39. K-th Smallest and largest Element in BST

1. Do the `Inorder Traversal`
2. Instead of adding value to vector, increase the count
3. If count == k, return count (kth smallest value)

**If want to find Kth Largest. then find (N - k)th smallest**

```cpp

int kthSmallest(TreeNode* root, int k) {
    stack<TreeNode*> st; 
    TreeNode* node = root;
    int cnt = 0; 
    while(true) {
        if(node != NULL) {
            st.push(node); 
            node = node->left; 
        }
        else {

            if(st.empty() == true) break; 
            node = st.top(); 
            st.pop(); 
            // inorder.push_back(node->val);
            cnt++; 
            if(cnt == k) return node->val; 
            node = node->right; 
        }  
    }
    return -1;
}

``` 
 
## 40. Check if a Tree is BST or Not

1. Do a Inorder Traversal
2. If arr[i+1] < arr[i] ~ not a BST

```cpp

void ino(TreeNode* root, vector<int>& arr) {
    if(root == NULL) return;
    
    ino(root->left, arr);
    arr.push_back(root->val);
    ino(root->right, arr);
}

bool isValidBST(TreeNode* root) {
    vector<int> arr;
    int count = 0;
    ino(root, arr);
    for(int i=0; i<arr.size()-1; i++) {
        if(arr[i] >= arr[i+1]) {
            count = 1;
        }
    }
    if(count == 1) return false;
    return true;
}

// ------------------------------------------------------------

bool isValidBST(TreeNode* root) {
    return isValidBST(root, INT_MIN, INT_MAX);
}

bool isValidBST(TreeNode* root, long minVal, long maxVal) {
    if (root == NULL) return true;

    if (root->val >= maxVal || root->val <= minVal) return false;
    return isValidBST(root->left, minVal, root->val) && isValidBST(root->right, root->val, maxVal);
}

``` 
 
## 41. Lowest Common Ancestor in BST

1. Find the common split between two nodes
2. Move `Right` if `curr < (A, B)`
3. Move `Left` if `curr > (A, B)`

```cpp

TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* A, TreeNode* B) {
    if(root == NULL) return NULL;

    int curr = root->val; 

    if(curr < A->val && curr < B->val) {
        return lowestCommonAncestor(root->right, A, B);
    }
    if(curr > A->val && curr > B->val) {
        return lowestCommonAncestor(root->left, A, B);
    }
    return root;
}

``` 
 
## 42. Construct BST from PREORDER Traversal

```cpp



```

1. 
2. 
3. 

```cpp



``` 
 
## 43. Inorder Successor/Predecessor in BST

1. 
2. 
3. 

```cpp



``` 
 
## 44. BST Iterator

1. 
2. 
3. 

```cpp



``` 
 
## 45. Two Sum in BST | Check If There Exists a Pair with Sum K

1. 
2. 
3. 

```cpp



``` 
 
## 46. Recover BST | Correct BST with Two Nodes Swapped

1. 
2. 
3. 

```cpp



``` 
 
## 47. Largest BST in Binary Tree

1. 
2. 
3. 

```cpp



``` 
