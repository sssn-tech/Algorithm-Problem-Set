/*
 * @lc app=leetcode.cn id=208 lang=cpp
 *
 * [208] 实现 Trie (前缀树)
 */

// @lc code=start
class TrieNode{
public:
    vector<TrieNode*> sons;
    bool end;
    TrieNode() {
        sons = vector<TrieNode*>(26, nullptr);
        end = false;
    }
};

class Trie {
private:
    TrieNode* root;

    int find(string& word) {
        // -1: can't find, 1: prefix match, 2: complete match
        TrieNode* curr = root;
        for (auto& ch : word) {
            int c = ch - 'a';
            if (curr->sons[c] == nullptr) {
                return -1;
            }
            curr = curr->sons[c];
        }
        return curr->end ? 2 : 1;
    }

public:
    
    Trie() {
        root = new TrieNode();
    }

    
    void insert(string word) {
        TrieNode* curr = root;
        for (auto& ch : word) {
            int c = ch - 'a';
            if (curr->sons[c] == nullptr) {
                curr->sons[c] = new TrieNode();
            }
            curr = curr->sons[c];
        }
        curr->end = true;
    }
    
    bool search(string word) {
        return find(word) == 2;
    }
    
    bool startsWith(string prefix) {
        int res = find(prefix);
        return res == 1 || res == 2;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// @lc code=end

