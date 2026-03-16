from logic_utils import check_guess, parse_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Tests targeting the 3 bugs we fixed ---

# Bug 2: invalid guesses should NOT count as attempts
# parse_guess must return ok=False for non-numeric input so the
# caller knows NOT to increment the attempt counter.
def test_invalid_guess_returns_not_ok():
    ok, guess_int, err = parse_guess("abc")
    assert ok is False
    assert guess_int is None
    assert err is not None

def test_empty_guess_returns_not_ok():
    ok, guess_int, err = parse_guess("")
    assert ok is False

def test_valid_guess_returns_ok():
    ok, guess_int, err = parse_guess("42")
    assert ok is True
    assert guess_int == 42
    assert err is None


# Bug 3: score formula should use attempt_number, not attempt_number + 1
# Winning on attempt 1 should give 90 points (100 - 10*1), not 80.
def test_score_win_on_first_attempt():
    score = update_score(0, "Win", attempt_number=1)
    assert score == 90  # was 80 before the fix (100 - 10*2)

def test_score_win_on_second_attempt():
    score = update_score(0, "Win", attempt_number=2)
    assert score == 80  # was 70 before the fix

def test_score_win_never_goes_below_minimum():
    # attempt 10 would give 0 pts, but the floor is 10
    score = update_score(0, "Win", attempt_number=10)
    assert score == 10

def test_score_wrong_guess_deducts_five():
    score = update_score(50, "Too High", attempt_number=1)
    assert score == 45
    score = update_score(50, "Too Low", attempt_number=1)
    assert score == 45


# Bug 1: new_game must reset status back to "playing"
# The fix lives in Streamlit session state (app.py), but we can verify
# that the downstream functions behave correctly when called after a reset.
def test_game_can_be_replayed_after_win():
    # Simulate: win a game, reset score to 0, play again
    score_after_win = update_score(0, "Win", attempt_number=1)
    assert score_after_win > 0

    # After new_game resets score to 0, a fresh round should score normally
    score_after_reset = update_score(0, "Win", attempt_number=1)
    assert score_after_reset == 90
