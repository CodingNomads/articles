# CodingNomads Publishing

This repo contains source materials and information for CodingNomads' educational articles.

## CodingNomads Article Drafts

We use the `/article-drafts` repo to upload article and blog post drafts for review.

Once the article has been approved, the final version will be copied to a new public repository called `articles`.

### Drafts Structure

Each article and any associated code snippets or Notebooks live in their own top-level folder

### Feedback

Feedback on writing and didactics will be preferably given in GitHub comments. Check out the [Technical Writing Materials](https://codingnomads.github.io/creator-docs/01-content-guidelines/#structure) as a guideline.

---

## CodingNomads Educational Articles

The `/articles` repo contains articles, tutorials and blog post, as well as related materials, such as screenshots and code snippets.

### Articles Structure

Each article and any associated code snippets or Notebooks live in their own top-level folder.

### Publications

You will be able to find the rendered versions of these articles on our channels in various blogging platforms, e.g.:

- [Company Blog](https://codingnomads.co/blog)
- [dev.to](https://dev.to/codingnomads)
- [Medium](https://medium.com/codingnomads)

---

## Helper Scripts

This repository includes a few helper scripts to make repetitive edits and publishing easier. To make use of them, you need to do the following:

- Download and run `bash setup.sh` for the initial setup. This will clone this repository and install the necessary dependencies
- Activate your virtual environment with `source venv/bin/activate`

This completes the initial setup. In order to prepare a file for publication, use the `prepare.py` CLI application:

- Run `python3 prepare.py <filename>` to update links to new-tab links
- If you also want to add a clickable TOC, add the optional `-toc` flag: `python3 prepare.py <filename> -toc`
- If the Markdown content is copied from the learning platform, add the optional `-p` flag, which applies some additional cleanup actions: `python3 prepare.py <filename> -toc -p`

Replace `<filename>` with the path to the file you want to edit. Remember to use <kbd>Tab</kbd> to find the correct paths.

In order to push your edits back to both GitHub repositories, which makes it possible to pull the content over to WordPress, run `bash post.sh`. This command will commit the changes to version control, add a default commit message, and push to both remote repositories.

You can now head over to the WordPress Admin and pull in the article.

---

## Acknowledgements

TOC created using [github-markdown-toc](https://github.com/ekalinin/github-markdown-toc).
