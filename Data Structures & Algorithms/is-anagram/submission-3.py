class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 : dict[str, int] = {}
        count2 : dict[str, int] = {}

        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in count1:
                    count1[s[i]] = count1[s[i]] + 1
                else:
                    count1[s[i]] = 1

                if t[i] in count2:
                    count2[t[i]] = count2[t[i]] + 1
                else:
                    count2[t[i]] = 1

            if not len(count1) == len(count2):
                return False

            for key, value in count1.items():
                count2_key_count = count2.get(key)

                if count2_key_count == "N/A":
                    return False

                if not value == count2_key_count:
                    return False

            return True

        else:
            return False

        