# -*- coding: utf-8 -*-
""" 
Ensemble of functions to load and preprocess audio signals.
"""

from .sound import (load,
                    envelope,
                    intoOctave,
                    audio_SNR,
                    spectral_SNR,
                    select_bandwidth,
                    fir_filter,
                    spectrogram,
                    avg_power_spectro,
                    avg_amplitude_spectro)

__all__ = ['load',
           'envelope',
           'intoOctave',
           'audio_SNR',
           'spectral_SNR',
           'select_bandwidth',
           'fir_filter',
           'spectrogram',
           'avg_power_spectro',
           'avg_amplitude_spectro']
