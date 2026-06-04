#! /bin/bash
if [ -f .coverage ]; then
  rm .coverage
fi

python -m pytest tests/unit \
--cov \
--cov-fail-under=60 \
--cov-report=html:htmlcov
