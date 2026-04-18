# Opportunities for Improvement

Ideas and enhancements identified during development that are not urgent enough to act on now. Review before starting new architectural work — an OFI may become relevant.

---

## Programmatic Link Opportunity Scanner

**Context:** As manual content grows, pages accumulate natural-language mentions of other pages that could be wiki links. Manually auditing for missed link opportunities is tedious.

**Idea:** Extend `wikiCheck` with a `--link-opportunities` mode. The tool would:
1. Maintain a manually curated keyword map (slug → natural-language phrases, e.g., `landing-gear-nose` → ["nose gear", "nosewheel"])
2. Scan all WR pages for unlinked mentions of those phrases
3. Report candidate locations for the Writer to review

The keyword map could live as YAML/JSON in the AR. The scanning logic belongs in `tools/wikiCheck/`.

**Why deferred:** Manual is early in content development. Benefit increases as page count grows. Not worth building until there is enough content to make false positives manageable.
