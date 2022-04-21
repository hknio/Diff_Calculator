from Levenshtein import *


class Stats_Calculator:
    ''' Functions '''

    def calculate_the_ratios(self, file1, file2):
        with open(file1) as f1:
            with open(file2) as f2:
                similarity = ratio(file1, file2) * 100
                diff = 100 - similarity
            return similarity, diff

    def calculate_total_similarity(self, lst):
        return sum(sim for sim, diff in lst) / len(lst)

    def calculate_total_diff(self, lst):
        return sum(diff for sim, diff in lst) / len(lst)

