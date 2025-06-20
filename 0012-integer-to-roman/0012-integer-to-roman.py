class Solution:
    symbols = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), 
        ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]
    def intToRoman(self, num: int) -> str:
        sequencia = ""
        for sym, value in self.symbols:
            while(num >= value):
                sequencia += sym
                num -= value

        return sequencia