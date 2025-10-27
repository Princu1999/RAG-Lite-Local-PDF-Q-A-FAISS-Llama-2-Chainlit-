import shutil
import subprocess
import sys
from pathlib import Path

def test_ingest_smoke(tmp_path):
    db_path = Path("vectorstore/db_faiss")
    if db_path.exists():
        shutil.rmtree(db_path)
    result = subprocess.run([sys.executable, "ingest.py"], capture_output=True, text=True)
    assert result.returncode == 0
    assert db_path.exists(), "FAISS DB path was not created"
