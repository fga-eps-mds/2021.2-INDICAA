import pytest
from django.test import TestCase
from scraping.QtdeAlunosMatriculados import main
from pytest_mock import MockerFixture
from .mocks import SCRAPING

class TestScraping(TestCase):
    def test_fga():
        faculdade_do_gama = main()
        assert faculdade_do_gama == SCRAPING
