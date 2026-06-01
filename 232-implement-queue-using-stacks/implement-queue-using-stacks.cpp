class MyQueue {
private:
    vector<int> pushStack {};
    vector<int> popStack {};
public:
    MyQueue() {
        
    }
    
    void push(int x) {
        pushStack.push_back(x);
    }

    void transfer() {
        while (pushStack.size() > 0) {
            popStack.push_back(pushStack.back());
            pushStack.pop_back();
        }
    }
    
    int pop() {
        if (popStack.size() > 0) {
            int val {popStack.back()};
            popStack.pop_back();
            return val;
        }

        transfer();
        
        int val {popStack.back()};
        popStack.pop_back();
        return val;
    }
    
    int peek() {
        if (popStack.size() > 0) return popStack.back();
        transfer();
        return popStack.back();
    }
    
    bool empty() {
        return pushStack.size() + popStack.size() == 0;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */