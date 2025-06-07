---
title: 'Gravitational-wave selection effects using neural-network classifiers'
date: 2020-07-15
permalink: /posts/2020/07/15/gravitational-wave-selection-effects-using-neural-network-classifiers
tags:
  - Birmingham
  - Papers
  - PRD
---

And here is my latest lockdown effort: some experiments in the wonderful and perilous world of machine learning. The idea of this paper is to teach a computer to figure out by itself if a gravitational-wave signal will be detectable or not. The problem is very similar to that of image recognition: much like classifying if an image is more likely to contain a dog or a cat, here we classify black-hole mergers based on the imprints they have in the LIGO and Virgo detectors. This is important to quantify the so-called “selection effects”: in order to figure out what the Universe does based on what we observe, we need to know very well “how” we observe and thus what we are going to miss. Our code is built using Google’s [TensorFlow](<https://www.tensorflow.org/>) and it is [public on Github](<https://github.com/dgerosa/pdetclassifier>), feel free to play with it! 

**Davide Gerosa** , Geraint Pratten, Alberto Vecchio.  
Physical Review D 102 (2020) [103020](<https://link.aps.org/doi/10.1103/PhysRevD.102.103020>).  
arXiv:[2007.06585](<https://arxiv.org/abs/2006.06647>) [astro-ph.HE]  
Open-source code: [homepage](<../../../../../index.html?p=3529>), [repository](<https://github.com/dgerosa/pdetclassifier>).

[comment]: Machine generated below here
