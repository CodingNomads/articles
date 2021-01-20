## Keep Your Secrets Safe With Environment Variables

Most programs that you build will include some secret information that you don't want to share with the world. Think about API keys for your web service calls, database login credentials, or the ingredients to your secret sauce in your recipe generator!

> While Git and GitHub are great, those personal secrets should _never_ make their way to the open-source community.

That's where **environment variables** come in handy. In this blog you will learn how to keep your secrets safe using environment variables in Bash and Python virtual environments. By the end you will know how to:

- **Set a variable** in Bash
- **Add and remove** environment variables from your Bash command line
- Create **virtual environment variables** in your Python virtual environment
- **Automatically set and unset** these virtual environment variables when you activate or deactivate your virtual environment

Knowing how to work with environment variables is a crucial skill when building for the web, and can be helpful in many other situations that require some level of secrecy.

## Table of Contents

- [Avoiding Horror Scenarios](#avoiding-horror-scenarios)
- [Using Environment Variables In Bash](#using-environment-variables-in-bash)
  - [Inspecting Environment Variables](#inspecting-environment-variables)
  - [Adding And Removing Environment Variables](#adding-and-removing-environment-variables)
- [Using Environment Variables In Python Virtual Environments](#using-environment-variables-in-python-virtual-environments)
  - [Editing Your Activation Script](#editing-your-activation-script)
  - [Unsetting Virtual Environment Variables](#unsetting-virtual-environment-variables)
  - [Setting Virtual Environment Variables](#setting-virtual-environment-variables)
  - [Accessing Virtual Environment Variables](#accessing-virtual-environment-variables)
- [Conclusion](#conclusion)

<h2 id="avoiding-horror-scenarios">Avoiding Horror Scenarios</h2>

The web is full of horror stories of accidentally posted API key secrets that ended up costing the owner a lot of money. If you need some extra convincing, or just want to stay up late tonight, check out the following posts:

- <a href='https://mikegerwitz.com/2012/05/a-git-horror-story-repository-integrity-with-signed-commits' target='_blank'>A Git Horror Story: Repository Integrity With Signed Commits</a>
- <a href='https://securosis.com/blog/my-500-cloud-security-screwup' target='_blank'>My $500 Cloud Security Screwup</a>
- <a href='https://www.theregister.co.uk/2015/01/06/dev_blunder_shows_github_crawling_with_keyslurping_bots/' target='_blank'>Dev put AWS keys on Github. Then BAD THINGS happened</a>

The quick take-away is that you should _never_ post your secrets to GitHub.

> Bots are quick, and one compromised commit is one too many.

There are multiple ways to keep your sensitive information safe. In this article, you'll learn how to do it using environment variables in UNIX systems.

<h2 id="using-environment-variables-in-bash">Using Environment Variables In Bash</h2>

[Environment variables](https://en.wikipedia.org/wiki/Environment_variable) are dynamic-named values, which you can access from anywhere in your current environment. They can help you make running your scripts more user-friendly and secure, and are shared across all applications in your current environment.

In UNIX systems, the most famous one of them is <a href="https://en.wikipedia.org/wiki/PATH_(variable)" target="_blank">$PATH</a>, which specifies file paths where your system looks for executable files.

You can access the value of your environment variables anywhere in your project without ever spelling out the actual value of that variable. Instead, you can refer to it through the environment variable defined in Bash.

That way you can work with API secrets and passwords throughout your project, and commit all project-relevant code to GitHub while keeping your sensitive information safe and to yourself.

<h3 id="inspecting-environment-variables">Inspecting Environment Variables</h3>

Open up your CLI and type the Bash command `printenv`. This will give you a list of all the current environment variables present on your system:

```bash
HOME=/Users/Martin
LOGNAME=Martin
USER=Martin
PATH=/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/bin:/bin
```

This example output shows you a couple of environment variables that are currently defined on your local machine. You'll probably see a different name and some additional lines in your own output.

You can check the value of each variable with `echo $<NAME>`. Because the environment variable `$LOGNAME` points to `Martin` in my case, I can confirm this using the `echo` command:

```bash
echo $LOGNAME
```

The output you receive when running the same command will be what your `LOGNAME` variable points to. You can confirm this value also by running `printenv` and looking for `LOGNAME` in your output.

With these two commands, you can inspect all the environment variables that are currently defined in your system. But what if you want to change, add, or remove one using Bash?

<h3 id="adding-and-removing-environment-variables">Adding And Removing Environment Variables</h3>

Using Bash in your CLI, you can add a new environment variable with the following command:

```bash
export <NAME>=<VALUE>
```

In this example, you'll have to replace `<NAME>` with the new environment variable that you want to add. You also need to replace `<VALUE>` with the value you want to assign to that environment variable.

For example, to add a new variable with the name `DAY` and the value `Sunday`, you would spell it out as follows:

```bash
export DAY=Sunday
```

After executing this command, you can see that a new variable has been added to your environment. Take a look at it using `printenv` and `echo` as described above.

In order to remove an environment variable with Bash, you'll have to call the following command:

```bash
unset <NAME>
```

Again, you'll have to add the actual name of the variable you want to remove instead of the placeholder `<NAME>`:

```bash
unset DAY
```

This Bash command removes the `DAY` variable you set before.

> Try adding and removing some environment variables using these Bash commands. Remember you can always check what’s happened using `printenv` or `echo <NAME>`.

However, when you are working on a Python web development project, you don't want to set your environment variables across your whole system environment. For example, as soon as you're working on more than one Django project, the `SECRET_KEY` variables you need for each project will clash with each other. That's why you should compartmentalize your environment variables using **virtual environments**.

<h2 id="using-environment-variables-in-python-virtual-environments">Using Environment Variables In Python Virtual Environments</h2>

When doing any project-specific development, you always want to avoid setting anything for your whole system. The same counts for secrets, which are usually project-specific.

It's a much better idea to set these types of environment variables inside of **virtual environments**, which makes them turn into **virtual environment variables**.

Using environment variables inside of a Python virtual environment is easier than having to first `export` and then `unset` each variable every time that you want to work on a project.

<h3 id="editing-your-activation-script">Editing Your Activation Script</h3>

Start by creating a virtual environment for your Python project:

```bash
python3 -m venv venv
```

This command creates a virtual environment in your current project folder. You can learn more about working with virtual environments and Python in the <a href='https://codingnomads.co/courses/python-bootcamp-online/' target='_blank'>Python Engineering</a> course.

After you successfully created a virtual environment, open the `activate` script in your favorite text editor. You can find this file inside of the `venv` folder that got created by running the command shown above. The relative path of this script is `venv/bin/activate`.

This Bash script runs every time your `venv` gets activated, which makes it a good place to let your computer know which environment variables you would like to have, and which ones to get rid of once you exit the virtual environment.

You will now edit this Bash script and hard-code the values you want in there. First, you need to make sure that your virtual environment variables won’t stick around once you deactivated them, so you start by _unsetting_ the environment variable that you haven't even created yet.

<h3 id="unsetting-virtual-environment-variables">Unsetting Virtual Environment Variables</h3>

To unset a virtual environment variable, you add an `unset` command to the `deactivate` command section in your Bash `activate` script. The code in this part of the script runs every time you `deactivate` your virtual environment.

For example, to unset the variable `MY_SUPER_SECRET_SECRET`, you need to add the following line of Bash code:

```bash
deactivate () {
    unset MY_SUPER_SECRET_SECRET
    # Lots of other code
}
```

Adding this line in the `deactivate` section makes sure that your virtual environment variables won't leak into your system environment. Instead, they'll exist only within your virtual environment.

Once you wrote the code to unset your variable, it's time to make sure you also _set_ it, so it'll exist in the first place.

<h3 id="setting-virtual-environment-variables">Setting Virtual Environment Variables</h3>

You can set a virtual environment variable in the same way as you practiced before when using the Bash CLI for it. However, instead of typing the `export` command directly in your terminal, you'll add it as a new line of code at the end of the `activate` script:

```bash
# The rest of the script
export MY_SUPER_SECRET_SECRET="OMG this is so secret I can't even say!"
```

Save the Bash script and close it. Now you can activate your virtual environment:

```bash
source venv/bin/activate
```

Once the virtual environment has been successfully activated, you can now run the `printenv` command to inspect the state of your environment variables in your current environment.

`MY_SUPER_SECRET_SECRET` should show up, as should the value you assigned to it.

After you confirmed that activating your virtual environment brings your virtual environment variable into existence, go ahead and deactivate it. Use `printenv` once again. Your secret should be gone.

As you can see, this setup can keep your project-specific secrets safe within their own comfy virtual environments.

<h3 id="accessing-virtual-environment-variables">Accessing Virtual Environment Variables</h3>

To use one of your virtual environment variables inside of your Python project, you need to access it with Python's `os` module from the standard library:

```python
import os

secret = os.environ['MY_SUPER_SECRET_SECRET']
print(secret)
```

You'll be able to run this code from any file in your project, as long as your virtual environment is activated, and an environment variable called `MY_SUPER_SECRET_SECRET` is defined.

If you don't want your script to terminate with an exception when you didn't define the environment variable, then you can use Python's <a href='https://docs.python.org/3/library/stdtypes.html?highlight=dict%20get#dict.get' target='_blank'><code>dict.get()</code></a> method instead of doing a direct lookup.

<h2 id="conclusion">Conclusion</h2>

Some secrets are meant to stay secret. Setting environment variables inside of your Python virtual environments allows you to easily access project-specific secrets without running into the danger of accidentally committing them to public version control.

> Make sure that you add your virtual environment folder to your `.gitignore` file, or you'll end up pushing your secrets to GitHub after all!

In this blog post you learned how to:

- **Add and remove** Python environment variables in Bash
- Set up **project-specific environment variables** inside of your Python **virtual environments**
- **Access** environment variables with Python

If you’re interested in learning about Python web development from the ground up and drilling best practices right from the start, check out CodingNomads' courses on <a href='https://codingnomads.co/courses/python-bootcamp-online/' target='_blank'>Python Engineering</a> and <a href='https://codingnomads.co/courses/django-course-learn-django-online' target='_blank'>Django Web Development</a>.
