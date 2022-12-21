# Copyright 2018 The ChromiumOS Authors
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Chromite extensions on top of the collections module."""


def GroupByKey(input_iter, key):
    """Split an iterable of dicts, based on value of a key.

    GroupByKey([{'a': 1}, {'a': 2}, {'a': 1, 'b': 2}], 'a') =>
      {1: [{'a': 1}, {'a': 1, 'b': 2}], 2: [{'a': 2}]}

    Args:
      input_iter: An iterable of dicts.
      key: A string specifying the key name to split by.

    Returns:
      A dictionary, mapping from each unique value for |key| that
      was encountered in |input_iter| to a list of entries that had
      that value.
    """
    split_dict = dict()
    for entry in input_iter:
        split_dict.setdefault(entry.get(key), []).append(entry)
    return split_dict


def GroupNamedtuplesByKey(input_iter, key):
    """Split an iterable of namedtuples, based on value of a key.

    Args:
      input_iter: An iterable of namedtuples.
      key: A string specifying the key name to split by.

    Returns:
      A dictionary, mapping from each unique value for |key| that
      was encountered in |input_iter| to a list of entries that had
      that value.
    """
    split_dict = {}
    for entry in input_iter:
        split_dict.setdefault(getattr(entry, key, None), []).append(entry)
    return split_dict


def InvertDictionary(origin_dict):
    """Invert the key value mapping in the origin_dict.

    Given an origin_dict {'key1': {'val1', 'val2'}, 'key2': {'val1', 'val3'},
    'key3': {'val3'}}, the returned inverted dict will be
    {'val1': {'key1', 'key2'}, 'val2': {'key1'}, 'val3': {'key2', 'key3'}}

    Args:
      origin_dict: A dict mapping each key to a group (collection) of values.

    Returns:
      An inverted dict mapping each key to a set of its values.
    """
    new_dict = {}
    for origin_key, origin_values in origin_dict.items():
        for origin_value in origin_values:
            new_dict.setdefault(origin_value, set()).add(origin_key)

    return new_dict
