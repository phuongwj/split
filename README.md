# split-it

## Table of Contents

- [About](#-about)
- [Project Structure](#-project-structure)

## 🤨 About
Split-it is a backend and (soon) frontend project for splitting receipts and expenses among groups of people. The goal is to make it easy to upload a receipt, assign items to people, and quickly see who owes what. **OCR (Optical Character Recognition) support is planned** - so you'll eventually be able to upload a photo of a receipt and have it parsed automatically.

Split-it goal is to help groups easily manage shared expenses by letting users upload receipts, assign items to individuals, and instantly see who owes what. With **OCR (Optical Character Recognition)** support planned, users will eventually be able to upload a photo of a receipt and have the items parsed automatically.

## 🧱 Project Structure
```
split-it/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models/
│   │   │   ├── bill.py
│   │   ├── routers/
│   │   │   ├── split.py
│   │   ├── services/
│   │   │   ├── split_service.py
│   │   ├── requirements.txt
│   │   ├── Dockerfile
│   │   ├── .dockerignore
├── frontend/
```

## Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** React (Javascript), coming soon...
- **Dev Environment:** Docker & Docker Compose