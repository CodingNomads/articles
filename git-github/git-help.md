Git has many commands. Additionally, many of Git's commands also have some options that can be used in coordination with each command. This is similar to other command-line programs, e.g. `bash`'s `ls -al`. Here `ls` is the command, and `-al` are two additional arguments passed to the `ls` command. In this case, the arguments indicate the additional info we want the `ls` command to provide.

>Hearing that Git has "many commands" and each command may have "many options" might sound like a lot, but don't worry, if you learn about them piece-by-piece it won't be overwhelming. Also, the standard Git workflow doesn't even include many commands _or_ options.

Let's start off diving into Git commands by learning about a **meta-command**, one that can always help you to look up information about other commands. These extremely helpful Git commands are `git help` and `man git`. Both commands actually do the same thing: They surface the Git _documentation_ in general, or for a specific command that you can indicate.

>The output from the <code>man</code> and <code>help</code> commands is the exact same documentation, which is also found on the <a href='https://git-scm.com/docs/' target='_blank'>Git Docs</a> website

## Get Help With `git help`

Let's give the documentation lookup a spin. Enter the following in your terminal or Windows Git CLI:

```bash
$ git help
```

You will see output similar to the wall of text below:

```text
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
```

>Don't let yourself be intimidated by the amount of information that some of these help commands may return. They really <em>are</em> helpful, and it is well worth the time to read through them in order to learn what to do next

As mentioned above, you can add the name of a Git command after `git help`, e.g. `git help commit`, to get specific information about that Git command. This will give you even more, as well as more _specific_ information:

<img alt="Git Help Commit" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/git_github/imgs/git-help-commit.png?raw=true">

>To stop looking at the documentation of this Git command, type <kbd>q</kbd>

With these commands under your belt, you've just learned a great tool to keep exploring Git whenever you want to dive a little deeper. Let's also look at the second way to get help.

## Read The Docs With `man git`

Enter the following in your terminal or Windows Git CLI:

```bash
$ man git
```

You will notice that this opens up a similar-looking editor window as when using `git help commit` before:

<img alt="Man of Git" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/git_github/imgs/man-git-ryan.png?raw=true">

>The <code>man git</code> command shows the documentation for the general <code>git</code> command, which you can access also via <code>git help git</code>

You can be more specific here as well. For instance, you can run, `man git commit` to get a bunch of useful information about the `commit` command and the many arguments you can pass to it. 

<img alt="Git Commit Help Text" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/git_github/imgs/git-help-commit.png?raw=true">

Notice how the output of `git help commit` and `man git commit` seem to be the same? That's because hey are! Both of them access the same documentation page, which also matches the online documentation for <a href='https://git-scm.com/docs/git-commit' target='_blank'>Git Commit</a>.

>To stop looking at the manual and return to the original terminal window, type <kbd>q</kbd> then hit enter

Wherever and however you choose to access the Git documentation, keep in mind that they exist and that they are a great resource that you can and should consult whenever you need to look something up or want a refresher on one of the commands. These docs really are your friend, so don't forget to visit every once in a while :)
