class MyStack {
private:
    std::queue<int> stackQueue {};
    std::queue<int> pushQueue {};

public:
    MyStack() {

    }
    
    void push(int x) {
        pushQueue.push(x);
        while(stackQueue.size() > 0) {
            pushQueue.push(stackQueue.front());
            stackQueue.pop();
        }
        std::swap(stackQueue, pushQueue);
    }
    
    int pop() {
        int val {stackQueue.front()};
        stackQueue.pop();
        return val;
    }
    
    int top() {
        return stackQueue.front();
    }
    
    bool empty() {
        return stackQueue.size() == 0;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */