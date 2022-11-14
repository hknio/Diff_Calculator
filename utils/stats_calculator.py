from Levenshtein import *
import numpy
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
        similarities = []
        dlocs = []
        for i in lst:
            tmp = list(i.values())
            similarities.append(tmp[0][0])
            dlocs.append(tmp[0][2])
        return numpy.average(similarities, weights=dlocs)

    def calculate_total_diff(self, lst):
        diffs = []
        dlocs = []
        for i in lst:
            tmp = list(i.values())
            diffs.append(tmp[0][1])
            dlocs.append(tmp[0][2])
        return numpy.average(diffs, weights=dlocs)
