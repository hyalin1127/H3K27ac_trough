Identifying trough regions from H3K27ac bigwig file
====================================================================================
This script aims to identify trough regions within H3K27ac peak reagions. Trough regions are more likely to be bound by transcriptional factors. Motif analysis of trough regions may help identify the master regulators that shape the epigentic landscape.

# Prerequisites #
The input of the H3K27ac trough identification workflow include 1) H3K27ac bigwig file 2) H3K27ac peak file in bed format


# Arguments #
```
optional arguments:
  -h, --help            show this help message and exit

Required arguments:

  -f H3K27AC_BIGWIG_FILE, --file=H3K27AC_BIGWIG_FILE
                        Name of H3K27ac bigwig file
  -p H3K27AC_PEAK_FILE, --peaks=H3K27AC_PEAK_FILE
                        Name of H3K27ac peaks file

Optional arguments for input and output:

  -n OUTPUT_TROUGH_NUMBER, --number=OUTPUT_TROUGH_NUMBER
                        Number of output trough, Default = 5,000
```
 
# Demonstration #

```
h3k27ac_trough -f "H3K27ac_bigwig_file_name" -p "H3K27ac_peaks_file_name"
```
# Contact #
Chen-Hao Chen (chen-hao_chen@dfci.harvard.edu)
