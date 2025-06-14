---
layout: archive
title: "My notes to install the LIGO Algorithm Library (lal)"
permalink: /installlal/
author_profile: true
---

>  This guide is very outdated, don't use it. Take it as a testimony of how hard things used to be in 2015ish. Now it's a pip install dreamland.


If you do research in gravity, you probably know what [lal](http://software.ligo.org/docs/lalsuite/lalsuite/) is (if not, maybe you should leave this page…). It’s a monumental set of codes and tools developed by the LIGO and Virgo Collaboration to run gravitational-wave search pipelines, source modeling studies, etc, etc.

It’s a great open-source tool if you know how to use it, but installation can be messy. I recently went through the process and would like to share my steps (this is mostly a set of notes for myself if I have to do it again, but thought maybe can be useful to others). The guide here mostly follows [this one](http://pycbc.org/pycbc/latest/html/install.html).

I was interested in doing basic stuff, like plotting waveforms, computing signal-to-noise ratios, etc. I think the most accessible way is the python [pyCBC module](https://ligo-cbc.github.io/pycbc/latest/html/). It provides a reasonable high-level interface to many of the lal functions, which is what I like.

**Important**: if you use pyCBC for your research, make sure you cite them as they want to be cited! See [here](https://ligo-cbc.github.io/pycbc/latest/html/credit.html).

**Important**: I’m not a lal or pyCBC developer, this is just my personal set of notes.

### Before you start…

On Mac, first use [homebrew](https://brew.sh/) to install a couple of things you’re going to need (maybe you have them already, I didn’t):

brew install gsl
brew install swig

### Isolate the mess

We will install lal and pyCBC in a dedicated virtual environment. Given how easy it is to mess things up, this **definitely** the way to go. If you don’t have it, I wrote about installing virtual environment [here](/installpython/).  First, go somewhere in your system (this will be the parent directory of your lal installation) and create a python virtual environment in there

```
cd somewhere
virtualenv lal
```

I personally find useful to have a short command to get in and out the environment. This will add a `lal` alias to your `bashrc`:

```
echo "" >>${HOME}/.bashrc
echo "alias lal='source ${HOME}/lal/bin/activate' " >> ${HOME}/.bashrc
source ${HOME}/.bashrc
```

Now you can type `lal` and `deactivate` to go in an out the virtual environment.

Go in, and install some basic python packages

```
lal
pip install --upgrade pip
pip install --upgrade setuptools
pip install numpy scipy matplotlib h5py astropy dqsegdb
```

Do not move the lal directory of your virtual environment, or everything will break because paths are hardcoded everywhere. If you want to change the installation location, delete everything and start again. If you get errors somewhere along the way and need to start again, just remove the lal directory and everything you’ve done will go with it.

### Install lalsuite

Now we are ready to install lalsuite. Create a source directory and clone the repository

```
mkdir -p ${VIRTUAL\_ENV}/src
cd ${VIRTUAL\_ENV}/src
git clone https://git.ligo.org/lscsoft/lalsuite.git # Takes a while...
cd ${VIRTUAL\_ENV}/src/lalsuite
```

LIGO migrated their repositories in Dec 2017. Earlier versions are at: [github.com/lscsoft/lalsuite.git](https://github.com/lscsoft/lalsuite.git).

Now, proceed with a simplified installation. Right now I am only interested in plotting waveforms, compute SNR, matches etc, so I removed things that for me are unnecessary:

```
./00boot
./configure --prefix=${VIRTUAL\_ENV}/opt/lalsuite --enable-swig-python --disable-lalstochastic --disable-lalxml --disable-lalinference --disable-laldetchar --disable-lalapps --disable-lalframe --disable-lalmetaio --disable-lalpulsar
make
make install
```

By the way, after running the configure command, you should have received a message which says something like

```
>>> LALSimulation has now been successfully configured:
>>> * Python support is ENABLED
>>> (many other things) DISABLED
```

If you don’t have this, then I guess something went wrong.  This piece of code requires the execution of a script to make variables accessible, etc. It’s useful if you run it together with the virtual environment activation script:

```
echo 'source ${VIRTUAL\_ENV}/opt/lalsuite/etc/lalsuite-user-env.sh' >> ${VIRTUAL\_ENV}/bin/activate
deactivate
lal
```

As a test of your successful installation, try

```
echo $LAL\_PREFIX
```

and you should get the lalsuite installation directory.

### Install pyCBC

After that, installing pyCBC is as easy as:

```
pip install PyCBC
```

You can try some of the examples presented [here](http://ligo-cbc.github.io/pycbc/latest/html/waveform.html).