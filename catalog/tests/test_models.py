from datetime import date
import uuid

from django.test import TestCase
from django.template.defaultfilters import slugify

from catalog.models import Content


class ContentModelTest(TestCase):
    """Test Content model."""

    @classmethod
    def setUpTestData(cls):
        """Setup a content image with related objects."""

        pass
