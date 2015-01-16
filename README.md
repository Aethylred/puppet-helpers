# Introduction

This is a fork of the puppet-helper scripts wirtten by Guido Günther <agx@sigxcpu.org> and originally hosted on [a gitorious repository](https://gitorious.org/puppet-helpers/puppet-helpers). These scripts reduce the number of bad commits to the repository due to syntax errors and other minor issues.

# Git hooks

In the [git/hooks] directory there are a collection of hook scripts that can be used in working repositories ([Client Scrips](#Client Scripts)) and server side scripts ([Server Scripts](#Server Scripts))

## Client scripts

To use the hooks copy (or symlink) the scripts into `.git/hooks` in the working repository, including the `puppethooks/` directory and it's contents.

For a new git repository initialize the repository with:

```
$ git init --template <path to puppet-helpers checkout>
```

### `pre-commit`

This git pre commit hook to check syntax of puppet manifest, erb and ruby functions. Useful to check syntax when committing in your local repo.

## Server Scripts

To use the hooks copy (or symlink) the scripts into the `hooks` directory of the bare server side repository, including the `puppethooks/` directory and it's contents.

## `update`

This git update hook to check syntax of puppet manifest, erb and ruby. Useful to reject pushs with broken syntax on the server. It does not check for incorrect line endings, trailing whitespace, or style checks with a linter.

## `post-recieve`

This git post-recieve hook will attempt to remotely login as the puppet user on a puppet master via SSH and update the environment matching the git branch. Note that he master branch is mapped to the production environment.

This hook must be edited and updated for your environment to set the puppet host and the git repository URI.

The update process will:

* delete the environment if a branch is deleted
* clone the branch into the environment if it does not exist
* update the environment that matches the branch if it exists
* update all git submodules
* run [librarian-puppet](https://github.com/rodjek/librarian-puppet) if a `Puppetfile` exists in the root of the repository

Although git submodules are supported they are not recommended as they can be fragile and difficult to manage.

Some git commands can cause issues with this script, notably:

* forced pushes
* deleting git submodules
* changing the source URL of a git submodule

### Fixing Broken Environments

If an environment is broken the following processes may resolve the problem. Remember that when fixing the production environment, that this maps to the master branch.

#### Reset and pull

The first method is to roll back some troublesome changes and re-pull the environment from the repository. This is most effective when git is complaning that changes may be overwritten or lost. This often happens after a forced push or if someone has been editing the environment locally on the puppet master.

Log into the puppet master as the puppet user, assuming a normal puppet installation and a broken test branch/environment try the following:

```
$ cd /etc/puppet/environments/test
$ git reset --hard HEAD~2
$ git pull
```
#### Wipe and Clone

As the authoratitive copy of the environment exists not on the puppet master, but in the git repository it is relativly safe to delete the environment from the puppet master and re-clone it from the repository, even for the production environment.

Log into the puppet master as the puppet user, assuming a normal puppet installation and a broken test branch/environment try the following:

```
$ cd /etc/puppet/environments
$ rm -rf test
$ git clone -b test https://git.example.org:puppet.git test
```

# Puppet report YAML parser

[This](yaml/puppet_yaml.py) is currently undocumented.

# Issues

Report bugs, issues, and improvements to the [Github project](https://github.com/Aethylred/puppet-helpers/issues)
