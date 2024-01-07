#!/usr/bin/env python3
from testprog import CartPole
import unittest
import numpy as np


class TestCartPole(unittest.TestCase):

    def test_1(self):
        env_id = 'CartPole-v1'
        cartpole = CartPole(env_id, False, True, 'cart.npy')
        cartpole.train()  # Assuming you have a train method in your CartPole class
        all_states = []  # Replace this with the appropriate method to get states
        max_ = np.max(all_states, axis=0)
        print("max = {}".format(max_))
        result_1 = max_[0] <= 2.4
        result_2 = max_[2] <= 0.226893
        result = result_1 and result_2
        print("Your max cart position = {}".format(max_[0]))
        print("Your max pole angle = {}".format(max_[2]))
        print("Cart position for success <= {}".format(2.4))
        print("Pole angle for success <= {} radians".format(0.226893))

        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
