"""
This module contains common helper functions which would be useful for testing.

WARNING: only use the below functions in test cases, not in actual codes
"""
import os

import yaml
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from mixer.backend.django import mixer
from munch import Munch

User = get_user_model()


def _create_group(**kwargs):
    group_id = kwargs.get('id')
    group_name = kwargs.get('name')
    if group_id:
        try:
            inst = Group.objects.get(pk=group_id)
            inst.name = group_name
            inst.save()
        except Group.DoesNotExist:
            inst = Group.objects.create(**kwargs)
        return inst
    if group_name:
        inst, _ = Group.objects.get_or_create(name=group_name)
        return inst


def create_user(*args, **kwargs):
    """Create a user, by default that user will be approved and completely
    onboarded"""
    kwargs['is_active'] = True
    kwargs['is_approved'] = True
    kwargs['onboarding_step'] = 100

    user = mixer.blend(User, **kwargs)
    return user


def import_yml_folder(yml_folder_path, test_name):
    # read input
    input_data = None
    inp_file_name = os.path.join(settings.BASE_DIR, yml_folder_path, 'inp', '%s.yml' % test_name)
    if os.path.exists(inp_file_name):
        with open(inp_file_name) as f:
            try:
                input_data = Munch(yaml.load(f, Loader=yaml.Loader))
            except yaml.YAMLError as e:
                print(e)
    # read output
    output_data = None
    out_file_name = os.path.join(settings.BASE_DIR, yml_folder_path, 'out', '%s.yml' % test_name)
    if os.path.exists(out_file_name):
        with open(out_file_name) as f:
            try:
                output_data = Munch(yaml.load(f, Loader=yaml.Loader))
            except yaml.YAMLError as e:
                print(e)
    return input_data, output_data
