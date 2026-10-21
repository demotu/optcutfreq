from pathlib import Path

import matplotlib
import numpy as np
import pytest

matplotlib.use("Agg")

import matplotlib.pyplot as plt

from optcutfreq import optcutfreq

DATA = Path(__file__).parents[1] / 'docs' / 'pezzack.txt'


def _random_walk(seed=0, n=1000):
    return np.cumsum(np.random.default_rng(seed).standard_normal(n))


def test_pezzack_benchmark():
    # Winter's benchmark: the notebook reports 5.6 Hz
    time, disp, _, _ = np.loadtxt(DATA, skiprows=6, unpack=True)
    fc_opt = optcutfreq(disp, freq=np.mean(1/np.diff(time)))
    assert fc_opt == pytest.approx(5.592, abs=0.01)


def test_automatic_search():
    assert optcutfreq(_random_walk(), freq=1000) == pytest.approx(82.29, abs=0.01)


def test_fclim_as_list_or_array():
    y = _random_walk()
    fc_list = optcutfreq(y, freq=1000, fclim=[100, 300])
    fc_array = optcutfreq(y, freq=1000, fclim=np.array([100, 300]))
    assert fc_list == pytest.approx(69.89, abs=0.01)
    assert fc_array == fc_list


def test_fclim_up_to_nyquist_frequency():
    # the residuals are computed up to 0.802 of the Nyquist frequency;
    # a larger upper limit uses the residuals up to there
    y = _random_walk()
    fc_opt = optcutfreq(y, freq=1000, fclim=[200, 500])
    assert fc_opt == optcutfreq(y, freq=1000, fclim=[200, 397])


def test_fclim_outside_range_uses_automatic_search():
    y = _random_walk()
    assert optcutfreq(y, freq=1000, fclim=[-1, 300]) == optcutfreq(y, freq=1000)
    assert optcutfreq(y, freq=1000, fclim=[100, 600]) == optcutfreq(y, freq=1000)


def test_not_found_returns_none_and_plots():
    # reversed limits: there is no noisy region to fit
    assert optcutfreq(_random_walk(), freq=1000, fclim=[300, 100], show=True) is None
    plt.close('all')


def test_plot_in_given_axes():
    fig = plt.figure()
    ax = np.array([fig.add_subplot(121), fig.add_subplot(222), fig.add_subplot(224)])
    fc_opt = optcutfreq(_random_walk(), freq=1000, show=True, ax=ax)
    assert ax[0].get_title() == 'Residual analysis'
    assert fc_opt == pytest.approx(82.29, abs=0.01)
    plt.close('all')


def test_plot_does_not_change_global_settings():
    before = dict(plt.rcParams)
    optcutfreq(_random_walk(), freq=1000, show=True)
    plt.close('all')
    changed = {k for k in before if plt.rcParams[k] != before[k]}
    assert not changed
