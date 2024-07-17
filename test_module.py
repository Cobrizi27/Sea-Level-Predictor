import unittest
from sea_level_predictor import draw_plot
import matplotlib as mpl

class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_plot(self):
        ax = draw_plot()
        self.assertIsInstance(ax, mpl.axes.Axes)
        self.assertEqual(ax.get_title(), 'Rise in Sea Level')
        self.assertEqual(ax.get_xlabel(), 'Year')
        self.assertEqual(ax.get_ylabel(), 'Sea Level (inches)')

if __name__ == "__main__":
    unittest.main()
