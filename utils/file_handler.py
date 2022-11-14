import os
import pprint

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
            elif ".DS_Store" in l or ".gitkeep" in l:
                continue
            else:
                return None
        return res

    def _getListOfFiles(self, dirName):
        listOfFile = os.listdir(dirName)
        allFiles = list()
        for entry in listOfFile:
            if entry.startswith("."):
                continue
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

    def get_diff_files(self, dfs, lst):
        result = []
        for i in lst:
            if dfs[i]:
                result.append(dfs[i])
        return result

    
    def _count_generator(self, reader):
        b = reader(1024 * 1024)
        while b:
            yield b
            b = reader(1024 * 1024)
    
    def count_diff_lines(self,f1,f2):
        count1 = 0
        count2 = 0
        with open(f1, 'rb') as fp1:
            c_generator = self._count_generator(fp1.raw.read)
            count1 = sum(buffer.count(b'\n') for buffer in c_generator)
        with open(f2, 'rb') as fp2:
            c_generator = self._count_generator(fp2.raw.read)
            count2 = sum(buffer.count(b'\n') for buffer in c_generator)
        return abs(count1 - count2)
    
    def count_lines(self, f):
        with open(f, 'rb') as fp:
            c_generator = self._count_generator(fp.raw.read)
            count = sum(buffer.count(b'\n') for buffer in c_generator)
            return count
