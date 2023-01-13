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


def prompt_with_default(prompt: str, default: str) -> str:
    """
    @param prompt
    @param default
    @return: answer
    @rtype: str
    """
    # If default is None
    if default is None:
        # Return input
        prompt = prompt + ': '
    else:
        prompt = prompt + ' [' + default + ']: '

    answer = input(prompt).strip()
    if not answer:
        return default
    return answer
