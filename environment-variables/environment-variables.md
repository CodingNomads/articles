# Using Environment Variables In Bash And Python

Every other program you build will include some secret information that you don't want to share with the world. API keys for your web service calls, database login credentials, or the ingredients to your secret sauce in your recipe generator.

While Git and GitHub is great, those personal secrets should _never_ make their way to the open source community.

In this blog post you will learn how to keep your secrets save using **environment variables**. By the end you will know how to:

- **Adding and removing** environment variables from your Bash command line
- Creating **virtual environment variables** in your Python virtual environment
- **Automatically setting and unsetting** these virtual environment variables when you activate or deactivate your virtual environment

Knowing how to work with environment variables is a crucial skill when building for the web, and can be helpful in many other situations that require some level of secrecy.

## Avoiding Horror Scenarios

The web is full of horror stories of accidentally posted API key secrets that ended up costing the owner a ton of money. If you need to stay up late tonight, or need some extra convincing, check out the following posts:

- [https://mikegerwitz.com/2012/05/a-git-horror-story-repository-integrity-with-signed-commits](A Git Horror Story: Repository Integrity With Signed Commits)
- [https://securosis.com/blog/my-500-cloud-security-screwup](My $500 Cloud Security Screwup)
- [https://www.theregister.co.uk/2015/01/06/dev_blunder_shows_github_crawling_with_keyslurping_bots/](Dev put AWS keys on Github. Then BAD THINGS happened)

The quick take-away is that you should never post your secrets to GitHub.

> Bots are quick, and one compromised commit is one too many.

There are a few ways to keep your sensitive information safe. In this article, you'll learn how to do it using environment variables in UNIX systems.

## Using Environment Variables

[Environment variables](https://en.wikipedia.org/wiki/Environment_variable) are variables that you can access from anywhere in your local system. They are usually shared across many applications.

In UNIX systems, the most famous one of them is [$PATH](<https://en.wikipedia.org/wiki/PATH_(variable)>) which specifies file paths where your system looks for executable files.

You can access the value of your environment variables anywhere in your project without ever spelling out the actual value of that variable. Instead, you can refer to it through the environment variable.

Because of that you can work with API secrets and passwords throughout your project, and commit all project-relevant code to GitHub, while keeping all these secrets safe to yourself.

### Inspecting Environment Variables

Open up your CLI and type `printenv`. This will give you a list of all the current environment variables present on your system:

```bash
HOME=/Users/Martin
LOGNAME=Martin
USER=Martin
PATH=/Library/Frameworks/Python.framework/Versions/3.9/bin:/usr/bin:/bin
```

This example output shows you a couple of environment variables that are currently defined on your local machine. You will probably see a different name and some additional lines in your output.

You can check the value of each variable with `echo $<NAME>`. For example, because the environment variable `$LOGNAME` points to `Martin` in my case, I can confirm this using the `echo` command:

```bash
echo $LOGNAME
```

The output you receive when running the same command will be whatever you have defined next to the `LOGNAME` variable that you can inspect by running `printenv`.

With these two commands you can inspect all the environment variables that are currently defined in your system, as well as their values. But what if you want to change, add, or remove one?

### Adding And Removing Environment Variables

You can add a new environment variable with the following command:

```bash
export <NAME>=<VALUE>
```

In this example, you'll have to replace `<NAME>` with the new environment variable that you want to add. You also need to replace `<VALUE>` with the value you want to assign to that environment variable.

For example, to add a new variable with the name `DAY` and the value `Sunday`, you would spell it out as follows:

```bash
export DAY=Sunday
```

After executing this command, you can see that there was a new variable added to your environment. Take a look at it using `printenv` and `echo` as described above.

In order to remove an environment variable, you'll have to call the following command:

```bash
unset <NAME>
```

Again, you'll have to add the actual name of the variable you want to remove instead of the placeholder `<NAME>`:

```bash
unset DAY
```

This command removes the `DAY` variable you set before.

Try adding and removing some environment variables using these commands. Remember you can check up on what’s happening using `printenv` or `echo <NAME>`.

However, when you are working on a Python web development project, you don't want to set your environment variables across your whole system. As soon as you're working on more than one Django project, the `SECRET_KEY` variables you need for each project will clash with each other. That's why you should compartmentalize your environment variables.

## Using Environment Variables In Python Virtual Environments

When doing any project-specific development, you always want to avoid setting anything for your whole system. The same counts for secrets, which are usually project-specific.

It's a much better idea to set such environment variables inside of **virtual environments**, which makes them turn into **virtual environment variables**.

Using environment variables inside of a Python virtual environment is easier than having to first `export` and then `unset` each variable every time you want to work on a project.

### Editing Your Activation Script

If you haven't yet created a virtual environment for your project, go ahead and make one:

```bash
python3 -m venv venv
```

This command creates a virtual environment in your current project folder. Learn more about working with virtual environments and Python in the [Python Engineering](https://codingnomads.co/courses/python-bootcamp-online/) course.

After you successfully created a virtual environment, open the `activate` script in your favorite text editor. You can find this file inside of the `venv` folder that got created by running the command shown above, specifically in `venv/bin/activate`.

This script runs every time your `venv` gets activated, which makes it a good place to let your computer know which environment variables you would like to have, and which ones to get rid of once you exit the virtual environment.

You will edit this script and hard-code the values in there. First, you need to make sure that your virtual environment variables won’t stick around once you deactivated it, so you start by _unsetting_ the environment variable that you haven't even created yet.

### Unsetting Virtual Environment Variables

To unset a virtual environment variable, you add an `unset` command to the `deactivate` command section in your `activate` script. The code in this part of the script runs every time you `deactivate` your virtual environment.

For example, to unset the variable `MY_SUPER_SECRET_SECRET`, you need to add the following line of code:

```bash
deactivate () {
    unset MY_SUPER_SECRET_SECRET
    # Lots of other code
}
```

Adding this line in the `deactivate` section makes sure that your virtual environment variables will remain only within your virtual environment, and not leak into your system environment.

Once you wrote the code to unset your variable, it's time to make sure you also _set_ it, so it will exist in the first place.

### Setting Virtual Environment Variables

You can set a virtual environment variable in the same way you learned about int he first section of this blog post. However, instead of typing the `export` command directly in your terminal, you'll add it as a new line of code at the end of the `activate` script:

```bash
# The rest of the script
export MY_SUPER_SECRET_SECRET="OMG this is so secret I can't even say!"
```

Safe the script and close it. Now you can activate your virtual environment:

```bash
source venv/bin/activate
```

Once the virtual environment has been successfully activated, you can now run the `printenv` command to inspect the state of your environment variables.

`MY_SUPER_SECRET_SECRET` should show up, as should the value you assigned to it.

After you confirmed that activating your virtual environment brings your virtual environment variable into existence, go ahead and deactivate it. Use `printenv` once again. Your secret should be gone.

As you can see, this setup can keep your project-specific secrets safe within their own comfy virtual environments.

### Accessing Virtual Environment Variables

To use one of your virtual environment variables inside of your Python project, you need to access it with Python's `os` module from the standard library:

```python
import os

secret = os.environ['MY_SUPER_SECRET_SECRET']
print(secret)
```

You'll be able to run this code from any file in your project, as long as your virtual environment is activated.

## Conclusion

Some secrets are meant to stay secret. Setting environment variables inside of your Python virtual environments allows you to easily access project-specific secrets without running into the danger of accidentally committing them to public version control.

Make sure that you add your virtual environment folder to your `.gitignore` file, or you'll end up pushing your secrets to GitHub after all!

In this blog post you learned how to:

- **Add and remove** environment variables in Bash
- Set up **project-specific environment variables** inside of your Python **virtual environments**
- **Access** environment variables with Python

If you’re interested in learning about Python web development from the ground up and drilling best practices right from the start check out the courses on [Python Engineering](https://codingnomads.co/courses/python-bootcamp-online/) and [Django Web Development](https://codingnomads.co/courses/django-course-learn-django-online). No snake-oil. Just coding.