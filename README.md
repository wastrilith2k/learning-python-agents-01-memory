# Conversational Memory Agent

A CLI-based chatbot that maintains conversation context across sessions using persistent memory. Built to learn fundamental AI agent concepts: LLM API integration, state management, and memory persistence.

**Part of:** Learn Python Agents Series - Project 1 of 5

---

## 🎯 What This Does

- Interactive command-line chat interface
- Maintains conversation context across multiple sessions
- Persists all conversations to SQLite database
- Uses Claude Sonnet 4 with prompt caching for cost optimization
- Displays token usage and cost estimates

## 🚀 Demo
```bash
$ python main.py

Welcome to the Conversational Memory Agent!
Type your message or '/quit' to exit.

You: Hello! What can you help me with?