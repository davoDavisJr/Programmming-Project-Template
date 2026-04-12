# ============================================================
# MARIE WORKFLOW
# ============================================================

MARIE_ROOT ?= /c/Users/dovid/.MARIE
MARIE_SRC  ?= src/main.mas

.PHONY: marie-check marie-dev marie-build marie-open clean

marie-check:
	@test -f "$(MARIE_SRC)" || (echo "Missing MARIE source: $(MARIE_SRC)" && exit 1)
	@test -d "$(MARIE_ROOT)" || (echo "Missing MARIE.js clone: $(MARIE_ROOT)" && exit 1)

marie-dev: marie-check
	cd "$(MARIE_ROOT)" && npm install && npx grunt bar-dev

marie-build: marie-check
	cd "$(MARIE_ROOT)" && npm install && npx grunt

marie-open: marie-check
	explorer.exe "$(MARIE_SRC)"
