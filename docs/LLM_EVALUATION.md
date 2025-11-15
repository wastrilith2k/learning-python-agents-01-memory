# LLM API Provider Evaluation

## Decision Context
For Project 1 (Conversational Memory Agent), we need to select an LLM API provider. This document outlines the evaluation criteria, options considered, and final decision with reasoning.

## Evaluation Criteria
1. **Cost** - Token pricing for learning/development use
2. **Learning Value** - Features that teach important concepts
3. **Documentation Quality** - SDK docs and examples
4. **API Simplicity** - Ease of integration for beginners
5. **Advanced Features** - Caching, context management tools

## Providers Evaluated

### OpenAI (GPT-4o, GPT-5 family)
**Pricing:**
- GPT-4o Mini: $0.60/$2.40 per 1M tokens (cheapest OpenAI option)
- GPT-4o: $5/$20 per 1M tokens
- GPT-5 Mini: $0.25/$2.00 per 1M tokens

**Pros:**
- Industry standard, extensive documentation
- Excellent Python SDK
- Wide community support
- Cached input discount (50%)

**Cons:**
- Higher cost than alternatives
- Shorter context windows (32-128K)
- Premium pricing model

**Use Case Fit:** Good for production, but expensive for learning

---

### Anthropic Claude
**Pricing:**
- Claude Haiku 3.5: $0.80/$4.00 per 1M tokens
- Claude Sonnet 4: $3.00/$15.00 per 1M tokens
- Prompt caching: 10x cheaper on repeated prompts (0.1x multiplier)

**Pros:**
- Excellent prompt caching (teaches memory optimization)
- Large context windows (200K standard, 1M beta)
- Strong safety/reliability focus
- Clean, well-documented Python SDK
- Competitive mid-tier pricing

**Cons:**
- Higher than budget options
- Newer player (less community content than OpenAI)

**Use Case Fit:** ⭐ **BEST for learning** - caching teaches optimization, good docs

---

### Google Gemini
**Pricing:**
- Gemini 2.5 Flash: $0.15/$0.60 per 1M tokens (no reasoning)
- Gemini 2.5 Pro: $1.25/$10 per 1M tokens

**Pros:**
- Very cheap (Flash model)
- Massive context (2M tokens)
- Good Google Cloud integration

**Cons:**
- Tiered pricing complexity
- Less Python-focused docs
- Requires Google Cloud account setup

**Use Case Fit:** Good budget option, but setup overhead

---

### DeepSeek (Chinese provider)
**Pricing:**
- V3.2: $0.28/$0.42 per 1M tokens (90% cheaper than competition!)
- Cache hits: $0.028 input

**Pros:**
- Dramatically cheapest option
- Large context (128K)
- Aggressive caching discounts

**Cons:**
- Chinese provider (potential availability/political concerns)
- Less documentation in English
- Smaller community
- Unknown long-term stability

**Use Case Fit:** Great for cost, risky for learning project

---

## Cost Comparison Example
**Scenario:** 100K input tokens + 100K output tokens (typical learning session)

| Provider | Cost per Session | Monthly (30 sessions) |
|----------|-----------------|----------------------|
| GPT-4o Mini | $0.30 | $9.00 |
| GPT-5 Mini | $0.225 | $6.75 |
| Claude Haiku | $0.48 | $14.40 |
| Claude Sonnet | $1.80 | $54.00 |
| Gemini Flash | $0.075 | $2.25 |
| DeepSeek | $0.07 | $2.10 |

---

## Final Decision: **Anthropic Claude (Sonnet 4)**

### Reasoning:

1. **Learning Value (PRIMARY GOAL):**
   - Prompt caching teaches real-world optimization patterns
   - Forces thinking about what to cache vs re-send
   - 200K context window teaches context management
   - These concepts transfer to ANY agent framework

2. **Cost vs Value:**
   - Yes, it's mid-tier pricing ($1.80/session)
   - But we're learning, not running production at scale
   - Monthly cost ~$50 is acceptable for education
   - Can drop to Haiku ($0.48/session) if budget becomes issue

3. **Documentation & SDK:**
   - Anthropic's Python SDK is clean and well-documented
   - Focus on safety = good prompting examples
   - Active development, modern Python practices

4. **Portfolio Value:**
   - Using Claude demonstrates knowledge of multiple providers
   - Caching implementation shows optimization thinking
   - Not just "default to OpenAI"

5. **Future Flexibility:**
   - Can easily swap to OpenAI or others later
   - Learning the concepts matters more than the specific API
   - Claude's approach to safety/context teaches good habits

### Alternative if Cost Becomes Issue:
If monthly costs exceed budget, fallback to **Claude Haiku 3.5** ($0.48/session = $14/month), which maintains all learning benefits at 1/4 the cost of Sonnet.

### Why NOT the Cheapest Option:
DeepSeek is 25x cheaper, but:
- Learning project success depends on good docs/community
- Unknown provider stability risk
- Less transferable knowledge (niche provider)
- Cost savings ($50 vs $2/month) aren't worth the friction

---

## Implementation Notes:
- Start with Claude Sonnet 4 for initial development
- Implement prompt caching from day 1 (learn optimization early)
- Monitor token usage to understand real costs
- Document caching strategy decisions
- Can migrate to cheaper tier after core concepts proven

**Cost estimate for Project 1 completion: $50-100** (acceptable for portfolio project)

---

*Last Updated: November 2025*
*Sources: IntuitionLabs LLM Pricing Comparison 2025, official provider documentation*