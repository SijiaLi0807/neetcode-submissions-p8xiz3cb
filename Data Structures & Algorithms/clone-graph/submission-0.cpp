/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
//为什么哈希表存指针？因为node的计算（根据定义）用指针
    unordered_map<Node*, Node*> visited;
    Node* cloneGraph(Node* node) {
        if (node == nullptr){
            return node;
        }

        if (visited.find(node) != visited.end()){
            return visited[node];
        }

        Node* cloneNode = new Node(node->val);//new: 为了保证“克隆出来的节点”在函数执行结束后，依然存活在内存中。

        //哈希表存储
        visited[node] = cloneNode;

        //存储邻居
        for (auto& neighbor: node->neighbors){
            cloneNode->neighbors.push_back(cloneGraph(neighbor)); //调用自身函数
            //用emplace_back避免构造临时对象
        }

        return cloneNode;
    }
};
