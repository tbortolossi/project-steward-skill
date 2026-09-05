# Technology Profile Detection

Project Steward should automatically infer applicable profiles from repository contents.

## Detection hints

### Python
Any of:
- `pyproject.toml`
- `requirements*.txt`
- `setup.py`
- meaningful `.py` tree

Load:
- `python.md`

### FastAPI
Indicators:
- FastAPI dependency
- imports from `fastapi`

Load:
- `python.md`
- `fastapi.md`

### Docker
Indicators:
- `Dockerfile*`
- `compose.yml`
- `docker-compose.yml`

Load:
- `docker.md`

### Terraform
Indicators:
- `.tf`
- `.tfvars`
- Terraform lock file

Load:
- `terraform.md`

### AI / LLM
Indicators include dependencies or code using:
- OpenAI-compatible APIs
- Anthropic
- Vertex AI
- Bedrock
- LangChain
- LangGraph
- LiteLLM
- Ollama
- Hugging Face inference
- vector databases
- MCP/tool calling

Load:
- `ai-llm.md`

### GitHub Actions
Indicator:
- `.github/workflows/*.yml`

Load:
- `github-actions.md`

### Node / TypeScript
Any of:
- `package.json`
- `tsconfig.json`

Load:
- `node-typescript.md`

### Stacks without a dedicated profile

Common indicators with no profile yet:

- Go: `go.mod`
- Rust: `Cargo.toml`

For these and any other undetected stack, apply only the generic references (git workflow, testing policy, documentation standard, security policy) plus the ecosystem's own mainstream conventions. If the same stack recurs across repositories, propose a new profile via `workflows/improve-skill.md`.

## Rule

Load only relevant profiles.

Existing repository conventions win when they are mature, coherent, and safe.

Profiles are guidance, not an excuse to rewrite healthy code.
