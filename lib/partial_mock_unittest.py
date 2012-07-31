#!/usr/bin/python

# Copyright (c) 2012 The Chromium OS Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                '..', '..'))
from chromite.lib import cros_test_lib
from chromite.lib import partial_mock

# pylint: disable=W0212

class ComparatorTest(cros_test_lib.MoxTestCase):
  """Test Comparitor functionality."""
  TEST_KEY1 = 'monkey'
  TEST_KEY2 = 'foon'

  def testEquals(self):
    """__eq__, __ne__ functionality of Comparator classes."""
    for cls_name in ['In', 'Regex', 'ListRegex']:
      cls = getattr(partial_mock, cls_name)
      obj1 = cls(self.TEST_KEY1)
      obj2 = cls(self.TEST_KEY1)
      obj3 = cls(self.TEST_KEY2)
      self.assertEquals(obj1, obj2)
      self.assertFalse(obj1 == obj3)
      self.assertNotEquals(obj1, obj3)

  def testIgnoreEquals(self):
    """Verify __eq__ functionality for Ignore."""
    obj1 = partial_mock.Ignore()
    obj2 = partial_mock.Ignore()
    self.assertEquals(obj1, obj2)
    self.assertFalse(obj1 != obj2)

  def testListRegex(self):
    """Verify ListRegex match functionality."""
    obj = partial_mock.ListRegex('.*monkey.*')
    self.assertTrue(obj.Match(['the', 'small monkeys', 'jumped']))
    self.assertFalse(obj.Match(['the', 'jumped']))
    self.assertFalse(obj.Match(None))
    self.assertFalse(obj.Match(1))


class RecursiveCompareTest(cros_test_lib.MoxTestCase):
  """Test recursive compare functionality."""

  LHS_DICT = {3: 1, 1: 2}
  RHS_DICT = {1: 2, 3: 1}
  LIST = [1, 2, 3, 4]
  TUPLE = (1, 2, 3, 4)

  def TrueHelper(self, lhs, rhs):
    self.assertTrue(partial_mock._RecursiveCompare(lhs, rhs))

  def FalseHelper(self, lhs, rhs):
    self.assertFalse(partial_mock._RecursiveCompare(lhs, rhs))

  def testIt(self):
    """Test basic equality cases."""
    self.TrueHelper(self.LHS_DICT, self.RHS_DICT)
    self.TrueHelper({3: self.LIST, 1: self.LHS_DICT},
                    {1: self.LHS_DICT, 3: self.LIST})
    self.FalseHelper({1: self.LHS_DICT, 3: self.LIST},
                     {1: self.LHS_DICT, 3: self.LIST + [5]})
    self.FalseHelper(self.LIST, self.TUPLE)


class MockedCallResultsTest(cros_test_lib.MoxTestCase):
  """Test MockedCallResults functionality."""

  ARGS = ('abc',)
  LIST_ARGS = ([1, 2, 3, 4],)
  KWARGS = {'test': 'ing'}
  NEW_ENTRY = {'new': 'entry'}

  def KwargsHelper(self, result, kwargs, strict=True):
    self.mr.AddResultForParams(self.ARGS, result, kwargs=kwargs,
                               strict=strict)

  def setUp(self):
    self.mr = partial_mock.MockedCallResults('SomeFunction')

  def testNoMock(self):
    """The call is not mocked."""
    self.assertRaises(AssertionError, self.mr.LookupResult, self.ARGS)

  def testArgReplacement(self):
    """Replacing mocks for args-only calls."""
    self.mr.AddResultForParams(self.ARGS, 1)
    self.mr.AddResultForParams(self.ARGS, 2)
    self.assertEquals(2, self.mr.LookupResult(self.ARGS))

  def testKwargsStrictReplacement(self):
    """Replacing strict kwargs mock with another strict mock."""
    self.KwargsHelper(1, self.KWARGS)
    self.KwargsHelper(2, self.KWARGS)
    self.assertEquals(2, self.mr.LookupResult(self.ARGS, kwargs=self.KWARGS))

  def testKwargsNonStrictReplacement(self):
    """Replacing strict kwargs mock with nonstrict mock."""
    self.KwargsHelper(1, self.KWARGS)
    self.KwargsHelper(2, self.KWARGS, strict=False)
    self.assertEquals(2, self.mr.LookupResult(self.ARGS, kwargs=self.KWARGS))

  def testListArgLookup(self):
    """Matching of arguments containing lists."""
    self.mr.AddResultForParams(self.LIST_ARGS, 1)
    self.mr.AddResultForParams(self.ARGS, 1)
    self.assertEquals(1, self.mr.LookupResult(self.LIST_ARGS))

  def testKwargsStrictLookup(self):
    """Strict lookup fails due to extra kwarg."""
    self.KwargsHelper(1, self.KWARGS)
    kwargs = self.NEW_ENTRY
    kwargs.update(self.KWARGS)
    self.assertRaises(AssertionError, self.mr.LookupResult, self.ARGS,
                      kwargs=kwargs)

  def testKwargsNonStrictLookup(self):
    """"Nonstrict lookup passes with extra kwarg."""
    self.KwargsHelper(1, self.KWARGS, strict=False)
    kwargs = self.NEW_ENTRY
    kwargs.update(self.KWARGS)
    self.assertEquals(1, self.mr.LookupResult(self.ARGS, kwargs=kwargs))

  def testIgnoreMatching(self):
    """Deep matching of Ignore objects."""
    ignore = partial_mock.Ignore()
    self.mr.AddResultForParams((ignore, ignore), 1, kwargs={'test': ignore})
    self.assertEquals(
        1, self.mr.LookupResult(('some', 'values'), {'test': 'bla'}))

  def testRegexMatching(self):
    """Regex matching."""
    self.mr.AddResultForParams((partial_mock.Regex('pre.ix'),), 1)
    self.mr.AddResultForParams((partial_mock.Regex('suffi.'),), 2)
    self.assertEquals(1, self.mr.LookupResult(('prefix',)))
    self.assertEquals(2, self.mr.LookupResult(('suffix',)))

  def testMultipleMatches(self):
    """Lookup matches mutilple results."""
    self.mr.AddResultForParams((partial_mock.Ignore(),), 1)
    self.mr.AddResultForParams((partial_mock.In('test'),), 2)
    self.assertRaises(AssertionError, self.mr.LookupResult, ('test',))

  def testHook(self):
    """Return value of hook is used as the final result."""
    def hook(*args, **kwargs):
      self.assertEquals(args, hook_args)
      self.assertEquals(kwargs, hook_kwargs)
      return 2

    hook_args = self.LIST_ARGS
    hook_kwargs = self.KWARGS
    self.mr.AddResultForParams(self.ARGS, 1, side_effect=hook)
    self.assertEqual(
        2, self.mr.LookupResult(self.ARGS, hook_args=hook_args,
                                hook_kwargs=hook_kwargs))

if __name__ == '__main__':
  cros_test_lib.main()
