import unittest
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))


def run_all_tests():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    test_root_directory = os.path.join(current_directory)
    loader = unittest.TestLoader()

    # init empty test suite
    all_tests_suite = unittest.TestSuite()

    # recursively find and load all tests in subdirectories
    for root, dirs, files in os.walk(test_root_directory):
        for file in files:
            if file.endswith("test.py"):
                test_directory = os.path.relpath(root, current_directory)
                test_module = file[:-3]
                full_module_path = f"{test_directory}.{test_module}"
                test_suite = loader.loadTestsFromName(full_module_path)
                all_tests_suite.addTest(test_suite)

    # Run test suite
    unittest.TextTestRunner(verbosity = 0).run(all_tests_suite)

if __name__ == "__main__":
    run_all_tests()
