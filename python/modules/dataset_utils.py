#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-10-09 12:35:57
# @Author  : gammatone (adrien.bardet@live.fr)
# @Link    : https://github.com/gammatone/tensorflow-music-experiments
# @Version : $Id$
"""
dataset_utils.py
Module gathering useful functions for dataset handling.
"""

import os

import pickle

# Custom imports
from dsp_utils import librosa_load_wav


def create_pkl_audio_dataset(load_dir, dest_dir, dest_filename, keynames=[], sr=44100):
    """
    Load all the .wav files specified by keynames located in load_dir.
    Store all the arrays in a dictionary and save it in .pkl file in dest dir.
    """
    pkl_dict = {}
    for file in os.listdir(load_dir):
        if file.endswith(".wav"):
            for keyname in keynames:
                if file.startswith(keyname):
                    array, _ = librosa_load_wav(os.path.join(load_dir, file), sr=sr)
                    break
            pkl_dict[keyname] = array
    # Make sure dest_dir exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    # Save dict
    with open(os.path.join(dest_dir, dest_filename), 'wb') as f:
        pickle.dump(pkl_dict, f)

def get_dict_from_pkl(pkl_path):
    """
    Load array dictionary from pickle file
    """
    with open(pkl_path, 'rb') as f:
        loaded_dict = pickle.load(f)
    return loaded_dict 
