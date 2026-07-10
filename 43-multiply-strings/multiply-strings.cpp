class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") {
            return "0";
        }

        if (num1.size() < num2.size()) {
            std::swap(num1, num2);
        }

        std::vector<int> res (num1.size() + num2.size() + 1);
        std::reverse(num1.begin(), num1.end());
        std::reverse(num2.begin(), num2.end());

        for (int i{}; i < num2.size(); ++i) {
            for (int j{}; j < num1.size(); ++j) {
                int num1digit {num1[j] - '0'};
                int num2digit {num2[i] - '0'};
                int sum {num1digit * num2digit};
                int remain {sum % 10};
                int carry {sum / 10};
                res[i + j] += remain;
                res[i + j + 1] += carry;
            }
        }

        for (int i{}; i < res.size(); ++i) {
            int val {res[i]};
            res[i] = val % 10;
            if (i != res.size() - 1) {
                res[i + 1] += val / 10; 
            }
        }
        
        std::string res_string {};
        bool leadingZeros {true};
        for (int i = res.size() - 1; i >= 0; --i) {
            if (res[i] != 0) {
                leadingZeros = false;
                res_string += static_cast<char>(res[i] + '0');
            } else if (!leadingZeros) {
                res_string += static_cast<char>(res[i] + '0');
            }
        }

        return res_string;
    }
};