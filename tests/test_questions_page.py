import pytest
import allure
from pages.questions_page import QuestionsPage
from conftest import QUESTIONS_AND_ANSWERS


@allure.suite('Test suite to check QA')
class TestQuestionPage:

    @allure.title('Open a dropdown menu of a question and check that the answer matches.')
    @pytest.mark.parametrize('question, answer', QUESTIONS_AND_ANSWERS)
    def test_answer_matches_question_true(self, driver, question, answer):
        page = QuestionsPage(driver)
        page.accept_cookies()
        page.find_question(question)
        page.find_answer(answer)
