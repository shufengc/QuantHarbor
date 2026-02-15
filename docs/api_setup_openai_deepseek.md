# API Setup: OpenAI and DeepSeek

This document explains how to obtain API keys, configure this project, and verify connectivity.

## 1) Obtain Keys

### OpenAI
- Go to `https://platform.openai.com/`
- Create an account and open API settings
- Generate a new API key
- Copy and store it securely

### DeepSeek
- Go to `https://platform.deepseek.com/`
- Create an account and open API key settings
- Generate a new API key
- Copy and store it securely

## 2) Configure Environment

From project root:

```bash
cp .env.example .env
```

Fill these variables:

```bash
PRIMARY_PROVIDER=openai
FALLBACK_PROVIDER=deepseek

OPENAI_API_KEY=...
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_CHAT_MODEL=gpt-4o-mini
OPENAI_EMBED_MODEL=text-embedding-3-small

DEEPSEEK_API_KEY=...
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
DEEPSEEK_CHAT_MODEL=deepseek-chat
DEEPSEEK_EMBED_MODEL=
```

If you already have valid OpenAI and DeepSeek keys, paste them directly into `.env` values above.

## 3) Provider Behavior

- Chat generation:
  - Uses `PRIMARY_PROVIDER` first.
  - Falls back to `FALLBACK_PROVIDER` if enabled and available.

- Embeddings:
  - Uses provider-specific embedding model when configured.
  - If DeepSeek embedding model is not configured, it falls back to OpenAI embeddings.

## 4) Provider Modes

### OpenAI only

```bash
PRIMARY_PROVIDER=openai
FALLBACK_PROVIDER=openai
```

### DeepSeek only

```bash
PRIMARY_PROVIDER=deepseek
FALLBACK_PROVIDER=deepseek
```

### Auto fallback

```bash
PRIMARY_PROVIDER=openai
FALLBACK_PROVIDER=deepseek
```

## 5) Connectivity Test

```bash
python3 scripts/smoke_test_providers.py --provider openai
python3 scripts/smoke_test_providers.py --provider deepseek
python3 scripts/smoke_test_providers.py --provider auto
```

Expected result:
- successful model response preview
- successful embedding vector dimension output

## 6) Common Errors

- `Missing OPENAI_API_KEY` or `Missing DEEPSEEK_API_KEY`
  - Add keys to `.env`

- `401 Unauthorized`
  - Key is invalid, expired, or belongs to a different project/account

- `404 model not found`
  - Model name is not available in your account/region

- `429 rate limit`
  - Reduce request volume or add retry logic

## 7) Security

- Never commit `.env`
- Rotate keys if exposed
- Use per-environment keys (dev/staging/prod)
