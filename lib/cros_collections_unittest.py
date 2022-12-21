# Copyright 2018 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Test the cros_collections module."""

import collections

from chromite.lib import cros_collections
from chromite.lib import cros_test_lib


class TestGroupByKey(cros_test_lib.TestCase):
    """Test SplitByKey."""

    def testEmpty(self):
        self.assertEqual({}, cros_collections.GroupByKey([], ""))

    def testGroupByKey(self):
        input_iter = [
            {"a": None, "b": 0},
            {"a": 1, "b": 1},
            {"a": 2, "b": 2},
            {"a": 1, "b": 3},
        ]
        expected_result = {
            None: [{"a": None, "b": 0}],
            1: [{"a": 1, "b": 1}, {"a": 1, "b": 3}],
            2: [{"a": 2, "b": 2}],
        }
        self.assertEqual(
            cros_collections.GroupByKey(input_iter, "a"), expected_result
        )


class GroupNamedtuplesByKeyTests(cros_test_lib.TestCase):
    """Tests for GroupNamedtuplesByKey"""

    def testGroupNamedtuplesByKeyWithEmptyInputIter(self):
        """Test GroupNamedtuplesByKey with empty input_iter."""
        self.assertEqual({}, cros_collections.GroupByKey([], ""))

    def testGroupNamedtuplesByKey(self):
        """Test GroupNamedtuplesByKey."""
        TestTuple = collections.namedtuple("TestTuple", ("key1", "key2"))
        r1 = TestTuple("t1", "val1")
        r2 = TestTuple("t2", "val2")
        r3 = TestTuple("t2", "val2")
        r4 = TestTuple("t3", "val3")
        r5 = TestTuple("t3", "val3")
        r6 = TestTuple("t3", "val3")
        input_iter = [r1, r2, r3, r4, r5, r6]

        expected_result = {"t1": [r1], "t2": [r2, r3], "t3": [r4, r5, r6]}
        self.assertDictEqual(
            cros_collections.GroupNamedtuplesByKey(input_iter, "key1"),
            expected_result,
        )

        expected_result = {"val1": [r1], "val2": [r2, r3], "val3": [r4, r5, r6]}
        self.assertDictEqual(
            cros_collections.GroupNamedtuplesByKey(input_iter, "key2"),
            expected_result,
        )

        expected_result = {None: [r1, r2, r3, r4, r5, r6]}
        self.assertDictEqual(
            cros_collections.GroupNamedtuplesByKey(input_iter, "test"),
            expected_result,
        )


class InvertDictionayTests(cros_test_lib.TestCase):
    """Tests for InvertDictionary."""

    def testInvertDictionary(self):
        """Test InvertDictionary."""
        changes = ["change_1", "change_2", "change_3", "change_4"]
        children = ["child_1", "child_2", "child_3", "child_4"]
        child_changes_dict = {
            children[0]: set(changes[0:1]),
            children[1]: set(changes[0:2]),
            children[2]: set(changes[2:4]),
            children[3]: set(),
        }
        change_children_dict = cros_collections.InvertDictionary(
            child_changes_dict
        )

        expected_dict = {
            changes[0]: set(children[0:2]),
            changes[1]: set([children[1]]),
            changes[2]: set([children[2]]),
            changes[3]: set([children[2]]),
        }
        self.assertDictEqual(change_children_dict, expected_dict)
