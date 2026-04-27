def recalculate_thresholds(
    initial_stake,
    current_stake,
    win_threshold,
    loss_threshold
):
    win_ratio = win_threshold / current_stake
    loss_ratio = loss_threshold / current_stake

    return (
        round(initial_stake * win_ratio, 2),
        round(initial_stake * loss_ratio, 2)
    )