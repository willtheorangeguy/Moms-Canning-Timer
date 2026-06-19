"""Tests for the GUI-free TimerState countdown logic."""

import unittest

from moms_canning_timer.state import (
    MAX_MINUTES,
    MIN_MINUTES,
    SECONDS_PER_MINUTE,
    TimerState,
)


class TestTimerState(unittest.TestCase):
    """Behaviour of a single timer's countdown."""

    def test_set_minutes_sets_total(self):
        state = TimerState()
        state.set_minutes(5)
        self.assertEqual(state.total_seconds, 5 * SECONDS_PER_MINUTE)
        self.assertEqual(state.remaining_seconds, 5 * SECONDS_PER_MINUTE)

    def test_set_minutes_clamps_range(self):
        state = TimerState()
        state.set_minutes(0)
        self.assertEqual(state.total_seconds, MIN_MINUTES * SECONDS_PER_MINUTE)
        state.set_minutes(9999)
        self.assertEqual(state.total_seconds, MAX_MINUTES * SECONDS_PER_MINUTE)

    def test_start_runs(self):
        state = TimerState(1)
        state.start()
        self.assertTrue(state.running)
        self.assertFalse(state.finished)

    def test_tick_decrements(self):
        state = TimerState(1)
        state.start()
        self.assertFalse(state.tick())
        self.assertEqual(state.remaining_seconds, SECONDS_PER_MINUTE - 1)

    def test_tick_when_not_running_is_noop(self):
        state = TimerState(1)
        self.assertFalse(state.tick())
        self.assertEqual(state.remaining_seconds, SECONDS_PER_MINUTE)

    def test_tick_to_zero_finishes_once(self):
        state = TimerState(1)
        state.start()
        results = [state.tick() for _ in range(SECONDS_PER_MINUTE)]
        self.assertEqual(state.remaining_seconds, 0)
        self.assertTrue(state.finished)
        self.assertFalse(state.running)
        # Exactly one tick reports completion.
        self.assertEqual(results.count(True), 1)
        self.assertTrue(results[-1])
        # Further ticks do not re-fire.
        self.assertFalse(state.tick())

    def test_pause_stops_ticking(self):
        state = TimerState(1)
        state.start()
        state.tick()
        state.pause()
        self.assertFalse(state.running)
        remaining = state.remaining_seconds
        self.assertFalse(state.tick())
        self.assertEqual(state.remaining_seconds, remaining)

    def test_resume_continues(self):
        state = TimerState(1)
        state.start()
        state.pause()
        state.resume()
        self.assertTrue(state.running)
        self.assertTrue(state.tick() is False)

    def test_reset_restores_full_duration(self):
        state = TimerState(1)
        state.start()
        for _ in range(5):
            state.tick()
        state.reset()
        self.assertEqual(state.remaining_seconds, state.total_seconds)
        self.assertFalse(state.running)
        self.assertFalse(state.finished)

    def test_fraction_done_endpoints(self):
        state = TimerState(1)
        state.start()
        self.assertAlmostEqual(state.fraction_done(), 0.0)
        for _ in range(SECONDS_PER_MINUTE):
            state.tick()
        self.assertAlmostEqual(state.fraction_done(), 1.0)

    def test_display_formatting(self):
        state = TimerState(15)
        self.assertEqual(state.display(), "15:00")
        state.start()
        state.tick()
        self.assertEqual(state.display(), "14:59")


if __name__ == "__main__":
    unittest.main()
