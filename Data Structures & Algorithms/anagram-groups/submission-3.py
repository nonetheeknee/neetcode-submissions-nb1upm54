class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        skip = []
        count = [None] * len(strs)
        print(count)

        for i in range(0,len(strs)):
            if i not in skip:
                sublist = []
                sublist.append(strs[i])
                set_1 = set(strs[i])
                print(count[i])
                if count[i] == None:
                    dict_1 = {}
                    for char in strs[i]:
                        if char not in dict_1.keys():
                            dict_1[char] = 1
                        else:
                            dict_1[char] += 1
                    count[i] = dict_1
                    print(count)
        

                for j in range (i+1, len(strs)):
                    print("i=",i)
            
                    if count[j] == None:
                        dict_1 = {}
                        for char in strs[j]:
                            if char not in dict_1.keys():
                                dict_1[char] = 1
                            else:
                                dict_1[char] += 1
                        count[j] = dict_1
                        print(count)
                    if count[i] == count[j]:
                        sublist.append(strs[j])
                        skip.append(j)

                result.append(sublist) 
           
    

        return result