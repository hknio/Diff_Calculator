from Levenshtein import *
import pprint

class Stats_Calculator:
    ''' Functions '''

    def calculate_the_ratios(self, file1, file2):
        with open(file1,'rb') as f1:
            with open(file2, 'rb') as f2:
                f1_str = f1.read()
                f2_str = f2.read()
                similarity = ratio(f1_str, f2_str) * 100
                diff = 100 - similarity
            return similarity, diff
            

    def calculate_total_similarity(self, lst):
        return sum(sim for sim, diff in lst) / len(lst)

    def calculate_total_diff(self, lst):
        return sum(diff for sim, diff in lst) / len(lst)

