#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for alpha acoustic indices

"""

import os
import pytest
import maad
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal
from pathlib import Path

#%% Temporal indices

def test_temporal_median():
    # Compute temporal median
    s, fs = maad.sound.load(Path('./data/spinetail.wav'))
    temporal_median_index = maad.features.temporal_median(s)

    # Load expected values
    expected_values = 0.007934564717486147

    assert np.allclose(temporal_median_index, expected_values)

def test_temporal_entropy():
    # Compute temporal median
    s, fs = maad.sound.load(Path('./data/spinetail.wav'))
    temporal_entropy_index = maad.features.temporal_entropy(s)

    # Load expected values
    expected_values = 0.7518917279549968

    assert np.allclose(temporal_entropy_index, expected_values)

def test_temporal_activity():
    # Compute temporal median
    s, fs = maad.sound.load(Path('./data/spinetail.wav'))
    temporal_activity_index = maad.features.temporal_activity(s, dB_threshold=6)

    # Load expected values
    expected_values = (0.36838978015448604, 620, 24.41347313621499)

    assert np.allclose(temporal_activity_index, expected_values)


#%% Spectral indices

def test_spectral_entropy():
    # Compute spectral entropy
    s, fs = maad.sound.load(Path('./data/cold_forest_daylight.wav'))
    Sxx_power, tn, fn, _ = maad.sound.spectrogram (s, fs)
    spectral_entropy_indices = maad.features.spectral_entropy(
        Sxx_power, fn, flim=(2000,10000))

    # Load expected values
    # expected_values = (0.26807540760637083,
    #                    0.4883515296525619,
    #                    0.24146196318401636,
    #                    1,
    #                    17.580495975968567,
    #                    3.5452699010615505)
    expected_values = (0.26807540760637083,
                       0.488351529652562,
                       0.24146196318401625,
                       0.2536420606912331,
                       17.580495975968567,
                       3.5452699010615505)

    assert np.allclose(spectral_entropy_indices,expected_values)


#%% Spectro-temporal indices

#%% Sepectral-temporal features

def test_spectra_features():
    s, fs = maad.sound.load(Path('./data/spinetail.wav'))

    spectral_features = maad.features.all_spectral_features(s, fs)

    expected_values = pd.DataFrame({"sm":2.2763302268911505e-06,
                                    "sv":8.11804174130019e-11,
                                    "ss":5.8446635093417045,
                                    "sk":40.488906373539436,
                                    "Freq 5%":6029.296875,
                                    "Freq 25%":6416.89453125,
                                    "Freq 50%":6632.2265625,
                                    "Freq 75%":6890.625,
                                    "Freq 95%":9216.2109375,
                                    "peak_freq":6632.2265625,
                                    "Time 5%":1.2190476190476192,
                                    "Time 25%":5.712108843537415,
                                    "Time 50%":11.818956916099774,
                                    "Time 75%":16.555827664399093,
                                    "Time 95%":17.751655328798186,
                                    "bandwidth_50":473.73046875,
                                    "bandwidth_90":3186.9140625,
                                    "bandwidth_3dB":320.8791300822477}, index=[0])

    assert_frame_equal(spectral_features, expected_values)

def test_temporal_features():
    s, fs = maad.sound.load(Path('./data/spinetail.wav'))

    temporal_features = maad.features.all_temporal_features(s, fs)

    expected_values = pd.DataFrame({"sm":-2.043264e-19,
                                    "sv":0.0011670735714956646,
                                    "ss":-0.006548,
                                    "sk":24.711611,
                                    "Time 5%":1.215429,
                                    "Time 25%":5.707076,
                                    "Time 50%":11.816876,
                                    "Time 75%":16.356414,
                                    "Time 95%":17.760507,
                                    "zcr":10500.397192,
                                    "duration_50":10.649338,
                                    "duration_90":16.545078}, index=[0])

    assert_frame_equal(temporal_features, expected_values)