---
layout: archive
title: "The best way to install Python"
permalink: /installpython/
author_profile: true
---

> My guide on how to install python. I wrote this back in 2015ish and it is now very outdated. We don't do things this way anymore. I leave it here on this website mainly for legacy; this used to be the most viewed page of this website by a large margin!


Python is cool, especially if you a scientist. All sort of scientific algorithms are already there (written and debugged!), you just have to use them. This is a step-by-step guide to the best way I found to install and use python for science, the easy (less hackable) way comes first, and the long way comes next.

### The easy way on mac: homebrew

Most (if not all) unix systems already come with a python distribution installed. However, it is advisable to install a local distribution and do your scientific stuff from there… If you screw something up, you can just delete everything and your OS is safe. I will also stay with python 2 for now,  but see below for some info on python 3 (see also [here](https://wiki.python.org/moin/Python2orPython3) for more).

The easiest way to safely install python on a MAC is [homebrew](https://brew.sh/). Homebrew installs a new version of python (by default the latest 2.x version available) and set is as default.

```
brew install python2
```

Next, we want a `virtualenv`. Python’s virtual environments are kind of separate boxes, where you can install modules and packages locally. You can have different boxes for different projects, or a single box for all your python stuff. Again, if you screw something up, you can just delete the box and start again. Now type

```
pip install virtualenv
virtualenv ~/box
```

The virtual environment is physically located in ~/box. You have created the box, but you’re still out of it. To get into the box

```
chmod u+x ${HOME}/box/bin/activate
source ${HOME}/box/bin/activate
```

Now you’re in the box, and you should see “(box)” close to your username in the terminal. To get out of the box, type

```
deactivate
```

and the label “(box)” should disappear from your terminal.

You may want to add this last command in your .bashrc

```
echo "" >>${HOME}/.bashrc
echo "alias inthebox='source ${HOME}/box/bin/activate' " >> ${HOME}/.bashrc
source ${HOME}/.bashrc
```

Now type “inthebox” and “deactivate” to get in and out of your new virtual environment.

### Science is fun again: install packages

And you’re done. `Virtualenv` comes with `pip`, the tool to install python modules from the Python Package Index [PyPi](https://pypi.python.org/pypi). From within your box, to install a package type

```
pip install PACKAGE\_NAME
```

But first of all, upgrade pip itself. It’s not needed strictly, but my experience is that it may fix issues, especially on mac OS X

```
pip install --upgrade setuptools pip
```

You can try with [numpy](http://www.numpy.org), [scipy](http://www.scipy.org), [matploltib](http://matplotlib.org), my own [precession](../?p=658) module to study black holes and my own [filltex](../?p=1108) module to handle Latex bibliographies.,

### Update: use python 2 and python 3 together…

As I mentioned, python 3 code is not really backward compatible with python 2. Python 3 is more recent, but there’s a lot of legacy code around that works only in python 2, so you might still need it (see [here](http://python-future.org/compatible_idioms.html) to write nice python 2-3 compatible code).

With virtual environments, you can have both python 2 and pyhton 3 on the same system, and switch between the two as needed. First, install a python 3 distribution:

```
brew install python3
```

Next, create another virtual environment and specify that the default python executable should be python 3

```
python3 -m venv box3
```

Now we have two boxes, `box` runs python 2 and `box3` runs python 3.  Now, let’s add the two boxes to our `bashrc`

```
echo "" >>${HOME}/.bashrc 
echo "alias py2='source ${HOME}/box/bin/activate' " >> ${HOME}/.bashrc 
echo "alias py3='source ${HOME}/box3/bin/activate' " >> ${HOME}/.bashrc 
source ${HOME}/.bashrc
```

If you type `py2` or `py3` you enter the respective box:

```
py2
python -V
>>>> Python 2.7.13
py3
python -V
>>>> Python 3.6.1
```

Again, `deactivate` will take you out of both boxes. If you need to use a package under both python 2 and python 3, you will need to install it twice via `pip`, in both boxes.

### The hard way (for the PROs)

Homebrew is great, but you can of course do the same manually. The procedure below is somehow taken from this [stack overflow](https://stackoverflow.com/questions/5506110/is-it-possible-to-install-another-version-of-python-to-virtualenv/5507373#5507373?newreg=78941aae422b4ddb9ed6ff43ebc2a0c4 "stackoverflow.com") question. Instructions here are given again for python 2 on mac OSX  but can be easily generalized to any unix system (e.g. replacing curl with wget and so on…).

First let’s install a python  distribution. Go to  [this URL](https://www.python.org/ftp/python/). 
and check what is the latest version of python 2. At the time of writing, this is 2.7.15, change the following lines if you want a different version. I am going to assume you want to put your new python distribution in a directory called “localpython” in your home directory

```
cd
mkdir localpython
cd localpython
curl  https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz > Python-2.7.15.tgz
tar -zxvf Python-2.7.15.tgz
cd Python-2.7.15
# "make clean" may be necessary here for earlier versions
./configure --prefix=${HOME}/localpython --enable-optimizations
make
make install
```

If, at any time, you need to start again, just

```
rm -rf ${HOME}/localpython
```

and you should be fine.

Now, virtualenv. Go to [this URL](https://pypi.python.org/pypi/virtualenv) and check what is the latest version of virtualenv. At the time of writing, this is 15.1.0, change the following lines if you want a different version.

```
cd ${HOME}/localpython
curl  https://pypi.python.org/packages/source/v/virtualenv/virtualenv-15.1.0.tar.gz > virtualenv-15.1.0.tar.gz
tar -zxvf virtualenv-15.1.0.tar.gz
cd virtualenv-15.1.0
${HOME}/localpython/bin/python setup.py install
```

Update: unfortunately pypi.python.org changed their link structure and the link above doesn’t work anymore. You need to go that webpage with a browser and get the tar.gz manually. At the time of writing, even the virtualenv official documentation has not been updated yet.

Now we create a virtual environment specifying it should run python from our local distribution. Again, we call our virtual environment “box” and place it in localpython

```
cd ${HOME}/localpython 
${HOME}/localpython/bin/virtualenv box --python=${HOME}/localpython/bin/python
```

If you get an error involving **zlib**, this is likely to be related to an upgrade of the OS: get back to the homebrew solution. If you’re still alive, type

```
chmod u+x ${HOME}/localpython/box/bin/activate
source ${HOME}/localpython/box/bin/activate
```

You can test everything with

```
which python
>>>  ${HOME}/localpython/box/bin/python
```

If you enter a python console, you should get today’s date and time (or yesterday’s if you found these instructions exhausting)

```
python
>>>  Python 2.7.10 (default, TODAY! )
```

To get out of the box, type

```
deactivate
```

As before, we can add these commands to our `.bashrc`

```
echo "" >>${HOME}/.bashrc
echo "alias inthebox='source ${HOME}/localpython/box/bin/activate' " >> ${HOME}/.bashrc
source ${HOME}/.bashrc
```

### Update: no pip, no fun!

I recently got across the situation that I did not want to use a virtual environment. This was because I was on a supercomputer which already had a python distribution installed and I didn’t want to deal with the scipy dependancies (e.g. lbpack etc.).

So, how to get pip and install modules anyway? The python people have a [script](https://pip.pypa.io/en/stable/installing/) precisely for this:

```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
```

Note the –user flag, which is good if you can’t sudo (as it was for me on the Caltech supercomputer).  Now, you only need to remember to install modules using this slightly different line:

```
python -m pip install MODULENAME --user
```

Done! Enjoy python on your supercomputer.

### Update: mac and backends, what a mess!

If you installed python on mac and tried to use [matplotlib](https://matplotlib.org/) to make beautiful plots for your papers, you might get into this error

RuntimeError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework.

This has to to with the default backend of matplotlib, which macOS doesn’t really like. The solution is

```
echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
```

### Now you can fly

Seriously… just [import antigravity](https://pypi.python.org/pypi/antigravity/0.1)

<p style="text-align: center;">
  <img src="https://imgs.xkcd.com/comics/python.png" alt="antigravity" style="max-width: 60%; height: auto;" />
</p>
Credit: [xkcd n. 353](https://xkcd.com/353/)