# 🤖 Chatbot (Python + Guanaco API)

A simple Python-based chatbot that communicates with the [Guanaco Chat Model API](http://guanaco-submitter.guanaco-backend.k2.chaiverse.com/endpoints/onsite/chat).  
This project uses modern tooling like `uv` for dependency management and GitHub Actions for CI.

---

## 📦 Features

- Interactive chatbot in the terminal
- Guanaco API-powered message generation
- Full chat history handling
- Modern dependency management via `uv`
- Unit tests using `pytest`
- GitHub Actions for continuous testing

---

## 🚀 Quick Start

### 🔧 Prerequisites

- Python 3.11 or later
- [`uv`](https://github.com/astral-sh/uv) (recommended, install via `curl -Ls https://astral.sh/uv/install.sh | sh`)
- `git`

---

### 📥 Installation

#### 1. Clone the repo

```bash
git clone https://github.com/eggji/chatbot.git
cd chatbot
```

#### 2. Sync dependencies using uv
```bash
uv sync
```

#### 3. Run the Chatbot
```python
python main.py
```

#### 4. Run the tests
```python
pytest tests/
```

### 📁 Project Structure
```bash
chatbot/
├── app/                    
│   ├── chatbot.py          
│   └── api_client.py       
│
├── tests/                  
│   └── test_chatbot.py
│
├── main.py                 
```
