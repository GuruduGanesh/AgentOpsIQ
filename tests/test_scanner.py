import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from agentopsiq.cli import scan_path  # noqa: E402


class ScannerFixtureTests(unittest.TestCase):
    def fixture(self, name: str) -> Path:
        return ROOT / "tests" / "fixtures" / name

    def test_passing_fixture_has_no_findings(self):
        report = scan_path(self.fixture("passing"))

        self.assertEqual(report["score"], 100)
        self.assertEqual(report["finding_count"], 0)

    def test_missing_resource_limits_fixture_reports_kubernetes_gaps(self):
        report = scan_path(self.fixture("missing-resource-limits"))
        finding_ids = {finding["id"] for finding in report["findings"]}

        self.assertIn("AOP-CHK-001", finding_ids)
        self.assertIn("AOP-CHK-002", finding_ids)
        self.assertIn("AOP-CHK-003", finding_ids)
        self.assertIn("AOP-CHK-004", finding_ids)
        self.assertIn("AOP-CHK-005", finding_ids)
        self.assertIn("AOP-CHK-006", finding_ids)
        self.assertLess(report["score"], 100)

    def test_missing_otel_exporter_fixture_reports_observability_gaps(self):
        report = scan_path(self.fixture("missing-otel-exporter"))
        finding_ids = {finding["id"] for finding in report["findings"]}

        self.assertIn("AOP-CHK-007", finding_ids)
        self.assertIn("AOP-CHK-008", finding_ids)
        self.assertLess(report["score"], 100)


if __name__ == "__main__":
    unittest.main()
