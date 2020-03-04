--- 
title: "Data Network Dashboards"
author: "This document is currently under construction"
date: "2020-03-04"
site: bookdown::bookdown_site
output: bookdown::gitbook
documentclass: book
bibliography: [refs.bib]
biblio-style: apalike
link-citations: yes
github-repo: rstudio/bookdown-demo
description: "This is the manual for setting up a clean installation of the dashboards used in the EHDEN project."
---

# Preface {-}

**This document is currently under construction**

<!--<img src="images/Cover/Cover.png" width="250" height="375" alt="Cover image" align="right" style="margin: 0 1em 0 1em" /> -->

Automated Characterization of Health Information at Large-scale Longitudinal Evidence Systems (ACHILLES) is a profiling tool developed by the OHDSI community to provide descriptive statistics of databases standardized to the OMOP Common Data Model. These characteristics are presented graphically in the ATLAS tool. However, this solution does not allow for database comparison across the data network. The proposed solution aggregates ACHILLES results files from databases in the network and displays the descriptive statistics through graphical dashboards. The tool is helpful to gain insight in the growth of the data network and is useful for the selection of databases for specific research questions. In the software demonstration we show a first version of this tool that will be further developed in EHDEN in close collaboration with all our stakeholders, including OHDSI.

## Goals {-}

This manual aims to document the procedures to install and configure the chasrts and dashboards choosen to compare the OHDSI databases.

....

## Contributors {-}

To develop this tool, EHDEN organized a hack-a-thon (Aveiro, December 2-3, 2019), where we defined and implemented a series of charts and dashboards containing the most relevant information about the databases. The team involved in this task were composed by the following members:

* João Rafael Almeida^1^
* André Pedrosa^1^
* Peter R. Rijnbeek^2^
* Marcel de Wilde^2^
* Michel Van Speybroeck^3^
* Maxim Moinat^4^
* Pedro Freire^1^
* Alina Trifan^1^
* Sérgio Matos^1^
* José Luís Oliveira^1^

1 - Institute of Electronics and Informatics Engineering of Aveiro, Department of Electronics and Telecommunication, University of Aveiro, Aveiro, Portugal

2 - Erasmus MC, Rotterdam, Netherlands

3 - Janssen Pharmaceutica NV, Beerse, Belgium

4 - The Hyve, Utrecht, Netherlands

## License {-}

The system is open-source under the license ....

The book is written in [RMarkdown](https://rmarkdown.rstudio.com) using the [bookdown](https://bookdown.org) package.

## Acknowledges {-}

This work has been conducted in the context of EHDEN, a project that receives funding from the European Union’s Horizon 2020 and EFPIA through IMI2 Joint Undertaking initiative, under grant agreement No 806968.