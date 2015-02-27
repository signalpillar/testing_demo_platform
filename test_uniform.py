# std
import collections
import random


def get_bucket_num(bucketnum, start, stop, value):
    for i in xrange(bucketnum):
        low_bound = (i*(float(stop-start)/bucketnum)) + start
        high_bound = ((i+1)*(float(stop-start)/bucketnum)) + start
        # if low_bound < value < high_bound:
        if (value > low_bound) and (value < high_bound):
            return i


def test_random_uniform():
    """Ensure .... ?"""

    # given
    start = 0
    stop = 1
    partitions = 20
    iterations = 10000

    expected_density = 1./partitions

    # exercise
    counter = collections.Counter((
        get_bucket_num(partitions, start, stop, random.uniform(start, stop))
        for i in xrange(iterations)
    ))

    # verify
    for bucket_idx, counts in counter.viewitems():
        density = float(counts)/iterations
        if abs(density - expected_density) > expected_density/10:
            raise AssertionError(
                "Strange Densityfor {!r} with density {!r}. Counter: {!r}"
                .format(bucket_idx, density, counts))
