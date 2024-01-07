#!/usr/bin/python

import argparse
import logging
import sys

import numpy as np

import gym
from gym import wrappers


class CartPole:
    def __init__(self, env_id, render=False, load_model=False, model_name=None):
        self.env = gym.make(env_id)
        self.outdir = '/tmp/' + 'qagent' + '-results'
        self.env = wrappers.Monitor(self.env, self.outdir, write_upon_reset=True, force=True)
        self.env.seed(0)

        self.Q = np.zeros([162, self.env.action_space.n])

        self.alpha = 0.7
        self.gamma = 0.97

    def discretize_state(self, x, xdot, theta, thetadot):
        one_degree = 0.0174532
        six_degrees = 0.1047192
        twelve_degrees = 0.2094384
        fifty_degrees = 0.87266

        box = 0
        if x < -2.4 or x > 2.4 or theta < -twelve_degrees or theta > twelve_degrees:
            return -1

        if x < -0.08:
            box = 0
        elif x < 0.08:
            box = 1
        else:
            box = 2

        box *= 3
        if xdot < -0.5:
            box += 0
        elif xdot < 0.5:
            box += 1
        else:
            box += 2

        box *= 6
        if theta < -six_degrees:
            box += 0
        if theta < -one_degree:
            box += 1
        elif theta < 0:
            box += 2
        elif theta < one_degree:
            box += 3
        elif theta < six_degrees:
            box += 4
        else:
            box += 5

        box *= 3
        if thetadot < -fifty_degrees:
            box += 0
        elif thetadot < fifty_degrees:
            box += 1
        else:
            box += 2

        return box

    def train(self, n_episodes=50001):
        for episode in range(n_episodes):
            tick = 0
            reward = 0
            done = False
            state = self.env.reset()
            s = self.discretize_state(state[0], state[1], state[2], state[3])
            while not done:
                tick += 1
                action = 0
                ri = -999
                for q in range(self.env.action_space.n):
                    if self.Q[s][q] > ri:
                        action = q
                        ri = self.Q[s][q]
                state, reward, done, _ = self.env.step(action)
                sprime = self.discretize_state(state[0], state[1], state[2], state[3])
                predicted_value = np.max(self.Q[sprime])
                if sprime < 0:
                    predicted_value = 0
                    reward = -5
                self.Q[s, action] += self.alpha * (reward + self.gamma * predicted_value - self.Q[s, action])
                s = sprime

            if episode % 1000 == 0:
                self.alpha *= 0.99  # decay rate for alpha, each 1000

    def close_env(self):
        self.env.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('env_id', nargs='?', default='CartPole-v0', help='Select the environment to run')
    args = parser.parse_args()

    logger = logging.getLogger()
    formatter = logging.Formatter('[%(asctime)s] %(message)s')
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    cartpole = CartPole(args.env_id)
    cartpole.train()
    cartpole.close_env()
