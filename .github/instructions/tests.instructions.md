---
applyTo: "tests/**/*.py"
---
# Test rules
- Use pytest, not unittest.
- Name tests test_<function>_<scenario>, for example test_validate_username_too_short.
- Use pytest.mark.parametrize when testing several inputs.
- Each test checks one behavior.
- Do not call the network or read real files.
