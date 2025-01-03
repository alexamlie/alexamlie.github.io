---
layout: archive
title: "Resume of Alex Amlie-Wolf, PhD"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

// I did part of this page and just decided to redirect to the public resume format 

{% include base_path %}

[Download this as a PDF](files/public_resume.pdf). 

Highly collaborative computational biologist with 13 years of experience in genomics and transcriptomics, large-scale data integration, RNA biology, and human genetics. 5+ years of industrial target nomination and drug development experience in disease areas including neuroscience, repeat expansions, immunology, and oncology. Experienced in people management, cross-functional collaboration, and communication with a wide range of audiences. Passionate about developing and applying computational methods to derive actionable biological insights from complex datasets. 

# Technical Skills
**Programming**: R (tidyverse, Rshiny), Python (large-scale data processing and ML), Unix and bash, cloud computing (AWS, GCP), pipelining and reproducible research (Snakemake, Nextflow, Docker, Anaconda), Jupyter, github/bitbucket, Atlassian (Confluence, Jira), auto-documentation (Sphinx), databases (SQL)

**Computational biology**: genomics (WES/WGS), transcriptomics (RNA-seq, TSS/PolyA-seq), epigenomics (ChIP/CLIP-seq), long read sequencing (Nanopore), proteomics, integrative analysis of public (FANTOM5, DepMap, ENCODE, GTEx, UK Biobank) and proprietary datasets, differential expression and differential splicing analysis, network biology and pathway analysis (IPA, GSEA, WGCNA) with regulatory factor inference, knowledge graphs, ontologies, machine learning and statistics, RNA structure prediction

**Genetics**: GWAS, QTL mapping, post-GWAS analysis (colocalization, functional data integration), haplotype deconvolution, repeat expansion, RNA splicing, transcriptional regulation, noncoding elements 

**Drug development**: GWAS, QTL mapping, post-GWAS analysis (colocalization, functional data integration), haplotype deconvolution, repeat expansion, RNA splicing, transcriptional regulation, noncoding elements 

# Professional Experience
## Arrakis Therapeutics, Waltham, MA
### Scientist II, Computational Biology. July 2021-Present
- Cross-functional, matrixed collaboration with biology and chemistry teams along the drug discovery process for neurology/repeat expansion, oncology, immunology, and additional target indications. This includes target RNA characterization and computational biology leadership around development of reproducible sequencing-based assays for compound discovery and screening and mouse PK/PD 
- Supervised and mentored one co-op student (H1 2021) who then transitioned to a Senior Research Associate position as my direct report (2022-2024) 
- Broadened skillset to include analysis of long read sequencing, proteomics, and RNA structure prediction tools to support integrative subtarget nominations for RNA-targeting small molecules 
- Facilitated maturation of internal data systems including documentation of computational pipelines and processes and supporting development of a data lake
- Incorporated human genetics data into target assessments along with continuously updating omics data sources to support platform approaches spanning multiple mRNA-centric mechanisms 

### Scientist, Computational Biology. June 2019-June 2021
- Multiomic (RNA-seq, TSS-seq, ribo-seq) analysis including differential expression and splicing, pathway and regulatory factor analysis of leaderboard compounds to characterize on- and off-target effects in relation to expected MoA and supporting Go/NoGo decisions on several projects  
- Developed reproducible cloud-based pipelines in close collaboration with experimentalists for sequencing data types including RNA-seq, TSS-seq, RACE-seq, polyA-seq & ribo-seq 
- Data mining of large-scale consortium (ENCODE, FANTOM5, CCLE, DepMap, GTEx), literature, and internal omics and genetics datasets for novel target characterization and prioritization based on RNA features for internal target pipeline and Roche and Amgen collaboration projects 
- Point person for academic collaboration and software licenses for computational biology requirements around RNA splicing assessment and pathway analysis (Qiagen) 

## University of Pennsylvania, Philadelphia, PA
### PhD Student in Genomics & Computational Biology. August 2013-May 2019
- Thesis research in Li-San Wang's lab involved integrative computational and experimental approaches for characterizing the regulatory mechanisms underlying noncoding genetic variation 
- Lead development of open-source INFERNO method for integrating hundreds of functional genomics datasets to INFER the molecular mechanisms of NOncoding genetic variants, with web server: http://inferno.lisanwanglab.org 
- Applied INFERNO to Alzheimer’s Disease where I uncovered novel lncRNA-mediated regulatory mechanisms and performed luciferase validation of enhancer activity 
- Applied INFERNO to a variety of phenotypes: neurodegenerative diseases (Parkinson’s, PSP, ALS, CBD, FTD), psychiatric traits (schizophrenia, ADHD), and 2,419 UK Biobank phenotypes to nominate regulatory mechanisms underlying disease 
- Implemented HiPPIE2 pipeline for Hi-C data analysis, from raw reads to high-resolution interacting sites, with functional annotation and identification of enhancer-promoter interactions 
- Throughout my thesis work, I gained experience in analyzing many types of 'omics data including RNA-seq and pathway analysis, ChIP-seq, DNA-seq, ATAC-seq, and Hi-C. I also applied statistical genetics approaches including colocalization, haplotype deconvolution, and Bayesian QTL mapping 
- My collaborative nature led me to many projects inside and outside of my thesis lab, spanning fields including neurodegenerative diseases (with Jerry Schellenberg, Virginia Lee, John Trojanowski, Eddie Lee), epigenetics (with Shelley Berger), and health economics (with Zeke Emanuel) 

# Education and Honors

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  

