---
title: "HIPPIE2: Hi-C-based landscape of physically interacting regions and interaction mechanisms"
collection: posters
type: "Poster"
permalink: /posters/2018-10-20-ASHG_HIPPIE2
venue: "American Society of Human Genetics (ASHG) 2018"
date: 2018-10-20
location: "San Diego, California"
---

[Poster PDF](/files/18.10.20.AAW.HIPPIE2.pdf)

Pavel P. Kuksa, Alexandre Amlie-Wolf, Yih-Chii Hwang, Brian D. Gregory, Li-San Wang

Most regulatory chromatin interactions are mediated by various transcription factors (TFs) and involve physically-interacting regions (PIRs) that are regulatory elements such as enhancers, insulators, or promoters.

To map genome-wide human TF-mediated regulatory interactions such as enhancer-TF-gene promoter interactions across cell lines, we developed a novel approach, HiPPIE2. HiPPIE2 accepts raw Hi-C reads as input and provides extensive characterization of (1) PIRs and their potential regulatory roles using epigenomic annotations, (2) high-confidence PIR-PIR interactions, and (3) TF complexes mediating regulatory interactions based on binding motifs and ChIP-seq experiments. Unlike standard genome binning approaches using equal-sized bins at 10K-1Mbp resolutions, HiPPIE2 calls PIRs using restriction enzyme cutting sites and strand orientations in the ligation step of the Hi-C protocol to identify PIRs with higher resolution.

We applied HIPPIE2 to high read-depth in situ Hi-C datasets across 6 human cell lines (GM12878, IMR90, K562, HMEC, HUVEC, and NHEK) with matched functional genomics datasets from ENCODE and Roadmap.

We identified between 1.6 and 1.9 million PIRs across cell lines, with an average length of 1,005bps. The detected PIRs were highly reproducible (92.3% shared PIRs between two GM12878 replicates).

We discovered that PIRs are enriched for regulatory epigenetic marks (2.18 and 1.96 fold for H3K27ac and H3K4me1), suggesting active regulatory roles for PIRs.

84.29% of PIRs overlapped between cell lines on average, suggesting important common and cell-type specific functional roles. An average of 10.76% of PIRs overlapped TF binding sites (ChIP-seq), suggesting that the majority of PIRs may reflect high-level TF-independent chromatin architecture common across cell lines while a relatively small proportion are involved in cell-specific TF-mediated regulatory interactions.

HIPPIE2 identified 50,608 significant enhancer-promoter interactions (Fit-Hi-C algorithm) mediated by 45 distinct TFs (41 in enhancers and 40 in promoters), including many factors known to be involved in regulatory interactions (e.g., YY1, SP1, CTCF, MYC, NR4A1, MEF2, PAX5). 35 TFs were enriched in more than one cell line whereas 10 were specific to individual cell lines, identifying both global and cell-specific mechanisms of regulatory interaction.

The compendium of identified regulatory DNA-DNA-TF relationships such as enhancer-gene-TFs is valuable for understanding mechanisms underlying long-range and cell-type specific gene regulation and interpretation of non-coding variants in GWAS.

HiPPIE2 is designed to run on high-performance computing LSF and SGE clusters and is freely available at https://bitbucket.com/wanglab-upenn/HIPPIE2. 