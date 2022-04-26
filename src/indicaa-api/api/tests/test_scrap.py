import pytest
from django.test import TestCase
from scraping.QtdeAlunosMatriculados import main
from .mocks.scraping import SCRAPING

class TestScraping(TestCase):
    def test_fga(self):
        faculdade_do_gama = main()
        assert faculdade_do_gama == SCRAPING