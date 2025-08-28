class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        l, r = 0, len(products) - 1 # [l, r] is the current valid range of strings
        res = []

        for i in range(len(searchWord)):
            temp = []
            char = searchWord[i]

            while l <= r:
                if i >= len(products[l]) or products[l][i] != char:
                    l += 1
                else:
                    break
            
            while l <= r:
                if i >= len(products[r]) or products[r][i] != char:
                    r -= 1
                else:
                    break

            for i in range(l, r + 1):
                if len(temp) < 3:
                    temp.append(products[i])
                else:
                    break

            res.append(temp)

        return res