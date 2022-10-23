import allure
from allure_commons.types import Severity

def test_dynamic_lables():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозитоории')
    allure.dynamic.story('неавторизованный пользователь может создать задачу в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')
    pass


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'eroshenkoam')
@allure.feature('Задачи в репозитоории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_decorator_lables():
    pass

