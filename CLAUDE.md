# Project Memory Configuration

This project uses Zep Cloud. Configuration is in `.project-context`.

## Startup Procedure

1. Read `.project-context` to get `ZEP_PROJECT_SESSION`
2. Use `zep_get_memory` with that session to load project facts
3. Acknowledge loaded context

## Memory Rules

**Project-specific facts:**
- Use `zep_store_memory` with session from `.project-context`
- Use `zep_search_memory` with session from `.project-context`

**Global knowledge:**
- Use `zep_store_memory` with session `global`
- Use `zep_search_memory` with session `global`

For this project, you will be guiding the user through creating the project, not coding it for the user. This is both
a learning experience for the user as well as a step in a more advanced project. You have been fed over 100 articles on  creating agents that are stored in the global Zep session. The user worked with Claude Desktop to come up with a plan that is stored in the Zep memory for this project.