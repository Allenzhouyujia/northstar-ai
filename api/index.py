"""Vercel entry point: serves the FastAPI backend as a Python function at /api/*.

The backend package lives in backend/, so put it on sys.path before importing.
Paths inside northstar.config resolve from the repo root, which Vercel keeps
because vercel.json bundles backend/, datasets/processed/ and experiments/.

Start-up warm-up (precomputing every preset and policy in a background thread)
is off here: on a one-vCPU function it would slow the visitor's own runs and
repeat on every cold start. Runs are computed on demand instead.
"""
import os
import sys
from pathlib import Path

os.environ.setdefault("NORTHSTAR_WARMUP", "0")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from northstar.api.main import app  # noqa: E402,F401
