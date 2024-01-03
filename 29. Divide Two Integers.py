class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle the case of dividend being INT_MIN and divisor being -1 (overflow)
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Take the absolute values of dividend and divisor
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        while abs_dividend >= abs_divisor:
            temp_divisor, multiple = abs_divisor, 1
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            abs_dividend -= temp_divisor
            quotient += multiple

        # Determine the sign of the result based on the signs of dividend and divisor
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            quotient = -quotient

        return quotient
