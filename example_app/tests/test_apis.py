import json
import os
import pathlib

import pytest
from django.conf import settings
from django.urls import reverse
from hamcrest import assert_that
from rest_framework import status
from rest_framework.test import APIClient

from core.tests import helpers


class TestExample:
    pytestmark = pytest.mark.django_db(reset_sequences=True)

    def setup(self):
        self.client = APIClient()
        self.user = helpers.create_user()
        self.path_data = os.path.relpath(pathlib.Path(__file__).resolve().parent, start=settings.BASE_DIR)

    def test_api_create_example(self):
        self.client.force_authenticate(self.user)
        inp, out = helpers.import_yml_folder(self.path_data, 'test_api_create_example')
        api = reverse(inp.api_name)
        response = self.client.post(api, data=inp.data)
        assert response.status_code == status.HTTP_201_CREATED
        response_data = json.loads(response.content)
        assert_that(response_data, out.results)
