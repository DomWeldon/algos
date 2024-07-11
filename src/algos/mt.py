"""Mersenne Twister random number generator."""

import collections
import os
import typing


def _a(x: int) -> int:
    return x >> 1 if x < 2**31 else (x >> 1) ^ 0x9908B0DF


def randint32(
    seed: typing.Iterable[int] | None = None,
) -> typing.Generator[int, None, None]:
    """Yield random 32-bit integers using a basic implementation of the MT."""
    # generate the seed using urandom unless otherwise specified
    if seed is None:
        seed = (int.from_bytes(os.urandom(4)) for _ in range(624))

    state = collections.deque(seed, maxlen=624)

    # begin yielding random numbers
    while True:
        sk, sk1, sk397 = state[0], state[1], state[397]
        # twist
        m = (sk & 0x80000000) | (sk1 & 0x7FFFFFFF)
        sk624 = sk397 ^ _a(m)

        yield state.popleft()

        state.append(sk624)
