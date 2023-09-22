import argparse
import os
import shutil


def _main(sqllogictest_rs_path, src_dir, test_dir, dest_dir):
    # create dest_dir if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # copy all files from src_dir to dest_dir
    for filename in os.listdir(src_dir):
        file_path = os.path.join(src_dir, filename)
        if (os.path.isfile(file_path)):
            shutil.copy(file_path, dest_dir)
            print("copied file: " + file_path)
        else:
            print("skipped file: " + file_path)

    print(sqllogictest_rs_path)

    # Get test files

    test_file_paths = []

    # append all test file paths to test_file_paths
    # recursively search for all files .slt in test_dir
    print(test_dir)
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            if file.endswith(".slt"):
                test_file_paths.append(os.path.join(root, file))

    # run sqllogictest-rs for each test file
    for test_file_path in test_file_paths:
        print("running test file: " + test_file_path)
        # run sqllogictest-rs
        os.system(sqllogictest_rs_path + " " + test_file_path)

        print("finished running test file: " + test_file_path)
        print("----------------------------------------------------------\n")

    print(len(test_file_paths))


def main():
    # get current directory
    current_path = os.getcwd()
    print(current_path)
    # get parent directory
    # parent_path = os.path.dirname(current_path)
    # print(parent_path)
    parent_path = current_path
    src_dir = parent_path + '/test/data/csv'

    test_dir = parent_path + '/test/sql'

    dest_dir = '/tmp/infinity/sqllogictest'

    parser = argparse.ArgumentParser(description='SQL Logic Test For Infinity')

    parser.add_argument('-p', '--path', help='path of sqllogictest-rs', type=str, default='./tools/sqllogictest', dest='path')
    parser.add_argument('-s', '--src', help='path of src directory', type=str, default=src_dir, dest='src')
    parser.add_argument('-t', '--test', help='path of test directory', type=str, default=test_dir, dest='test')
    parser.add_argument('-d', '--dest', help='path of dest directory', type=str, default=dest_dir, dest='dest')

    args = parser.parse_args()

    # get bin sqllogictest-rs path from input argument

    _main(args.path, args.src, args.test, args.dest)

    return


# main
if __name__ == '__main__':
    main()
