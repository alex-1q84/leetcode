__author__ = 'mywo'
'''The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.
'''


def _split_number(n):
    """
    :param n:
    :return:
    21   -> [1,2]
    1211 -> [1, 1, 2, 1]
    """
    numbers = []
    div, mod = divmod(n, 10)
    while div:
        numbers.append(mod)
        div, mod = divmod(div, 10)
    numbers.append(mod)
    return numbers


def _append_and_reset(prev, same_count, result):
    # check if need append to the result
    if same_count != 0:
        result.append(str(same_count))
        result.append(str(prev))
    # reset the same_count and prev
    same_count = 0
    prev = None
    return prev, same_count


def say_a_number(c):
    if not c:
        return "1"

    num_say_list = []
    prev = None
    same_count = 0
    num_stack = _split_number(c)
    while num_stack:
        number = num_stack.pop()
        # check if same to prev then increase the same_count
        # else append the same_count if it is not 0 and the prev is not None
        if number == prev:
            same_count += 1
        elif prev is None:
            same_count += 1
            prev = number
        else:
            prev, same_count = _append_and_reset(prev, same_count, num_say_list)
            same_count += 1
            prev = number
    _append_and_reset(prev, same_count, num_say_list)
    return "".join(num_say_list)


class Solution:
    # @return a string

    def countAndSay(self, n):
        """
        :param n: number
        :return: string
        """
        result = []
        for i in range(n):
            try:
                last = result.pop()
            except:
                last = 0
            result.append(say_a_number(int(last)))
        return str(result.pop())
