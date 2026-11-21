import pytest
import math
from media import audio_splice_click as mod

CASES = [
    ("power", 'm.equal_power(0.5) == approx((0.7071, 0.7071), abs=1e-3)'),
    ("phase", 'm.phase_align(2, 2) == 2'),
    ("dc", 'm.dc_offset([1, 3]) == approx(2.0)'),
    ("warm", 'm.resample_warmup(8) == 8'),
    ("round", 'm.sample_round(10, 48000) == 480'),
    ("loop", 'm.loop_diff(0.5, 0.5) == 0'),
    ("norm", 'm.normalize_after(0.5, 1) == approx(2.0)'),
    ("rate", 'm.unify_rate([44100, 48000]) == 48000'),
    ("fade", 'm.fade_curve(0.5, "linear") == approx(0.5)'),
    ("preroll", 'm.preroll_cut(3) == 2'),
    ("index", 'm.splice_index(10, 48000) == 480'),
    ("delta", 'm.click_delta(0.1, 0.3) == approx(0.2)'),
    ("key", 'm.audio_key(3, 2) == "3:2"'),
    ("gain", 'm.apply_gain(2, 0.5) == approx(1.0)'),
    ("disc", 'm.is_discontinuity(0.3, 0.1) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
