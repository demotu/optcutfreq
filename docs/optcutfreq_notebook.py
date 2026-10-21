# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "marimo",
#     "matplotlib",
#     "numpy",
#     "optcutfreq",
#     "pandas",
#     "pyversions",
#     "scipy",
# ]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # [optcutfreq](https://pypi.org/project/optcutfreq)

    A Python module for automatic search of optimal filter cutoff frequency based on residual analysis

    [https://pypi.org/project/optcutfreq](https://pypi.org/project/optcutfreq)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Determination of the optimal cutoff frequency for a low-pass filter

    A common problem in signal processing is to automatically determine the optimal cutoff frequency that should be employed in a low-pass filter to attenuate as much as possible the noise without compromising the signal content of the data.

    Unfortunately, there is no definite solution for this problem, but there are some techniques, with different degrees of success, to try to determine the optimal cutoff frequency.

    David Winter, in his classic book *Biomechanics and motor control of human movement*, proposed a method to find the optimal cutoff frequency based on residual analysis of the difference between filtered and unfiltered signals over a range of cutoff frequencies. The optimal cutoff frequency is the one where the residual starts to change very little because it is considered that from this point, it's being filtered mostly noise and minimally signal, ideally. This concept is straightforward to implement.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The function `optcutfreq.py`

    The function `optcutfreq.py` ([source code](https://github.com/demotu/optcutfreq/blob/master/optcutfreq/optcutfreq.py)) of the Python module `optcutfreq` contains an implementation of this method and it is divided in three parts (after the help section): first, the residuals over a range of cutoff frequencies are calculated; second, an algorithm tries to find the noisy region (with a supposed linear behavior in the frequency domain) of the residuals versus cutoff frequencies plot and finds the optimal cutoff frequency; and third, the results are plotted. The code is lengthy relatively to the simplicity of the idea because of the long help section, the implementation of the automatic search and a rich plot. Here is the function signature:

    ```python
    fc_opt = optcutfreq(y, freq=1, fclim=None, show=False, ax=None)
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Installation

    ```bash
    pip install "optcutfreq[plot]"
    ```

    Or

    ```bash
    conda install -c duartexyz optcutfreq
    ```

    To run this [marimo](https://marimo.io) notebook in an isolated environment with all its dependencies:

    ```bash
    uvx marimo edit --sandbox optcutfreq_notebook.py
    ```
    """)
    return


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from scipy.signal import butter, filtfilt
    import pyversions

    from optcutfreq import optcutfreq

    return butter, filtfilt, mo, np, optcutfreq, pd, plt, pyversions


@app.cell
def _(pyversions):
    _info = pyversions.versions()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Test with benchmark data
    Let's test this function with benchmark data.

    In 1977, Pezzack, Norman and Winter published a paper where they investigated the effects of differentiation and filtering processes on experimental data (the angle of a bar manipulated in space). Since then, these data have became a benchmark to test new algorithms. Let's work with these data (available at [http://isbweb.org/data/pezzack/index.html](http://isbweb.org/data/pezzack/index.html)). The data have the angular displacement measured by video and the angular acceleration directly measured by an accelerometer, which we will consider as the true acceleration.
    Part of these data are showing next:
    """)
    return


@app.cell
def _(mo, np, pd):
    # the data file is next to this notebook; in the browser, read it from GitHub
    _url = 'https://raw.githubusercontent.com/demotu/optcutfreq/master/docs/pezzack.txt'
    try:
        _path = mo.notebook_location() / 'pezzack.txt'
        _source = _path if _path.is_file() else _url
    except (AttributeError, TypeError):  # in the browser, the location is a URL
        _source = _url
    _data = pd.read_csv(_source, sep='\t', header=None, skiprows=6).to_numpy()
    time, disp, disp2, aacc = _data.T
    freq = np.mean(1/np.diff(time))
    return aacc, disp, freq, time


@app.cell
def _(aacc, disp, plt, time):
    _fig, (_ax1, _ax2) = plt.subplots(1, 2, sharex=True, figsize=(11, 4))
    _fig.suptitle("Pezzack's benchmark data", fontsize=20)
    _ax1.plot(time, disp, 'b')
    _ax1.set_xlabel('Time [s]')
    _ax1.set_ylabel('Angular displacement [rad]')
    _ax2.plot(time, aacc, 'g')
    _ax2.set_xlabel('Time [s]')
    _ax2.set_ylabel('Angular acceleration [rad/s$^2$]')
    _fig.subplots_adjust(wspace=0.3)
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And using the residual analysis code:
    """)
    return


@app.cell
def _(disp, freq, optcutfreq):
    fc_opt = optcutfreq(disp, freq=freq, show=True)
    return (fc_opt,)


@app.cell(hide_code=True)
def _(fc_opt, mo):
    mo.md(rf"""
    The optimal cutoff frequency found is {fc_opt:.1f} Hz. Note that the filtering process is relevant only for the derivative of the data; we cannot distinguish the unfiltered and filtered displacements (see that the RMSE residual is very small).
    Let's employ this filter, differentiate the data twice and compare with the true acceleration:
    """)
    return


@app.cell
def _(aacc, butter, disp, fc_opt, filtfilt, freq, np, plt, time):
    # Butterworth filter
    # Correct the cutoff frequency for the number of passes in the filter
    C = 0.802  # for dual pass; C = (2**(1/npasses) - 1)**0.25
    _b, _a = butter(2, (fc_opt/C)/(freq/2))
    _dispf = filtfilt(_b, _a, disp)
    _aaccBW = np.diff(_dispf, 2)*freq*freq
    # RMSE:
    _rmseBW = np.sqrt(np.mean((_aaccBW - aacc[1:-1])**2))
    # plot data
    _fig, _ax1 = plt.subplots(1, 1, figsize=(11, 4))
    _fig.suptitle("Pezzack's benchmark data", fontsize=20)
    _ax1.plot(time[1:-1], aacc[1:-1], 'g', label='Analog acceleration:     (True value)')
    _ax1.plot(time[1:-1], _aaccBW, 'r',
              label='Butterworth %.3g Hz:     RMSE = %0.2f' % (fc_opt, _rmseBW))
    _ax1.set_xlabel('Time [s]')
    _ax1.set_ylabel('Angular acceleration [rad/s$^2$]')
    _ax1.legend(frameon=False, fontsize=12, loc='upper left')
    _fig
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The performance seems satisfactory (see [this Jupyter notebook](https://nbviewer.jupyter.org/github/BMClab/BMC/blob/master/notebooks/DataFiltering.ipynb) for a comparison using other filters), but it is known that this residual analysis algorithm results in oversmoothing the kinematic data (see [http://www.clinicalgaitanalysis.com/faq/cutoff.html](http://www.clinicalgaitanalysis.com/faq/cutoff.html)).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Interactive example

    If the automatic search fails or you disagree with the noisy region of the residuals it found, choose the limit frequencies of the noisy part of the residuals curve (`fclim`):
    """)
    return


@app.cell
def _(freq, mo):
    automatic = mo.ui.checkbox(value=False, label='automatic search')
    fclim = mo.ui.range_slider(0, round(0.8*freq/2, 1), step=0.1, value=[8, 18],
                               label='fclim [Hz]', show_value=True, full_width=True)
    mo.vstack([automatic, fclim])
    return automatic, fclim


@app.cell
def _(automatic, disp, fclim, freq, mo, optcutfreq):
    _fc = optcutfreq(disp, freq=freq, fclim=None if automatic.value else fclim.value,
                     show=True)
    mo.md('Optimal cutoff frequency: **%s**' % ('%.2f Hz' % _fc if _fc else 'not found'))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To read more about the determination of the optimal cutoff frequency, see the following papers:

    - Pezzack, Norman, & Winter (1977). [An assessment of derivative determining techniques used for motion analysis](https://doi.org/10.1016/0021-9290(77)90010-0). Journal of Biomechanics, 10, 377-382.
    - Giakas & Baltzopoulos (1997) [A comparison of automatic filtering techniques applied to biomechanical walking data](https://doi.org/10.1016/S0021-9290(97)00042-0). J. Biomech. 30, 847-850.
    - Alonso, Salgado, Cuadrado & Pintado (2009) [Automatic smoothing of raw kinematic signals using SSA and cluster analysis](http://lim.ii.udc.es/docs/proceedings/2009_09_EUROMECH_Automatic.pdf). 7th EUROMECH Solid Mechanics Conference.
    - Kristianslund, Krosshaug & van den Bogert (2012) [Effect of low pass filtering on joint moments from inverse dynamics: Implications for injury prevention](https://doi.org/10.1016/j.jbiomech.2011.12.011). J. Biomech. 45, 666-671.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## References

    - Pezzack JC, Norman RW, & Winter DA (1977). [An assessment of derivative determining techniques used for motion analysis](https://doi.org/10.1016/0021-9290(77)90010-0). Journal of Biomechanics, 10, 377-382. [PubMed](https://pubmed.ncbi.nlm.nih.gov/893476/).
    - Winter DA (2009) [Biomechanics and motor control of human movement](http://books.google.com.br/books?id=_bFHL08IWfwC&printsec=frontcover&source=gbs_ge_summary_r&cad=0#v=onepage&q&f=false). 4 ed. Hoboken, EUA: Wiley.
    """)
    return


if __name__ == "__main__":
    app.run()
