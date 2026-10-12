from pathlib import Path
import sys
root = Path(__file__).resolve().parents[1]
workflow = (root / '.github/workflows/rea-free-manual.yml').read_text()
checks = {
  'manual_only': 'workflow_dispatch:' in workflow and '  push:' not in workflow,
  'read_only': '  contents: read' in workflow,
  'no_credentials': 'persist-credentials: false' in workflow,
  'synthetic_target': (root / 'targets/fixture-app/src/pricing.js').is_file(),
  'pinned_version': "REA_VERSION: '6.4.0'" in workflow,
  'public_only': 'repository.private' in workflow,
  'bounded_time': 'timeout-minutes: 25' in workflow,
  'macos_intel': 'macos-15-intel' in workflow
}
for key, valid in checks.items():
    print(key, 'PASS' if valid else 'FAIL')
print(f"{sum(checks.values())}/{len(checks)} checks passed")
sys.exit(0 if all(checks.values()) else 1)
