# Dr. Fakhra Ghafoor — Academic Homepage

Built with the [academic-homepage](https://github.com/luost26/academic-homepage) Jekyll template (MIT License).

## Where to edit

| What | File |
| --- | --- |
| Name, bio, education, experience, awards, links | `_data/profile.yml` |
| Publications (one file per paper) | `_publications/<year>/*.md` |
| News | `_news/*.md` |
| Teaching & Activities cards | `_showcase/cv/*.md` |
| Blog posts | `_posts/YYYY-MM-DD-title.md` |
| Menu | `_data/navigation.yml` |
| Photo | put `portrait.jpg` in `assets/images/photos/` and set `portrait_url` in `_data/profile.yml` |
| CV (PDF) | `assets/files/Dr_Fakhra_Ghafoor_CV.pdf` |

Three paper thumbnails (`cover:`) link to the publisher's graphical-abstract images
(the others are key figures cropped from the paper PDFs). To keep local copies,
run `python scripts/download_covers.py` once; it saves the images to
`assets/images/covers/` and updates the `cover:` lines.

## Preview locally

```bash
bundle install
bundle exec jekyll serve
```
Then open http://127.0.0.1:4000

## Deploy

Push to a GitHub repository named `<username>.github.io`, then
Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.
