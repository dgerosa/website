---
title: "Scalable data-analysis framework for long-duration gravitational waves from compact binaries using short Fourier transforms"
date: 2025-02-18
permalink: /posts/2025-02-18-scalable-data-analysis-framework-for-long-duration-gravitational-waves-from-compact-binaries-using-short-fourier-transforms
tags:
  - Milano
  - Papers
  - PRD
---

Long gravitational-wave signals are, well, long. And long often means painful, as more data need to be stored and processed. Kind of intuitively, the solution might be that of cutting things into chunks, so that long becomes short. Here we apply this idea to the popular inner product entering all gravitational-wave pipelines; this is a key building block of everything we do. The answer is that using SFTs, “Short-time Fourier Transforms”, can make things faster by more than 3 orders of magnitudes, sometimes 5. We think this is _the_ solution to future gravitational-wave data analysis problems (think LISA and 3G…).

R. Tenorio, **D. Gerosa**.\
[Physical Review D 111 (2025) 104044](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.104044). [arXiv:2502.11823 [gr-qc]](https://arxiv.org/abs/2502.11823).