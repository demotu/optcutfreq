# [optcutfreq](https://pypi.org/project/optcutfreq)

Automatic search of optimal filter cutoff frequency based on residual analysis

The 'optimal' cutoff frequency (in the sense that a filter with such cutoff frequency removes as much noise as possible without considerably affecting the signal) is found by performing a residual analysis of the difference between filtered and unfiltered signals over a range of cutoff frequencies.  
The optimal cutoff frequency is the one where the residual starts to change very little because it is considered that from this point, it's being filtered mostly noise and minimally signal, ideally.

## Installation

```bash
pip install optcutfreq
```

Or

```bash
conda install -c duartexyz optcutfreq
```

## Examples

```python
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

- [In a Jupyter notebook](https://github.com/demotu/optcutfreq/blob/master/docs/optcutfreq.ipynb)

## How to cite this work

Here is a suggestion to cite this GitHub repository:

> Duarte, M. (2020) optcutfreq: Automatic search of optimal filter cutoff frequency based on residual analysis. GitHub repository, <https://github.com/demotu/optcutfreq>.

And a possible BibTeX entry:

```tex
@misc{Duarte2020,  
    author = {Duarte, M.},
    title = {optcutfreq: Automatic search of optimal filter cutoff frequency based on residual analysis},  
    year = {2020},  
    publisher = {GitHub},  
    journal = {GitHub repository},  
    howpublished = {\url{https://github.com/demotu/optcutfreq}}  
}
```

## License

The non-software content of this project is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/), and the software code is licensed under the [MIT license](https://opensource.org/licenses/mit-license.php).
