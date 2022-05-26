class Solution:
    def lengthOfLongestSubstring(self, s):
        list_a = []
        list_b = []
        list_a[:0] = s
        count = 0
        if s == "":
            return 0
        for i in list_a:
            print(i)
            if i not in list_b:
                list_b.append(i)
                count += 1
            else:
                if count < len(list_b):
                    count = len(list_b)
                list_b = [i]
        print(count)
        return count



# s = "pwwkew"
# s = "abcabcbb"
# s = "bbbbb"
# s = ""
# s = "au"
s = "dvdf"
Solution().lengthOfLongestSubstring(s)