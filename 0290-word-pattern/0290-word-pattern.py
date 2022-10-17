class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st = s.split()
        print(st)
        if len(pattern) != len(st):
            return False
        mapping = dict()
        print(len(pattern))
        for i in range(len(pattern)):
            if pattern[i] in mapping.keys():
                if mapping[pattern[i]] != st[i]:
                    return False
            else:
                if st[i] in mapping.values():
                    return False
                mapping[pattern[i]] = st[i]
                print(mapping)
                
        return True
            