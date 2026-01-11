import os

_base_ = ['./golfpose_golfer_ViTPose_huge.py']

# Ensure metainfo.from_file is resolved relative to this config file, not CWD.
_THIS_DIR = os.path.dirname(__file__)
metainfo = dict(
    from_file=os.path.join(_THIS_DIR, '_base_', 'datasets', 'golfswing_golfer.py')
)

# Inference-only config:
# - Same model as training
# - Forces heatmap output
# - Disables flip test for speed and to reduce multi-peak artifacts
model = dict(
    test_cfg=dict(
        flip_test=False,
        flip_mode='heatmap',
        shift_heatmap=False,
        output_heatmaps=True,
    )
)

