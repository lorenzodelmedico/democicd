import random
import time


def test_confirm_exit(monkeypatch):
    """
    Test the confirm_exit() function by simulating a user input and
    forcing a random outcome that leads to exiting the script.

    In this test:
      - The simulated user input is "n" (i.e. not wanting to exit).
      - We override random.choice() to always return True so that the
        function flips the decision. For input "n", a flip leads to exit.
      - We also override time.sleep() to avoid delays during testing.
    """
    # Simulate input: user types "n"
    inputs = iter(["n"])
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    # Force a flip so that the final decision becomes True (exit)
    monkeypatch.setattr(random, "choice", lambda choices: True)

    # Skip delays in the animation
    monkeypatch.setattr(time, "sleep", lambda seconds: None)

    # Import the function after patching to ensure patches take effect
    # path must be written as democicd.cli because the application is deployed to pypi
    from democicd.cli import confirm_exit

    # Run the function; it should eventually return True (exit)
    result = confirm_exit()
    assert result is True
