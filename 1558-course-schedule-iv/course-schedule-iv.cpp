class Solution {
public:
    vector<bool> checkIfPrerequisite(int numCourses, vector<vector<int>>& prerequisites, vector<vector<int>>& queries) {
        std::unordered_map<int, std::vector<int>> adj_list {};
        std::vector<int> indegree (numCourses);
        for (const auto& prereq : prerequisites) {
            adj_list[prereq[0]].push_back(prereq[1]);
            ++indegree[prereq[1]];
        }

        std::unordered_map<int, std::unordered_set<int>> parents {};
        std::queue<int> q {};
        for (int i{}; i < numCourses; ++i) {
            if (!indegree[i]) {
                q.push(i);
            }
        }

        while (q.size() > 0) {
            int node {q.front()};
            q.pop();
            for (int neighbour : adj_list[node]) {
                --indegree[neighbour];
                if (!indegree[neighbour]) {
                    q.push(neighbour);
                }
                parents[neighbour].insert(node);
                for (int n : parents[node]) {
                    parents[neighbour].insert(n);
                }
            }
        }

        std::vector<bool> res {};
        for (const auto& query : queries) {
            res.push_back(parents[query[1]].contains(query[0]));
        }
        return res;
    }
};