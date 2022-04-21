import os

class File_Handler:

    '''Functions'''

    def convert_to_dict(self, file_paths, file_names):
        return dict(zip(file_names, file_paths))

    def seperate_name_from_dir(self, lst):
        res = []
        for l in lst:
            if ".sol" in l:
                dir_end_index = l.rfind("/")
                res.append(l[dir_end_index + 1:])
            elif ".DS_Store" in l:
                continue
            else:
                return None
        return res

    def _getListOfFiles(self, dirName):
        listOfFile = os.listdir(dirName)
        allFiles = list()
        for entry in listOfFile:
            fullPath = os.path.join(dirName, entry)
            if os.path.isdir(fullPath):
                allFiles = allFiles + self._getListOfFiles(fullPath)
            else:
                allFiles.append(fullPath)
        return allFiles

    def getListOfFiles(self, lst):
        file_paths = self._getListOfFiles(lst)
        file_names = self.seperate_name_from_dir(file_paths)
        return self.convert_to_dict(file_paths=file_paths, file_names= file_names)

    def file_names_match(self, keyword, filename):
        if keyword in filename:
            return True
        else:
            return False

    def get_files_diff(self, files1, files2):
        file1_keys = list(files1.keys())
        file2_keys = list(files2.keys())
        diff = list(set(file1_keys) - set(file2_keys))
        return diff

    def remove_diff_files(self, dfs, lst):
        for i in dfs:
            del lst[i]