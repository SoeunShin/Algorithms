# LeetCode 1736. Latest Time by Replacing Hidden Digits

"""
You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

Input: time = "2?:?0"
Output: "23:50"

Input: time = "0?:3?"
Output: "09:39"

Input: time = "1?:22"
Output: "19:22"
"""

class Solution:
    def maximumTime(self, time: str) -> str:
        answer = ''
        for i in range(5):
            if time[i] == '?':
                if i == 0:
                    if time[1] <= '3' or time[1] == '?':
                        answer += '2'
                    else:
                        answer += '1'
                if i == 1:
                    if answer[0] == '2':
                        answer += '3'
                    else: # str[0] <= '1'
                        answer += '9'
                if i == 3:
                    answer += '5'
                if i == 4:
                    answer += '9'
            else:
                answer += time[i]
        return answer
