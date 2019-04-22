# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

#это значок инициализатора фикстуры. Раньше оно лежало в файле Test_add_group.py, но в Лекц 2_03 tuj gthtytcnb d afqk сщтаеуыеюзн
# запись (scope = "session") рзначает что все тесты запускать в одном браузере, а не каждый раз входить=
@pytest.fixture(scope = "session")
def app(request):
    #инициализация создания фикстуры
    fixture = Application()
    #указание как фикстура д.б. разрушена
    request.addfinalizer(fixture.destroy)
    return fixture