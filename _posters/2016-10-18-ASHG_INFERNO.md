---
title: "INFERNO – INFERring the molecular mechanisms of NOncoding genetic variants"
collection: posters
type: "Poster"
permalink: /posters/2016-10-18-ASHG_INFERNO
venue: "American Society of Human Genetics (ASHG)"
date: 2016-10-18
location: "Vancouver, Canada"
---

[Poster PDF](/files/16.10.18.AAW_ASHG.pdf)

Alexandre Amlie-Wolf, Mitchell Tang, Pavel P. Kuksa, Yuk Yee Leung, Barry Slaff, Jessica King, Beth Dombroski, Gerard D. Schellenberg, Li-San Wang

Genome-wide association studies (GWAS) have identified genetic variants associated with many diseases, but limitations remain. First, GWAS-identified variants tag
linkage disequilibrium (LD) blocks of potentially functional variants, many of which are not causal. Second, most GWAS variants are in the noncoding genome and may
affect transcriptional enhancers. Enhancers are context-specific and annotations are incomplete, so information must be integrated across tissue contexts and data
sources to identify enhancer variants. Finally, to translate GWAS findings into therapeutics, the affected genes and expression changes underlying disease risk must be
identified. We propose INFERNO, a new tool that addresses these limitations by integrating hundreds of diverse data sets to identify the causal variants within LD blocks,
the enhancers they affect, the tissue context of the enhancers, the affected target genes, and the direction of these effects.
Given a list of tagging variants, INFERNO uses 1,000 Genomes Project data to define LD blocks. Each linked variant is compared with: enhancer RNA transcription sites,
reflecting enhancer activity, across 112 tissue types from the FANTOM5 consortium; epigenetically-defined enhancers across 127 tissues and cell types from the Roadmap
Epigenomics consortium; expression quantitative trait loci across 44 tissues from the GTEx consortium; and predicted transcription factor binding sites (TFBSs) for 332
transcription factors from HOMER. Tissues or cell types from each data source are grouped into 38 broad tissue categories for comparison, and empirical p-values for the
enrichment of functional overlaps in each tissue category are obtained by bootstrapping.
Application of INFERNO to 19 top Alzheimer’s disease (AD) GWAS variants from the International Genomics of Alzheimer’s Project (IGAP) 2013 study identified significant
enrichment of functional variants affecting blood/immune enhancers in 18 of the tagged regions, bolstering the hypothesis of immune involvement in AD. Four regions
contained variants supported by all three functional data sources as well as predicted TFBSs, and luciferase assays validated their effects on enhancer activity. Thus,
INFERNO provides an easy and powerful approach for inferring the molecular mechanisms of noncoding genetic variants. We have implemented INFERNO in an efficient
Python- and R-based pipeline with source code and access to a web server version available at lisanwanglab.org/INFERNO.