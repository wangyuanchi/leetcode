struct Node {
    int val {};
    Node* next {};
};

class MyCircularQueue {
private:
    int maxNodeCount {};
    int curNodeCount {};
    Node* head {};
    Node* tail {};
    
public:
    MyCircularQueue(int k) : maxNodeCount{k} {
        
    }

    bool enQueue(int value) {
        if (curNodeCount == maxNodeCount) {
            return false;
        }
        Node* elemPtr {new Node{value}};
        if (curNodeCount == 0) {
            head = elemPtr;
            tail = elemPtr;
        } else {
            tail->next = elemPtr;
            tail = tail->next;
        }
        ++curNodeCount;
        return true;
    }
    
    bool deQueue() {
        if (curNodeCount == 0) {
            return false;
        }
        if (curNodeCount == 1) {
            delete head;
            head = tail = nullptr;
        } else {
            Node* temp {head};
            head = head->next;
            delete temp;
        }
        --curNodeCount;
        return true;
    }
    
    int Front() {
        if (!head) {
            return -1;
        }
        return head->val;
    }
    
    int Rear() {
        if (!tail) {
            return -1;
        }
        return tail->val;
    }
    
    bool isEmpty() {
        return curNodeCount == 0;
    }
    
    bool isFull() {
        return curNodeCount == maxNodeCount;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */