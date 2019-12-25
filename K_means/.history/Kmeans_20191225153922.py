"""
 * @Author: wangling 
 * @Date: 2019-12-25 15:08:37 
"""


def load_dataset(file_name):
    data_mat = []
    with open(file_name, 'r') as file:
        for line in file.readline():
            line.strip().split('\t')
            flt_line = map(float, line)
            data_mat.append(flt_line)
    return data_mat


if __name__ == '__main__':
    data = load_dataset('./data/testSet.txt')
    print
                

