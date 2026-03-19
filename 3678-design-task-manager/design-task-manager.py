class Task:

    def __init__(self, userId: int, taskId: int, priority: int):
        self.userId = userId
        self.taskId = taskId
        self.priority = priority
        self.isDeleted = False

    def delete(self) -> None:
        self.isDeleted = True

    def __lt__(self, other) -> bool:
        if self.priority != other.priority:
            return self.priority > other.priority
        
        return self.taskId > other.taskId
     
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.ranking = []
        self.tasks = {}

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = Task(userId, taskId, priority)
        self.tasks[taskId] = task
        heapq.heappush(self.ranking, task)

    def edit(self, taskId: int, newPriority: int) -> None:
        task = self.tasks[taskId]
        task.delete()
        self.add(task.userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        task = self.tasks[taskId]
        task.delete()

    def execTop(self) -> int:
        while self.ranking and self.ranking[0].isDeleted:
            heapq.heappop(self.ranking)
        
        if not self.ranking:
            return -1

        task = heapq.heappop(self.ranking)
        return task.userId

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()