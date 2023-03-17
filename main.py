import argparse
import pprint
import numpy

from utils import file_handler, stats_calculator

if __name__ == '__main__':
    ''' Variables '''
    fh = file_handler.File_Handler()
    sc = stats_calculator.Stats_Calculator()
    results = []
    results_diff = []
    results_sim = []

    '''Input Handling'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-p1","--path1", action="store", dest='file_path1')
    parser.add_argument("-p2","--path2", action="store", dest='file_path2')
    parser.add_argument('-i', '--ignore', action="store", required=False,  dest='ignore', nargs='+')
    parser.add_argument('-v', '--verbose',  action="store_true", required=False,  dest='verbose')
    args = parser.parse_args()
    file_path1 = args.file_path1
    file_path2 = args.file_path2
    verbose  = args.verbose
    ignoreList = args.ignore

    '''Get Files From Paths'''
    path1_files = fh.removeIgnoredFiles(fh.getListOfFiles(file_path1), ignoreList) if ignoreList else fh.getListOfFiles(file_path1)
    path2_files = fh.removeIgnoredFiles(fh.getListOfFiles(file_path2), ignoreList) if ignoreList else fh.getListOfFiles(file_path2)

    '''Check if Differing Files Exist'''
    file2_diff = fh.get_files_diff(path2_files, path1_files) # in path2 but not in path1

    '''Create Final List of Files'''
    tmp =  fh.get_diff_files(path2_files, file2_diff)
    all_files = list(path1_files.values()) + tmp


    for i in all_files:
        loc = fh.count_lines(i)
        results.append({i:(0.0,100.0,loc)})

    '''Comparison can be made and the rate of change can be calculated '''
    for key1, val1 in path1_files.items():
        for key2, val2 in path2_files.items():
            if key1 == key2:
                sim, diff = sc.calculate_the_ratios(val1, val2)
                results_diff.append(diff)
                results_sim.append(sim)
                dloc = fh.count_diff_lines(val1,val2)
                for x in results:
                    if val1 in x:
                        x[val1] = (sim,diff,dloc)

    if verbose:
        print("Results")
        pprint.pprint(results)
        print("*************************")
        print("Avg Similarity: " + str(sc.calculate_total_similarity(results)))
        print("Avg Diff: " + str(sc.calculate_total_diff(results)))
        print("Process Completed")
    else:
        print("Results")
        pprint.pprint(results)
        print("*************************")
        print("Avg Diff: " + str(sc.calculate_total_diff(results)))
        print("Process Completed")





