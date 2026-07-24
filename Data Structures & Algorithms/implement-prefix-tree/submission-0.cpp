#include <cstring>
#include <string>
using namespace std;

class PrefixTree {
private:
    bool isEnd;
    PrefixTree* next[26];

public:
    PrefixTree() {
        isEnd = false;
        memset(next, 0, sizeof(next));   // 将所有指针置为 nullptr
    }
    
    void insert(string word) {
        PrefixTree* node = this;
        for (char c : word) {
            int idx = c - 'a';
            if (node->next[idx] == nullptr) {
                node->next[idx] = new PrefixTree();
            }
            node = node->next[idx];
        }
        node->isEnd = true;
    }
    
    bool search(string word) {
        PrefixTree* node = this;
        for (char c : word) {
            node = node->next[c - 'a'];
            if (node == nullptr) return false;
        }
        return node->isEnd;   // 关键：确保完整单词
    }
    
    bool startsWith(string prefix) {
        PrefixTree* node = this;
        for (char c : prefix) {
            node = node->next[c - 'a'];
            if (node == nullptr) return false;
        }
        return true;
    }
};