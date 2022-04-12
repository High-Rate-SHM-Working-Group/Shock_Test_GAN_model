""" Script for generating data. Thompson 2022"""
from constants import GENERATOR_NAME, LATENT_DIM
from tensorflow import keras


def random_labels(num_signals: int):
    """ Generates and returns number of random labels."""


def generate_data(num_signals: int, generator, labels=None):
    fn_labels = labels if labels is not None and len(labels) == num_signals else random_labels(num_signals)
    return generator.predict()


def main():
    pass


if __name__ == '__main__':
    main()