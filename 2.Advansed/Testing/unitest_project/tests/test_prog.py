import unittest
import prog


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ До начала тестирования """
        print(">>> Начало тестирования! <<<")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """ После всех тестов """
        print("\n==========")
        print(">>> Конец тестирования <<<")

    # def setUp(self):
    #     """ Для каждого теста """
    #     print(" !!! ")

    def test_main(self):
        # print("id: " + self.id()) # Отобразить id
        self.assertEqual(prog.main(), "ok")

    @unittest.skip("SKIP")
    def test_func1(self):
        # print("id: " + self.id())
        self.assertEqual(prog.func1(), "false")

    def test_summ(self):
        # print("id: " + self.id())
        self.assertEqual(prog.summ(2, 3), 5)


if __name__ == "__main__":
    unittest.main()

# Для условного пропуска тестов применяются следующие декораторы:
# @unittest.skipIf(condition, reason)
# Тест будет пропущен, если условие (condition) истинно.

# @unittest.skipUnless(condition, reason)
# Тест будет пропущен если, условие (condition) не истинно.
