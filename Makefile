MARIE_ROOT ?= $(HOME)/.MARIE
MARIE_SRC ?= src/main.mas

.PHONY: marie-check marie-open marie-root clean

marie-check:
	@test -f "$(MARIE_SRC)" || (echo "Missing MARIE source: $(MARIE_SRC)" && exit 1)
	@test -d "$(MARIE_ROOT)" || (echo "Missing MARIE_ROOT: $(MARIE_ROOT). Set MARIE_ROOT to your local simulator folder." && exit 1)
	@echo "MARIE setup looks ready."

marie-root:
	@echo "$(MARIE_ROOT)"

marie-open:
	@echo "Open $(MARIE_SRC) in your MARIE simulator."

clean:
	@echo "No generated MARIE build output to clean."
