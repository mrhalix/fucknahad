import requests
import json
class FuckNahad():
    """
    This class is written from stolen API endpoints at maaref.ecnahad.ir.
    using functions written below you can pass every exam you want with the grade of 20 !
    """
    def __init__(self, auth_token) -> None:
        """
        Inits the class using JWT authentication token

        :param auth_token: your authentication token to access quizes, courses and etc.
        :type auth_token: :obj:`str`
        """
        self.token = auth_token
    def get_lesson(self, lessonID : str):
        """
        Gets every information from the given lessonID.
        Refer to "apiExamples/user-sections-115.json" for more information about the API Response.

        :param lessonID: lesson id to get lesson sections.
        :type lessonID: :obj:`str`
        :return: lesson sections
        :rtype: :obj:`dict`
        """

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Authorization': self.token,
            'Connection': 'keep-alive',
            'Origin': 'https://maaref.ecnahad.ir',
            'Referer': 'https://maaref.ecnahad.ir/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.get('https://lesson.faragiran.net/api/lessons/user/sections/' + str(lessonID), headers=headers).text
        return json.loads(response)

    def start_quiz(self, courseID : str, quizID : str):
        """
        Starts a quiz and returns the quiz information in order to receive questions
        Refer to "apiExamples/grade-quiz-start-116.json" for more information about the API Response.

        :param courseID: course id the quiz is underneath.
        :type courseID: :obj:`str`
        :param quizID: quiz id to start.
        :type quizID: :obj:`str`
        :return: quiz information
        :rtype: :obj:`dict
        """
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Authorization': self.token,
            'Connection': 'keep-alive',
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'Origin': 'https://maaref.ecnahad.ir',
            'Referer': 'https://maaref.ecnahad.ir/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
        'courseId': courseID,
        }

        response = requests.post('https://quiz.faragiran.net/api/grade/quiz-start/' + quizID, headers=headers, json=json_data).text
        return json.loads(response)

    def start_attempt(self, attemptID : str):
        """
        Starts an attempt and returns the quiz questions and options.
        Refer to "apiExamples/grade-attempt-start-attemptID.json" for more information about the API Response.

        :param attemptID: attempt id to get quiz questions. you have to get this from start_quiz()
        :type attemptID: :obj:`str`
        :return: attempt information
        :rtype: :obj:`dict
        """
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Authorization': self.token,
            'Connection': 'keep-alive',
            # 'Content-Length': '0',
            'Origin': 'https://maaref.ecnahad.ir',
            'Referer': 'https://maaref.ecnahad.ir/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.post('https://quiz.faragiran.net/api/grade/attempt-start/' + str(attemptID), headers=headers).text
        return json.loads(response)

    def send_answer(self, questionID : str, answerID : int):
        """
        simulates the action of selecting an option when doing the exam in browser, and submits the answer to the question.
        Refer to "apiExamples/grade-update-answers-182474446.json" for more information about the API Response.

        :param questionID: came from start_attempt()
        :type questionID: :obj:`str`
        :param answerID: came from start_attempt()
        :type answerID: :obj:`int`
        :return: submitted information
        :rtype: :obj:`dict
        """
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Authorization': self.token,
            'Connection': 'keep-alive',
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'Origin': 'https://maaref.ecnahad.ir',
            'Referer': 'https://maaref.ecnahad.ir/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        json_data = {
            'option_id': int(answerID),
        }

        response = requests.post('https://quiz.faragiran.net/api/grade/update-answers/' + str(questionID), headers=headers, json=json_data).text
        return json.loads(response)
    
    def end_quiz(self, quizID : str):
        """
        Finishes the quiz.
        Refer to "apiExamples/grade-quiz-finish-119.json" for more information about the API Response.

        :param quizID: quiz id to finish.
        :type quizID: :obj:`str`
        :return: submitted information
        :rtype: :obj:`dict
        """
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
            'Authorization': self.token,
            'Connection': 'keep-alive',
            # 'Content-Length': '0',
            'Origin': 'https://maaref.ecnahad.ir',
            'Referer': 'https://maaref.ecnahad.ir/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        response = requests.post('https://quiz.faragiran.net/api/grade/quiz-finish/' + str(quizID), headers=headers).text
        return json.loads(response)

nahad = FuckNahad('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozMDgxNjAyLCJleHAiOjE2NjAzNzgwNjd9.Bu0YL8BVNY0LUsPdlkeM8GkAeOw-mYUutcgpuaXKl-I')
courseID = input("Enter Course ID: ") # Example: 49356 -- must be str
quizID = input("Enter Quiz ID: ") # Example: 119 -- must be str
print("Starting Quiz", quizID, "...")
quiz_info = nahad.start_quiz(courseID=courseID, quizID=quizID)
print("Starting Attempt...")
attempt = nahad.start_attempt(quiz_info['data']['attempt']['id'])
qcounter = 0
questions = attempt['data']
for question in questions:
    acounter = 0
    qcounter += 1
    print("Doing Question No. ", qcounter)
    qid = question['id']
    print(qid)
    for option in question['question']['options']:
        acounter += 1
        print("Checking option", acounter, "from quiz no.", qcounter)
        answer_result = nahad.send_answer(questionID=qid, answerID=option['id'])
        if answer_result['data']['option'][0]['is_correct'] == 1:
            print(answer_result['data']['option'][0]['body'])
            print("Found Answer, Done.")
            break
print("Questions are over, Ending quiz...")
results = nahad.end_quiz(quizID=quizID)
print("Grade:", results['data']['grade'])