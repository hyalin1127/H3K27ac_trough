Integrative CRISPR analysis using MAGeCK-NEST
====================================================================================
Model-based Analysis of Genome-wide CRISPR-Cas9 Knockout (MAGeCK_NEST) is a computational tool to identify important genes from the recent genome-scale CRISPR-Cas9 knockout screens technology. Based on the previous generation, MAGeCK_VISPR, MAGeCK_NEST includes some new features, including:
```
* Outliers removal.
* Protein-protein interaction information integration.
* QC:
  1. Histogram of beta scores (modified log fold changes)
  2. QQ-plot of z-statistics
  3. Gene set enrichment analysis (GSEA) using positive control genes as quality control.
  4. Correlation coefficients between interacting genes.
  5. QC report
```

# Prerequisites #
The input of the MAGeCK-NEST workflow are read count files. The formats are sgRNA, gene, readcounts
Ex: 
```
sgRNA         gene     sample1_readcount     sample2_readcount...
gene1_gRNA_1  gene1    557                   421
gene1_gRNA_2  gene1    295                   128
     .          .       .
     .          .       .
     .          .       .
gene2_gRNA_1  gene2    173                   68
gene2_gRNA_2  gene2    85                    38
     .          .       .
     .          .       .
     .          .       .
```
# Installation #

# Usage #

```
python3 mageck_nest.py nest [-h] -k COUNT_TABLE -d DESIGN_MATRIX
                           [-n OUTPUT_PREFIX] [-i INCLUDE_SAMPLES]
                           [-b BETA_LABELS]
                           [--norm-method {none,median,total,control}]
                           [-e NEGATIVE_CONTROL]
                           [--genes-varmodeling GENES_VARMODELING]
                           [--adjust-method {fdr,holm,pounds}] [-o] [-p] [-q]
```

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
                        Number of output trough
```
 
# Demonstration #

```
python3 pioneer_K27ac_motif_Daisy.py -f "H3K27ac_bigwig_file_name" -p "H3K27ac_peaks_file_name"
```
