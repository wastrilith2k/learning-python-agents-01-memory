# Project 1: Conversational Memory Agent

## Overview
Build a CLI-based chatbot that maintains conversation context across sessions using persistent memory. This project teaches fundamental AI agent concepts: LLM API integration, state management, and memory persistence.

---

## Learning Objectives

### Primary Goals
By completing this project, you will understand:

1. **Python Development Environment**
   - Setting up virtual environments (venv)
   - Managing dependencies with pip/requirements.txt
   - Project structure best practices
   - VSCode Python configuration

2. **LLM API Integration**
   - How API requests/responses work
   - Authentication and API keys
   - Token counting and cost management
   - Error handling and rate limits

3. **Conversation Context Management**
   - What is "context" in LLM conversations
   - How to structure conversation history
   - When to include/exclude previous messages
   - Context window limitations

4. **Persistent State/Memory**
   - Difference between runtime state and persistent storage
   - SQLite database basics (tables, queries, transactions)
   - Serializing/deserializing conversation data
   - Loading previous context on restart

5. **Prompt Engineering Basics**
   - System prompts vs user messages
   - Maintaining consistent agent personality
   - Controlling response format/length

### Secondary Learning Goals
- Basic SQL operations (CREATE, INSERT, SELECT)
- Working with environment variables (.env files)
- Python async/await patterns (if using async SDK)
- Command-line interface design
- Git version control workflow

---

## Technical Scope

### What This Project DOES
✅ Accept user input via CLI
✅ Send messages to LLM API (Claude Sonnet 4)
✅ Display AI responses in terminal
✅ Save conversation history to SQLite database
✅ Load previous conversations on restart
✅ Handle basic errors (API failures, invalid input)
✅ Track token usage and estimated costs

### What This Project DOES NOT DO
❌ No web interface / GUI
❌ No multi-user support
❌ No voice input/output
❌ No image/file handling
❌ No complex memory retrieval (semantic search)
❌ No agent frameworks (LangChain, CrewAI, etc.)

**Why these limitations?**
We're learning fundamentals first. Each excluded feature will be explored in future projects once you understand the basics.

---

## Architecture Overview

### High-Level Flow