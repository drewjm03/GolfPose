_base_ = ['./golfpose_golfer_ViTPose_huge.py']

metainfo = dict(
    # Path is relative to your project root (e.g. /content/GolfCoach)
    from_file='third_party/golfpose/configs/mmpose/_base_/datasets/golfswing_golfer.py'
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

