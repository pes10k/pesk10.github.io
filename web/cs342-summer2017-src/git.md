---
layout: page
title: Git
permalink: /git/
---

This course will use git repos to distribute homework assignments, and you'll
need to use your own repos to submit those assignments.

This page is a very basic overview of how to get your repos set up to get
and submit assignments.  These instructions assume some familiarity with git.
If you're not familiar with terms like `pull`, `push`, and `remote`, you might
want to brush up on those topics elsewhere before continuing.


## 0. Overview of Setup
Each student will need to interact with two repos during the course.  The
`course` repo, at `git@git.uicbits.net:cs342/course.git`, is maintained by
me and the TA.

We'll use it to post skeleton code for each assignment. The
other repo you'll interact with is your own, which we'll call `origin`.

Students will pull changes in from the `course` repo, into their own repos,
complete the assignments, and then push the completed assignments into their
`origin` repos.

## 1. Generating Keys
Each student will need to generate a SSH key for authenticating with the git
repos. Instructions for doing so might differ if you're on Windows, but the
general pattern is to do something like the following:

(*note*: if you already
have a public key, at either `~/.ssh/id_ed25519.pub` or `~/.ssh/id_rsa.pub`,
you can just send that public key and ignore the rest of this step.)

```bash
# Generate a public/private key pair
ssh-keygen -t ed25519

# Follow all the instructions prompted.  This should generate a private
# key at ~/.ssh/id_ed25519 and a public key at ~/.ssh/id_ed25519.pub.
# You can test if this is the case with:
file ~/.ssh/id_ed25519.pub

# Then add the newly generated priviate key to your SSH agent, so that
# git knows to use it when authenticating with the git server.
ssh-add ~/.ssh/id_ed25519
```

You should then send the *public* key to me over email.  Make sure you're not
sharing the private key with anyone or it will defeat the whole purpose of
using public/private keys.

## 2. Configuring Your "origin" Repo
Once we've got your public key in place, the next steps are to get your
`origin` repo cloned and set up to get code from the `course` repo.  In other
words, we need to get the place where you'll write your code ready to go,
and then get that place set up to bring in the skelleton code from the course
repo.

```bash
# First, we clone your personal repo, which we'll call 'origin'.  By default
# this will be empty, since you've written no code so far.  Make sure to
# replace <NETID> in the example below with your own NETID.
git clone git@git.uicbits.net:cs342/<netid>.git cs342hw

# Assuming everything is set up at this point, you'll have a directory
# called cs342hw, which will be an empty git repo.  We'll move into it
# so that we can start getting it configured to pull in changes from the
# `course` repo.
cd cd342h2

# Next, configure the git repo to be able to pull in changes from the `course`
# repo.
git remote add course git@git.uicbits.net:cs342/course.git
```

## 3. Getting And Submitting Assignments
You're now ready to start pulling in changes from the course repo, so that
you can start on your assignments.  For each assignment, you'll generally
follow these steps.

```bash
# First, fetch any changes from the `course` repo that you don't already
# have in your local repo.
git pull course master

# The first time you do this, it'll create some directories I've set up for
# you.  For example, you'll have a .gitignore file, to help keep your repo
# closed, and a skelletal hw1 directory.
#
# You can then do some work on the assignment.  Once you have some changes
# you'd like to save / back up / commit in your repo, you can do so by
# adding them to the next "bundle" of changes you'd like to store, and then
# "storing" them in the repo (ie commiting them).

# Making some changes...
vim hw1/src/Main.java

# Telling git about the files you want to bundle together
git add hw1/src/Main.java

# Saving the changes that have been bundled together, along with a helpful
# note describing those changes"
git commit -m "Updated the main function in Main.java"

# Last, you'll want to occasionally push those changes back into your origin
# repo (ie the copy of your repo stored on UIC's servers).  This both makes sure
# that your changes are backed up remotely, and shares your changes with us
# so they can be graded or discussed.
git push origin
```

You'll do the above patern for each assignment, `pull`ing new assignments
and outlines from the `course` server, and pushing your completed changes
back into your `origin` server.


## 4. Questions and Debugging
Git is an extremly powerful, but occasionally baffling, tool, especially when
you're just learning it.  Please don't hesitate to ask any questions or share
any problems that come up on [Piazza]({{ site.piazza_url }}) and we'll be
very happy to help debug or get things set straight.
