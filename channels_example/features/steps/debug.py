from aloe import step


@step(r"pause for a debugging session")
def pause_debug(self):
    """Wait for a key to be pressed for debugging."""

    print("Press Enter to continue...")
    input()
