Git is not the same as GitHub. In this article you'll learn about what distinguishes the two, and also what an important, related concept actually means. Let's talk about:

- Version Control
- Git
- Github

### Version Control & Version Control Systems

On a general level, you can think of version control like this:

>Version Control is the practice of keeping track of different versions of your code, or really any kind of product.

To make this _practice_ easier, more secure, and more efficient, you can use a **version control system**, or VCS for short. You can think of a version control system as a type of _database_. It keeps track of your files, the changes you are making, and lets you see every modification you made previously. It allows you to manage and revisit changes made to the files over time.

Version control systems also let you create **branches** in your project. A branch is a version of the project that split off at a certain point in time, and developed from there on separately to another branch of the same project. A VCS helps you to track these branches independently of one another, as well as merge them back together, if you want to combine the edits done on different branches. While doing so, it also keeps a record of who made which changes when.

<div class='alert alert-info' role='alert'>
    <strong>Info:</strong> As a real-life example of branching, think back to the example about creating multiple different resumes for different roles and companies. Each of these resumes could be a branch of the project
</div>

Being able to efficiently keep track of both the edit history as well as multiple versions of a project is quite powerful, but there is more to version control that makes it such a widely-applied concept:

- **Topic-Independent**: Version control is independent of what kind of technology or framework you are working with. You can use a VCS to track the files in a book you're writing, graphics you're creating, software projects your coding or any other file-based project you're working on your computer.

- **Tool-Independent**: Version control systems work well with a wide range of operating systems. Furthermore, it doesn't care if you are working with a text editor, a fancy IDE, or any other tool. It lets you work with the tools you are comfortable with. It simply tracks the changes to the files you are working on.

With this overview of version control in mind, let's sum up the main benefits of a VCS:

- **Reviewing**: Stepping back in time and keeping a historical record of the code base
- **Branching**: Creating and tracking different versions of a project alongside each other
- **Merging**: Combining the changes done on different branches back together
- **Tracking**: Tracing all changes to a given user and moment in time

The most popular open-source version control systems are **Git, SVN, CVS, and Mercurial**. Of those four, _Git_ is by far the most popular modern VCS.

### Git

Git is the most famous and widely used modern open-source version control system. It was created by <a href='https://en.wikipedia.org/wiki/Linus_Torvalds' target='_blank'>Linus Torvalds</a>, the creator of the Linux kernel, in 2005.

**Distributed**: Git is a _distributed_ version control system, which means that the entire codebase and history, including all branches of a project, are available on every person's computer who is involved in a project. This makes it easy to branch and merge at any given time.

<div class='alert alert-info' role='alert'>
    <strong>Info:</strong> You'll learn more about branching and merging in just a bit
</div>

Git also allows users to work on any number of projects at the same time and tracks each project independently of the others.

#### Advantages of Using Git

- **Performance**: Git provides high-quality performance when it comes to version control systems. Branching, merging and committing are all optimized for fast performance
- **Security**: Git secures your repositories with a cryptographically secure hashing algorithm named SHA-1
- **Offline-Access**: Network access is not mandatory to use Git, you can work with it offline on your computer
- **Distributed Development**: The distributed nature of Git allows you to have your own copy of a project and work locally on your own computer
- **Parallel Branches**: Git provides support for parallel development by supporting parallel branches
- **Clarity**: Git has an intermediate stage called the "staging area" that allows us to combine many files into a single commit. This helps to de-clutter the history of your project
- **History**: You can undo the changes you made, by reverting to previous versions on the file
- **Open-Source Software**: Git is open-source software, which means that developers can contribute from all over the world. The community can help by adding new features or solving newly discovered issues quickly

#### Disadvantages of Using Git

- **Complexity**: Git can be a bit difficult to learn for new users

### GitHub

Git and Github are not the same. While Git is version tracking software that runs on your local machine, _GitHub_ is a web service that hosts projects that are _tracked with Git_. It is a cloud-based system where you can store your Git projects outside of your local computer, and it also helps you keep track of your stored projects. Projects on GitHub are also called **repositories**.

<img alt="GitHub Repositories" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/git_github/imgs/github.png?raw=true">

GitHub offers additional features to Git. It has an intuitive graphical user interface to access the different functionalities, and supports its users with built-in task-management tools. Additional features and functionalities can be implemented via the _GitHub Marketplace_. Since GitHub repositories live on the internet, you can access the repositories you uploaded from any computer, anywhere in the world.

For individual users, GitHub is free to use. It makes its profit from companies that require additional features, such as added security, and support.

GitHub is popular, but not the only hosting service for Git repositories. Some other popular ones are <a href='https://about.gitlab.com/' target='_blank'>GitLab</a> and <a href='https://bitbucket.org/' target='_blank'>BitBucket</a>. They are both commonly used alternatives to GitHub that provide a similar set of features.

The majority of people who use Github are developers, but you don't need to be a developer to use GitHub. Since all it is is a web service for hosting your projects that you track via Git, you can use it to manage any files and projects you are working with. There are, for example, writers who use GitHub to store their developing novels, etc.

<div class='alert alert-info' role='alert'>
    <strong>Info:</strong> You can use GitHub to store any document that benefits from easy access, version control, and collaboration
</div>

#### Advantages of Using GitHub

- **Graphical User Interface**: GitHub provides a well-furnished and organized graphical interface, which makes interacting with your Git repositories intuitive
- **Collaboration**: GitHub provides access control and collaboration features such as wikis, as well as basic task management tools for every project
- **Online Storage**: GitHub lets you store your projects online in public as well as private repositories
- **Documentation**: GitHub provides <a href='https://docs.github.com/en' target='_blank'>excellent documentation</a> for its users. There are guides and articles for almost every topic related to Git & GitHub that you can think of
- **Education**: GitHub has helped popularize the use of Git. <a href='https://lab.github.com/)' target='_blank'>GitHub's Learning Lab</a> makes it easier to learn both Git and GitHub
- **Open-Source**: GitHub makes it easier to contribute to open-source projects. A large amount of popular open-source projects use GitHub.
- **Forking**: GitHub's flagship feature called "forking" is one of the most famous feature of the platform. Forking helps people with contributing to open-source projects and also lets you create something new by starting with a mirror of the original project. You will learn more about this shortly
- **Visualize Git**: GitHub gives us a variety of graphical tools to understand and visualize the changes made to a project, who made the changes and when the changes were made 
- **Portfolio**: You can easily showcase your work on GitHub. Nowadays, Github serves as a kind of portfolio site for many developers. In addition to showcasing your own projects, you can also highlight your contribution to open-source projects. When interviewing and reviewing a job candidate, many companies will take a look at the applicant's GitHub profile and projects. If your profile is solid and shows plenty of work, projects, and ideally also some open-source contributions, you will have a higher chance of getting hired
- **Discussion**: GitHub allows you to easily discuss issues with your project with other users

With this in-depth explanation in mind, let's look at an image that sums up the two main distinctions between Git and GitHub:

<img alt="Git Vs. GitHub Graphic" class="img-responsive cn_image" src="https://github.com/CodingNomads/static/blob/main/git_github/imgs/gitvsGithub.png?raw=true">

GitHub is an important tool for a modern software developer, and crucial for participating in collaboration with other programmers.

<div class='alert alert-info' role='alert'>
    <strong>Info:</strong> If you don't have a GitHub profile yet, head over to their website and <a href='https://github.com/join' target='_blank'>Sign Up</a> for an account.
</div>

Once you have your GitHub profile set up, you can head to the next page where you will learn about GitHub repositories.
