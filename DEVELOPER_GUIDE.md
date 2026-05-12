# Developer Guide

This guide explains how to set up the MathEXLab website locally for development and how to contribute changes.

## Prerequisites

You will need:
- [Git](https://git-scm.com/)
- [Hugo](https://gohugo.io/installation/) (extended version recommended)

### Installing Hugo

**macOS (Homebrew):**
```bash
brew install hugo
```

**Linux:**
```bash
sudo apt install hugo
```

**Windows:**
```bash
winget install Hugo.Hugo.Extended
```

Verify the installation:
```bash
hugo version
```

---

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/MathEXLab/mathexlab-website.git
cd mathexlab-website
```

### 2. Run the local development server

```bash
hugo server
```

Hugo will build the site and serve it at [http://localhost:1313](http://localhost:1313). The server watches for file changes and hot-reloads automatically — you do not need to restart it when editing content.

To include draft content (pages with `draft: true` in their front matter):
```bash
hugo server -D
```

---

## Project structure

```
mathexlab-website/
├── content/          # Site content (Markdown files)
│   ├── contact/
│   ├── gallery/
│   ├── people/
│   ├── positions/
│   ├── publications/
│   ├── research highlights/
│   └── seminars/
├── static/           # Static assets (images, CSS, etc.)
├── layouts/          # Custom HTML templates
├── themes/ananke/    # Base theme (do not edit directly)
├── scripts/          # Utility scripts (e.g. Google Scholar scraper)
├── public/           # Built output — do not commit
└── hugo.toml         # Site configuration
```

### Key things to know

- **Content lives in `content/`** — each section corresponds to a subfolder. Most pages are Markdown files with YAML front matter.
- **Images and other assets go in `static/`** — they are served at the root URL (e.g. `static/images/foo.png` → `/images/foo.png`).
- **Do not edit files in `themes/ananke/`** — override them by creating matching files under `layouts/` instead.
- **Do not commit the `public/` directory** — it is the built output and is excluded by `.gitignore`.

---

## Contributing changes

> **All changes must go through a pull request. Do not commit directly to `main`.**

### 1. Create a branch

Branch off `main` and use a descriptive name:

```bash
git checkout main
git pull origin main
git checkout -b your-name/description-of-change
```

Examples:
- `alice/add-new-publication`
- `bob/update-people-photos`
- `fix/broken-seminar-link`

### 2. Make and preview your changes

Edit files in `content/`, `static/`, or `layouts/` as needed. Keep `hugo server` running to preview changes at [http://localhost:1313](http://localhost:1313) as you work.

### 3. Commit your changes

```bash
git add <files you changed>
git commit -m "Brief description of what changed"
```

Avoid `git add .` — it can accidentally include build artefacts or local config files.

### 4. Push your branch

```bash
git push origin your-name/description-of-change
```

### 5. Open a pull request

Go to the [GitHub repository](https://github.com/MathEXLab/mathexlab-website) and open a pull request from your branch targeting **`main`**.

- Write a short description of what you changed and why.
- Request a review from a maintainer before merging.
- Do not merge your own PR without approval.

---

## Common tasks

### Adding a team member

Create a new Markdown file under `content/people/` following the format of existing entries. Place their photo in `static/images/people/`.

TODO: Edit images to have coloured backgrounds

### Adding a publication

Add an entry to the relevant file under `static/all_publications.json`, or to scrape directly from Google Scholar, run `python scripts/scrape_google_scholar.py "<GOOGLE_SCHOLAR_ID>" START_YEAR` to scrape all papers by that author from starting year or later. Publications should deduplicate if they already exist.

### Adding a position or seminar

Create a new Markdown file under `content/positions/` or `content/seminars/` following existing examples.

### Updating site configuration

Global settings (site title, theme colour, social links) are in [hugo.toml](hugo.toml). Custom CSS is in [static/css/custom.css](static/css/custom.css).

---

## Deployment

Merging to `main` triggers deployment to [www.mathexlab.com](https://www.mathexlab.com). Do not push directly to `main`.
