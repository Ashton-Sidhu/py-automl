import unittest

import numpy as np
import pandas as pd
import shutil
from pathlib import Path

from aethos.core import Data


class Test_TestBase(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        report_path = str(Path.home()) + "/.aethos/reports/"

        if Path(report_path).exists():
            shutil.rmtree(report_path)

    def test_compare_dist_predict(self):

        data = np.random.randint(0, 2, size=(1000, 3))
        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        df = Data(data, target_field="col3", report_name="test")
        df.predict_data_sample()

        self.assertTrue(True)

    def test_compare_dist_ks(self):

        data = np.random.randint(0, 2, size=(1000, 3))
        data = pd.DataFrame(data=data, columns=["col1", "col2", "col3"])

        df = Data(data, target_field="col3", report_name="test")
        df["col4"] = np.random.normal(1, 2, size=(1, 800))[0]
        df["col4"] = np.random.normal(10, 20, size=(1, 200))[0]
        df.ks_feature_distribution()

        self.assertTrue(True)

    def test_most_common_list(self):

        data = pd.Series([["hi", "aethos"], ["hi", "py-automl"], [], ["hi"]])
        data = pd.DataFrame(data, columns=["col1"])

        df = Data(data, split=False)
        df.most_common("col1", plot=True)

        self.assertTrue(True)

    def test_most_common_str(self):

        data = pd.Series(
            [
                "hi aethos",
                "aethos is awesome",
                "hi",
                "py-automl is the old name",
                "hi everyone",
            ]
        )
        data = pd.DataFrame(data, columns=["col1"])

        df = Data(data, split=False)
        df.most_common("col1")

        self.assertTrue(True)

    def test_most_common_int(self):

        data = pd.Series([1, 1, 2, 4, 2, 5])
        data = pd.DataFrame(data, columns=["col1"])

        df = Data(data, test_split_percentage=0.5)
        df.most_common("col1", plot=True, use_test=True)

        self.assertTrue(True)

    def test_2s_ttest_atterror(self):

        data1 = np.random.normal(0, 1, size=50)
        data2 = np.random.normal(2, 1, size=50)

        data = pd.DataFrame({"d1": data1, "d2": data2})

        df = Data(data, split=False)

        self.assertRaises(AttributeError, df.paired_ttest, "d1")

    def test_2s_pairedttest(self):

        data1 = np.random.normal(0, 1, size=50)
        data2 = np.random.normal(2, 1, size=50)

        data = pd.DataFrame({"d1": data1, "d2": data2})

        df = Data(data)

        df.paired_ttest("d1", "d2")

        self.assertTrue(True)

    def test_2s_indttest(self):

        data1 = np.random.normal(0, 1, size=50)
        data2 = np.random.normal(2, 1, size=50)

        data = pd.DataFrame({"d1": data1, "d2": data2})

        df = Data(data)

        df.ind_ttest("d1", "d2")

        self.assertTrue(True)

    def test_1s_indttest(self):

        data1 = np.random.normal(0, 1, size=50)
        data2 = np.random.normal(2, 1, size=50)

        data = pd.DataFrame({"d1": data1, "d2": data2})

        df = Data(data)

        df.onesample_ttest("d1", 1.0)

        self.assertTrue(True)
