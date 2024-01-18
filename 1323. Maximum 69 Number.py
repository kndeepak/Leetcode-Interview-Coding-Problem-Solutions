class Solution:
    def maximum69Number (self, num: int) -> int:
        
       

            # Convert the number to a string
        number_str = str(num)

        # Convert the number string into a list of digits
        number_list = [int(digit) for digit in number_str]

        # Iterate through the list and replace any digit that is not 6 with 9
        for i in range(len(number_list)):
            if number_list[i] == 6:
                number_list[i] = 9
                break  # Only replace the first non-6 digit

        # Convert the modified list back to an integer
        result = int(''.join(map(str, number_list)))

        return result
