# [optcutfreq](https://pypi.org/project/optcutfreq)

[![PyPI version](https://badge.fury.io/py/optcutfreq.svg)](https://badge.fury.io/py/optcutfreq)
[![DOI](https://zenodo.org/badge/250840016.svg)](https://zenodo.org/badge/latestdoi/250840016)

Automatic search of optimal filter cutoff frequency based on residual analysis

The 'optimal' cutoff frequency (in the sense that a filter with such cutoff frequency removes as much noise as possible without considerably affecting the signal) is found by performing a residual analysis of the difference between filtered and unfiltered signals over a range of cutoff frequencies.  
The optimal cutoff frequency is the one where the residual starts to change very little because it is considered that from this point, it's being filtered mostly noise and minimally signal, ideally.

## Installation

```bash
pip install optcutfreq
```

The plots (parameter `show=True`) require matplotlib, which can be installed together with:

```bash
pip install "optcutfreq[plot]"
```

Or

```bash
conda install -c duartexyz optcutfreq
```

## Examples

```python
>>> import numpy as np
>>> from optcutfreq import optcutfreq
>>> y = np.cumsum(np.random.randn(1000))
>>> # optimal cutoff frequency based on residual analysis and plot:
>>> fc_opt = optcutfreq(y, freq=1000, show=True)

>>> # sane analysis but specifying the frequency limits and plot:
>>> optcutfreq(y, freq=1000, fclim=[200,400], show=True)

>>> # It's not always possible to find an optimal cutoff frequency
>>> # or the one found can be wrong (run this example many times):
>>> y = np.random.randn(100)
>>> optcutfreq(y, freq=100, show=True)
```

More examples, with Winter's benchmark data, are in a [marimo](https://marimo.io) notebook in the [docs](https://github.com/demotu/optcutfreq/tree/master/docs) directory. Run it in your browser, no installation needed:

| Notebook | molab | marimo.app |
|---|---|---|
| [optcutfreq](https://molab.marimo.io/github/demotu/optcutfreq/blob/master/docs/optcutfreq_notebook.py) | [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/demotu/optcutfreq/blob/master/docs/optcutfreq_notebook.py/wasm) | [![Open with marimo](https://marimo.io/shield.svg)](https://marimo.app/github.com/demotu/optcutfreq/blob/master/docs/optcutfreq_notebook.py) |

The notebook name links to a static preview with the outputs; the badges run the notebook in your browser with [WebAssembly](https://docs.marimo.io/guides/wasm/).

Or run it locally:

```bash
uvx marimo edit --sandbox docs/optcutfreq_notebook.py
```

## How to cite this work

Here is a suggestion to cite this GitHub repository:

> Marcos Duarte. (2021). optcutfreq: A Python module for automatic search of optimal filter cutoff frequency based on residual analysis (Version v0.0.8). Zenodo. http://doi.org/10.5281/zenodo.4599114

And a possible BibTeX entry:

```tex
@software{marcos_duarte_2021_4599114,
  author       = {Marcos Duarte},
  title        = {{optcutfreq: A Python module for automatic search of optimal filter cutoff frequency based on residual analysis}},
  month        = mar,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {v0.0.8},
  doi          = {10.5281/zenodo.4599114},
  url          = {https://doi.org/10.5281/zenodo.4599114}
}
```

## License

The non-software content of this project is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/), and the software code is licensed under the [MIT license](https://opensource.org/licenses/mit-license.php).
