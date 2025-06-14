---
layout: archive
title: "From git to git"
permalink: /git2git/
redirect_from:
  - /svn2git/
---

This is a short guide to migrate repositories between different hosts, while preserving the history. 

## git to git

First, let's go from git to git. We want to migrate from one server to another, say because you're copying that repository somewhere else. The naive way is to clone the old repo, move files manually, and push to the new repo. That works but you're not going to preserve the history of the old repository.  You'll find a million solutions around if you google this problem, but [this](https://stackoverflow.com/a/26552740) is by far the best one:

```
git clone --mirror git@github.com:dgerosa/OLD_REPO
cd OLD_REPO.git
git remote set-url origin git@github.com:dgerosa/NEW_REPO
git push --mirror origin
```  


## svn to git

Once upon a time, I was using svn to handle my research projects, then saw the light and discovered git (there are a billion of GIT tutorials on the web, but if you’re looking for a recommendation, I found [this](https://www.atlassian.com/git) page from Bitbucket very nice!).

So, you have many svn repos and want to switch to git? I am going to assume you have very simple svn repositories (one single branch, no tags) like I used to have. If you have a more complicated structure, have a look [here](https://git-scm.com/book/en/v2/Git-and-Other-Systems-Migrating-to-Git) and [here](http://www.sailmaker.co.uk/blog/2013/05/05/migrating-from-svn-to-git-preserving-branches-and-tags-3/).

You need the [git-svn](https://git-scm.com/docs/git-svn) tool. It should be there by default, but if you don’t have it, you can easily install it from your package manager.

First, clone your old SNV repository using `git svn`. Use the same link you used to checkout the svn repo in the first place. Then push it to the new remote on git:

```
git svn clone svn+ssh://USER@HOST/PATH/SVNNAME
cd SVNNAME
git remote add origin [\[email protected\]](https://davidegerosa.com/cdn-cgi/l/email-protection):USERNAME/GITNAME
git push origin --all
```


## Repo too big?

I recently tried to run these commands again, and found out one of my old repo was too big for the remote server I want to use. Just want to say that this tool called [bfg](https://rtyley.github.io/bfg-repo-cleaner/) is great to reduce a repo size while removing only some of the previous history.


### The ultimate git solution

If you get stuck with git, this always works:

<p style="text-align: center;">
  <img src="https://imgs.xkcd.com/comics/git_2x.png" alt="git" style="max-width: 60%; height: auto;" />
</p>
Credit: [xkcd n. 1597](https://xkcd.com/1597/)