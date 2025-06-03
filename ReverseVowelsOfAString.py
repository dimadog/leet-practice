class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_list = ['a', 'e', 'i', 'o', 'u']
        char_list = list(s)
        vowel_index = []
        index = 0
        for char in char_list:
            if char.casefold() in vowels_list:
                vowel_index.append(index)
            index += 1
        parity = len(vowel_index)//2
        for i in vowel_index:
            if parity >0:
                fst_ch = char_list[i]
                lst_inx = vowel_index[-1]
                lst_ch = char_list[vowel_index.pop()]
                char_list[i] = lst_ch
                char_list[lst_inx] = fst_ch
                parity -= 1
        return ''.join(char_list)