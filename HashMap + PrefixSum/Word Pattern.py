class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(pattern) != len(s):
            return False

        p_s_map = {}
        s_p_map = {}

        for i, j in zip(pattern, s):
            if i in p_s_map and p_s_map[i] != j:
                return False

            if j in s_p_map and s_p_map[j] != i:
                return False

            p_s_map[i] = j
            s_p_map[j] = i

        return True