_base_ = ['./golfpose_golfer_ViTPose_huge.py']

metainfo = dict(
    # Path is relative to this config file's directory (configs/mmpose)
    from_file='_base_/datasets/golfswing_golfer.py'
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

