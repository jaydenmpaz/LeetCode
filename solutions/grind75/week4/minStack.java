class MinStack {
    private List<int[]> st;

    public MinStack() {
        st = new ArrayList<>();
    }
    
    public void push(int val) {
        int[] top = st.isEmpty() ? new int[]{val, val} : st.get(st.size() - 1);
        int min_val = top[1];
        if (min_val > val) {
            min_val = val;
        }
        st.add(new int[]{val, min_val});  
    }
    
    public void pop() {
        st.remove(st.size() - 1);
    }
    
    public int top() {
        if (!st.isEmpty()) {
            return st.get(st.size()-1)[0];
        } else {
            return -1;
        }
    }
    
    public int getMin() {
        if (!st.isEmpty()) {
            return st.get(st.size()-1)[1];
        } else {
            return -1;
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */