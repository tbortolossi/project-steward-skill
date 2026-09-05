# Profile: AI / LLM Application

Apply when the project integrates LLM APIs, local models, agents, RAG, embeddings, tool calling, MCP, or AI gateways.

## Model abstraction

Avoid coupling core application logic unnecessarily to one model/provider.

Document:

- provider;
- model;
- fallback behavior;
- timeout;
- retry policy;
- token/context limits;
- cost-sensitive operations.

## Prompt management

Treat prompts as versioned application logic.

For important prompts:

- store them predictably;
- review changes;
- test representative cases;
- avoid embedding secrets;
- document purpose and expected behavior.

## Agent/tool security

Treat model output as untrusted.

Before tool execution:

- validate arguments;
- enforce authorization;
- constrain filesystem/network access;
- apply least privilege;
- protect destructive actions;
- log meaningful decisions without leaking secrets.

Never let model text directly become privileged shell commands without controls.

## Prompt injection

For applications consuming external content:

- assume retrieved/user-provided text may contain hostile instructions;
- separate trusted system policy from untrusted content;
- limit tool authority;
- validate actions independently of model claims.

## RAG

Document:

- embedding model;
- chunking strategy;
- retrieval strategy;
- reranking;
- metadata filters;
- source attribution;
- freshness/update strategy.

Test retrieval quality separately from generation quality.

## Evaluation

For important workflows, maintain evaluation cases for:

- expected answers;
- refusal/security behavior;
- tool selection;
- hallucination risk;
- regression across model changes.

## Cost and reliability

Consider:

- token budgets;
- caching;
- retry/backoff;
- provider rate limits;
- timeout behavior;
- model fallback;
- observability;
- denial-of-wallet/resource abuse.

## Privacy

Do not send secrets, credentials, or sensitive data to external model providers unless explicitly allowed by project policy.
