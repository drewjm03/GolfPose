_base_ = ['./golfswing_vitpose_huge_kps22_train.py']  # TODO: point this at your actual training config

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

