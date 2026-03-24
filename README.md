# PromptPanda

PromptPanda is a prompt debugging and evaluation toolkit for LLM applications.
It analyzes prompts, detects weaknesses, suggests improvements, and runs prompt experiments to help developers build more reliable LLM systems.

The project simulates a prompt engineering workflow used in real AI systems.

---

## Features

* Prompt quality analysis
* Prompt improvement suggestions
* Prompt execution runner
* Prompt scoring
* Prompt library management
* JSON-based prompt storage
* Streamlit UI for testing prompts

---

## Use Cases

* Prompt engineering experiments
* LLM prompt debugging
* Prompt optimization
* Prompt evaluation for RAG / LLM apps
* Testing prompt variations

---

## Architecture

```
Prompt
  ↓
Analyzer
  ↓
Fixer
  ↓
Runner
  ↓
Score
  ↓
Library / Storage
```

---

## Modules

```
prompt_analyzer.py
prompt_fixer.py
prompt_runner.py
prompt_library.py
utils.py
app.py
```

---

## Project Structure

```
PromptPanda
│
├── app.py
├── prompt_analyzer.py
├── prompt_fixer.py
├── prompt_runner.py
├── prompt_library.py
├── utils.py
├── prompts.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Prompt Analyzer

Detects issues such as:

* vague prompts
* missing context
* unclear instructions
* weak constraints

---

## Prompt Fixer

Generates improved prompts by:

* adding constraints
* clarifying instructions
* enforcing output format
* improving specificity

---

## Prompt Runner

Executes prompts and returns response + score.

```
score = relevance + clarity + correctness
```

---

## Prompt Library

Stores prompts in JSON format.

```
prompts.json
```

Supports loading, saving and resusing prompts.

---


Streamlit dashboard for testing prompts.

Run:

```
streamlit run app.py
```

---

## Requirements

```
streamlit
requests
ollama
python-dotenv
```


---

## Motivation

Prompt engineering is critical for building reliable LLM applications.
Small prompt changes can significantly affect output quality.

PromptPanda was built to simulate a prompt debugging workflow similar to tools used in real AI development.

---

## Future Work

```
prompt benchmarking
multi-model comparison
RAG prompt testing
prompt versioning
automatic evaluation
```

