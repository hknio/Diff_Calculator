import argparse
import pprint

from utils import file_handler, stats_calculator

if __name__ == '__main__':
    ''' Variables '''
    fh = file_handler.File_Handler()
    sc = stats_calculator.Stats_Calculator()
    results = []

    '''Input Handling'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-p1","--path1", action="store", dest='file_path1')
    parser.add_argument("-p2","--path2", action="store", dest='file_path2')
    parser.add_argument('-v', '--verbose',  action="store_true", required=False,  dest='verbose')
    args = parser.parse_args()
    file_path1 = args.file_path1
    file_path2 = args.file_path2
    verbose  = args.verbose

    '''Get Files From Paths'''
    path1_files = fh.getListOfFiles(file_path1)
    path2_files = fh.getListOfFiles(file_path2)

    '''Check if Differing Files Exist & Remove differing files'''
    file1_diff = fh.get_files_diff(path1_files, path2_files) # in path1 but not in path2
    file2_diff = fh.get_files_diff(path2_files, path1_files) # in path1 but not in path2

    if len(file1_diff) > 0 and len(file1_diff) == 0:
        fh.remove_diff_files(file1_diff, path1_files)
    elif len(file2_diff) > 0 and len(file1_diff) == 0:
        fh.remove_diff_files(file2_diff, path2_files)

    '''Now that the common files are determined, comparison can be made and the rate of change can be calculated '''
    for key1, val1 in path1_files.items():
        for key2, val2 in path2_files.items():
            if key1 == key2:
                sim, diff = sc.calculate_the_ratios(val1, val2)
                results.append((sim, diff))

    if verbose:
        print("Results")
        pprint.pprint(results)
        print("*************************")
        print("Total Similarity: " + str(sc.calculate_total_similarity(results)))
        print("Total Diff: " + str(sc.calculate_total_diff(results)))
        print("Process Completed")
    else:
        print("Total Diff: " + str(sc.calculate_total_diff(results)))
        print("Process Completed")





