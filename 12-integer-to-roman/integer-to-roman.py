class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        subtractive_form = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
        }
        roman = ""
        while num > 0:
            starting_value = str(num)[0]
            if starting_value != "4" and starting_value != "9":
                dict_to_search = symbols
            else:
                dict_to_search = subtractive_form
            for k, v in dict_to_search.items():
                if num - v >= 0:
                    num -= v
                    roman += k
                    break
        return roman
