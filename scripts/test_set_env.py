"""Tests for set_env.py. Run with: python -m unittest discover -s scripts -p 'test_*.py'"""

import contextlib
import io
import stat
import tempfile
import unittest
from pathlib import Path

import set_env


class SetEnvTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.env = Path(self.dir.name) / ".env"

    def tearDown(self):
        self.dir.cleanup()

    def run_cli(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = set_env.main(["--file", str(self.env), *args])
        return code, out.getvalue(), err.getvalue()

    def test_adds_replaces_and_keeps_everything_else(self):
        self.env.write_text("# comment\nANTHROPIC_API_KEY=sk-ant-xyz\nREGION=eu\nREGION=us\n# REGION=old\n")
        code, out, _ = self.run_cli("REGION=global", "PROJECT=lab-1")
        self.assertEqual(code, 0)
        self.assertEqual(out, "REGION replaced\nPROJECT added\n")
        self.assertEqual(
            self.env.read_text(),
            "# comment\nANTHROPIC_API_KEY=sk-ant-xyz\nREGION=global\n# REGION=old\nPROJECT=lab-1\n",
        )

    def test_never_prints_values(self):
        self.env.write_text("ANTHROPIC_API_KEY=sk-ant-secret\n")
        _, out, err = self.run_cli("--check", "ANTHROPIC_API_KEY", "MISSING")
        self.assertEqual(out, "ANTHROPIC_API_KEY set\nMISSING -\n")
        self.assertNotIn("sk-ant-secret", out + err)
        _, out, err = self.run_cli("REGION=global")
        self.assertNotIn("sk-ant-secret", out + err)

    def test_refuses_secret_names_but_accepts_paths_to_them(self):
        for item in ("ANTHROPIC_API_KEY=x", "CLAUDE_CODE_OAUTH_TOKEN=x", "DB_PASSWORD=x", "GCP_SA_KEY=x"):
            code, _, err = self.run_cli(item)
            self.assertEqual(code, 2, item)
            self.assertIn("names a secret", err)
        code, _, _ = self.run_cli("GCP_SA_KEY_FILE=secrets/sa.json", "GOOGLE_APPLICATION_CREDENTIALS=/k.json")
        self.assertEqual(code, 0)

    def test_refuses_secret_looking_values(self):
        for value in ("sk-ant-api03-abc", "ghp_abc", "eyJhbGciOi", "-----BEGIN KEY", '{"type": "x"}', "a" * 48):
            code, _, err = self.run_cli(f"SOME_SETTING={value}")
            self.assertEqual(code, 2, value)
            self.assertIn("looks like", err)
        self.assertFalse(self.env.exists())

    def test_refusal_writes_nothing(self):
        self.env.write_text("A=1\n")
        self.run_cli("B=2", "API_KEY=x")
        self.assertEqual(self.env.read_text(), "A=1\n")

    def test_quotes_values_that_need_it_and_keeps_model_ids_plain(self):
        self.run_cli('MODELS=a b "c"', "MODEL=claude-haiku-4-5@20251001")
        self.assertEqual(
            self.env.read_text(), 'MODELS="a b \\"c\\""\nMODEL=claude-haiku-4-5@20251001\n'
        )

    def test_new_file_is_private_and_existing_mode_is_kept(self):
        self.run_cli("A=1")
        self.assertEqual(stat.S_IMODE(self.env.stat().st_mode), 0o600)
        self.env.chmod(0o640)
        self.run_cli("A=2")
        self.assertEqual(stat.S_IMODE(self.env.stat().st_mode), 0o640)

    def test_appends_after_a_last_line_without_newline(self):
        self.env.write_text("A=1")
        self.run_cli("B=2")
        self.assertEqual(self.env.read_text(), "A=1\nB=2\n")

    def test_unset_removes_the_variable_and_its_comments(self):
        self.env.write_text(
            "# --- Gateway ---\nGCP_PROJECT_ID=p\n# the region\nVERTEX_REGION=global\n"
            "\nANTHROPIC_API_KEY=sk-ant-keep\n\n# kept: blank line above\n\nOTHER=1\n"
        )
        code, out, _ = self.run_cli("--unset", "GCP_PROJECT_ID", "VERTEX_REGION", "NOPE")
        self.assertEqual(code, 0)
        self.assertEqual(out, "GCP_PROJECT_ID removed\nVERTEX_REGION removed\nNOPE absent\n")
        self.assertEqual(
            self.env.read_text(),
            "ANTHROPIC_API_KEY=sk-ant-keep\n\n# kept: blank line above\n\nOTHER=1\n",
        )

    def test_header_titles_the_appended_block_only(self):
        self.env.write_text("A=1\n")
        self.run_cli("--header", "--- Vertex ---", "A=2", "B=3")
        self.assertEqual(self.env.read_text(), "A=2\n\n# --- Vertex ---\nB=3\n")


if __name__ == "__main__":
    unittest.main()
