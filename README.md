# split-it

## Table of Contents

- [About](#-about)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)

## 🤔 About

Split-it is a tool for splitting receipts and managing expenses among groups. It makes it easy to upload a receipt, assign items to people, and quickly see who owes what. **AI image uplaod (coming soon)**, so you'll eventually be ble to upload a photo of a receipt and have it parsed automatically, **voice recognition is also planned**, so users wouldn't have to upload who used what manually, but can use their voice to assign items. 

*Please note:* The implementation of this project may change if a more effective solution is identified.
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

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** React (Javascript) - coming soon
- **Dev Environment:** Docker & Docker Compose
- **AI for receipt parsing and voice recognition** - coming soon
