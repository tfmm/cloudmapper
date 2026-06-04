import unittest
from .nose_compat import assert_equal, assert_true, assert_false
from shared import pyjq_compat as pyjq


class TestPyjqCompat(unittest.TestCase):
    def test_all(self):
        res = pyjq.all(".[]", [1, 2, 3])
        assert_equal(res, [1, 2, 3])

        # Test safe handling of iteration over null/empty dict
        res_null = pyjq.all(".AvailabilityZones[]", {})
        assert_equal(res_null, [])

    def test_first(self):
        res = pyjq.first(".[]", [1, 2, 3])
        assert_equal(res, 1)

        res_none = pyjq.first(".[5]?", [1, 2, 3])
        assert_equal(res_none, None)

        res_fallback = pyjq.first(".[] | select(. == 4)", [1, 2, 3], "fallback")
        assert_equal(res_fallback, "fallback")

        # Test safe handling of first on null iteration
        res_null_fallback = pyjq.first(".AvailabilityZones[]", {}, "fallback")
        assert_equal(res_null_fallback, "fallback")

    def test_one(self):
        res = pyjq.one(".[0]", [10, 20])
        assert_equal(res, 10)

        with self.assertRaises(ValueError):
            pyjq.one(".[] | select(. == 4)", [1, 2, 3])

        with self.assertRaises(ValueError):
            pyjq.one(".[]", [1, 2, 3])

        # Test safe handling of one on null iteration
        with self.assertRaises(ValueError):
            pyjq.one(".AvailabilityZones[]", {})
