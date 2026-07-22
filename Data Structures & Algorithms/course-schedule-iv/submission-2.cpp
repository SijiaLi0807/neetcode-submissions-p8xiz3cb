class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        vector<vector<int>> edge(numCourses);
        vector<int> indegree(numCourses, 0);
        vector<vector<bool>> isPre(numCourses, vector<bool>(numCourses, false));

        for (auto& p: prerequisites){
            ++indegree[p[1]];
            edge[p[0]].push_back(p[1]);
        }

        queue<int> q;
        for (int i = 0; i < numCourses; ++i){
            if (indegree[i]==0){
                q.push(i);
            }
        }

        while (!q.empty()){
            auto cur = q.front();
            q.pop();
            for (auto& ne: edge[cur]){
                isPre[cur][ne] = true;
                for (int i = 0; i < numCourses; ++i){
                    if (isPre[i][cur]){isPre[i][ne] = true;}
                    //isPre[i][ne] | isPre[i][cur];
                }
                --indegree[ne];
                if (indegree[ne] == 0) {
                    q.push(ne);
                }
            } 
        }

        vector<bool> res;
        for (auto& query: queries){
            res.push_back(isPre[query[0]][query[1]]);
        }
        return res;
    }
};