# wavelet_filters
Over 100 (decomposition level 1) wavelet (high pass) and scaling (low pass) filters packaged into user-friendly python dictionaries and R lists.

## For Python users

See `wavelet_dict.pkl` for 128 wavelet filters stored in a Python dictionary.
See `scaling_dict.pkl` for 128 scaling filters stored in a Python dictionary.

I've also incuded a `.py` file called `load_pickle.py` which is a convenience function to load
the dictionaries stored in `wavelet_dict.pkl` and `scaling_dict.pkl`. Here's an example:

``` python
from load_pickle import load_pickle

scaling_dict = load_pickle("scaling_dict.pkl")
wavelet_dict = load_pickle("wavelet_dict.pkl")
```

## For R users

See `wavelet_list.RData` for 128 wavelet filters stored in an R list.
See `scaling_list.RData` for 128 scaling filters stored in an R list.

## Available filters
The following are short names for the available filters:

``` python
['bl7', 'bl9', 'bl10', 
'beyl', 
'coif1', 'coif2', 'coif3', 'coif4', 'coif5', 
'db1', 'db2', 'db3', 'db4', 'db5', 'db6', 'db7', 'db8', 'db9', 'db10', 'db11', 'db12', 
'db13', 'db14', 'db15', 'db16', 'db17', 'db18', 'db19', 'db20', 'db21', 'db22', 'db23', 
'db24', 'db25', 'db26', 'db27', 'db28', 'db29', 'db30', 'db31', 'db32', 'db33', 
'db34', 'db35', 'db36', 'db37', 'db38', 'db39', 'db40', 'db41', 'db42', 'db43', 'db44', 'db45', 
'fk4', 'fk6', 'fk8', 'fk14', 'fk18', 'fk22', 
'han2_3', 'han3_3', 'han4_5', 'han5_5', 
'dmey', 
'mb4_2', 'mb8_2', 'mb8_3', 'mb8_4', 'mb10_3', 'mb12_3', 'mb14_3', 'mb16_3', 'mb18_3', 'mb24_3', 'mb32_3', 
'sym2', 'sym3', 'sym4', 'sym5', 'sym6', 'sym7', 'sym8', 'sym9', 'sym10', 'sym11', 'sym12', 'sym13', 'sym14', 
'sym15', 'sym16', 'sym17', 'sym18', 'sym19', 'sym20', 'sym21', 'sym22', 'sym23', 'sym24', 'sym25', 'sym26', 'sym27', 
'sym28', 'sym29', 'sym30', 'sym31', 'sym32', 'sym33', 'sym34', 'sym35', 'sym36', 'sym37', 'sym38', 'sym39', 'sym40', 
'sym41', 'sym42', 'sym43', 'sym44', 'sym45', 
'vaid', 
'la8', 'la10', 'la12', 'la14', 'la16', 'la18', 'la20']
```
where

- `bl` corresponds to "Best-localized Daubechies"
- `beyl` corresponds to "Beylkin"
- `coif` corresponds to "Coiflets"
- `db` corresponds to "Daubechies"
- `fk` corresponds to "Fejér-Korovkin"
- `han` corresponds to "Han linear-phase moments"
- `mb` corresponds to "Morris minimum-bandwidth"
- `sym` corresponds to "Symlets"
- `vaid` corresponds to "Vaidyanathan"
- `la` corresponds to "Least asymmetric"

NOTE: The `db1` is the Haar wavelet.

## Source of data

The `wfilters` function from MATALB R2022b's wavelet toolbox provided 121 of the 128 wavelet (scaling) filters available 
in `wavelet_dict.pkl`/`wavelet_list.RData` (`scaling_dict.pkl`/`scaling_list.RData`). The R package `wavelets` provided the remaining 7 least asymmetric
wavelet (scaling) filters. In total, there are 128 wavelet (scaling) filters available to both Python and R users.

## References

[1] Daubechies, Ingrid. Ten Lectures on Wavelets. Society for Industrial and Applied Mathematics, 1992.

[2] Morris, Joel M, and Ravindra Peravali. “Minimum-Bandwidth Discrete-Time Wavelets.” Signal Processing 76, no. 2 (July 1999): 181–93. https://doi.org/10.1016/S0165-1684(99)00007-9.

[3] Doroslovački, M.L. “On the Least Asymmetric Wavelets.” IEEE Transactions on Signal Processing 46, no. 4 (April 1998): 1125–30. https://doi.org/10.1109/78.668562.

[4] Han, Bin. “Wavelet Filter Banks.” In Framelets and Wavelets: Algorithms, Analysis, and Applications, 92–98. Applied and Numerical Harmonic Analysis. Cham, Switzerland: Birkhäuser, 2017. https://doi.org/10.1007/978-3-319-68530-4_2.
