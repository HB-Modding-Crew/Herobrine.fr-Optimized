def confirm_yes_or_no(prompt: str) -> bool:
    """
    @param prompt
    @return: confirmation
    @rtype: bool
    """
    prompt = prompt + ' [Y/N]: '
    while True:
        answer = input(prompt).lower().strip()
        if not answer:
            continue
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print('Please answer yes or no.')
