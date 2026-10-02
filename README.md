# Best Cars Dealership Review Portal

Full Stack Application Development Capstone Project.

A full stack web application for a national car dealership ("Best Cars")
that lets customers look up dealership branches across the United States,
filter them by state, read customer reviews with sentiment analysis, and
register an account to post their own reviews.

## Tech stack

- **Frontend**: React, HTML, CSS, Bootstrap
- **Main application**: Python, Django, SQLite (user management, car
  makes/models, proxy services)
- **Dealership & review service**: Node.js, Express, MongoDB (Dockerized)
- **Sentiment analyzer**: Python, Flask, NLTK (deployed on IBM Cloud Code
  Engine)
- **CI/CD**: GitHub Actions (linting)
- **Deployment**: Docker, Kubernetes

## Project structure

- `server/` - Django project (`djangoproj`), Django app (`djangoapp`),
  React frontend (`frontend`), Express-MongoDB service (`database`),
  Dockerfile and Kubernetes deployment artifacts
- `.github/workflows/` - CI linting workflow
