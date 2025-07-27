FROM python:3.12-slim-bookworm AS base

FROM base AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

WORKDIR /code

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

COPY src /code/

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

FROM base

COPY --from=builder /code /code

ENV PATH="/code/.venv/bin:$PATH"

COPY bin ./bin/
RUN chmod 777 /bin/entrypoint.sh

EXPOSE 8100

ENTRYPOINT ["/entrypoint.sh"]