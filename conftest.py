# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application

fixture = None

#это значок инициализатора фикстуры. Раньше оно лежало в файле Test_add_group.py, но в Лекц 2_03 tuj gthtytcnb d afqk сщтаеуыеюзн
# запись (scope = "session") рзначает что все тесты запускать в одном браузере, а не каждый раз входить=
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin ():
        fixture.session.logout()
        fixture.destroy()
    #указание как фикстура д.б. разрушена
    request.addfinalizer(fin)
    return fixture