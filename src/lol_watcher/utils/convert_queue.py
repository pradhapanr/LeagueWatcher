queue_dict = {
    'blind': 430,
    'draft': 400,
    'solo': 420,
    'flex': 440,
    'aram': 450,
}


def queue_to_int(queue: str) -> int:
    if queue not in queue_dict:
        raise ValueError(
            'Queue name invalid. Refer to docs for more info about this endpoint.')
    return queue_dict[queue]
