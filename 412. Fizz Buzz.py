from typing import List

def fizzBuzz(self, n: int) -> List[str]:
    output = []
    for i in range(1, n + 1):
        match i:
            case _ if i % 3 == 0 and i % 5 == 0:
                output.append("FizzBuzz")
            case _ if i % 3 == 0:
                output.append("Fizz")
            case _ if i % 5 == 0:
                output.append("Buzz")
            case _:
                output.append(str(i))

    return output
