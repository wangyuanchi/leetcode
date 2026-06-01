class NumMatrix {
private:
    std::vector<std::vector<int>> prefix;
public:
    NumMatrix(vector<vector<int>>& matrix)
    : prefix(matrix.size() + 1, std::vector<int>(matrix[0].size() + 1))
    {
        for (int row{1}; row < prefix.size(); ++row) {
            for (int col{1}; col < prefix[0].size(); ++col) {
               prefix[row][col] = matrix[row - 1][col - 1] + prefix[row - 1][col]
                    + prefix[row][col - 1] - prefix[row - 1][col - 1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        ++row1; ++col1; ++row2; ++col2;
        return prefix[row2][col2] - prefix[row2][col1 - 1]
            - prefix[row1 - 1][col2] + prefix[row1 - 1][col1 - 1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */