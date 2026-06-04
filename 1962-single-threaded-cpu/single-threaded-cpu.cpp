class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        int taskId {};
        for (auto& task : tasks) {
            task.push_back(taskId);
            ++taskId;
        } // enqueueTime, processingTime, taskId
        std::sort(tasks.begin(), tasks.end()); // sorted based on enqueueTime

        long curTime {tasks[0][0]};
        int curIndex {};
        using Task = std::tuple<int, int>; // processingTime, taskId
        std::priority_queue<Task, std::vector<Task>, std::greater<Task>> minHeap {};
        std::vector<int> res {};

        while (res.size() < tasks.size()) {
            while (curIndex < tasks.size() && tasks[curIndex][0] <= curTime) {
                minHeap.push({tasks[curIndex][1], tasks[curIndex][2]});
                ++curIndex;
            }

            auto [processingTime, taskId] = minHeap.top();
            minHeap.pop();
            res.push_back(taskId);

            curTime += processingTime;

            // If no tasks in heap and there is still a next task whose time is in the future
            if (minHeap.size() == 0 && curIndex < tasks.size() && curTime < tasks[curIndex][0]) {
                curTime = tasks[curIndex][0];
            }
        }

        return res;
    }
};