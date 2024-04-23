import tkinter
from questions import questions

questions = [
    {
        'вопрос': 'Какой оператор умножает числа в Питоне?',
        'ответы': ['-', 'x', '*', '**'],
        'индекс правильного ответа': 2
    },
    {
        'вопрос': 'Какой из этих типов изменяемый?',
        'ответы': ['list', 'str', 'tuple', 'int'],
        'индекс правильного ответа': 0
    },
]


class App:
    '''Приложение'''
    def __init__(self) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Arial', 30))
        self.window.bind('<Escape>', self.quit)
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_height}')
        self.questions_frame = None
        self.results_frame = None
        self.make_widgets()
        self.position_widgets()
        self.quiestion_index = 0
        self.right_anwers = 0
        self.wrong_anwers = 0
        self.show_question()
        self.window.mainloop()

    def quit(self, event: tkinter.Event) -> None:
        self.window.destroy()


    def make_widgets(self) -> None:
        '''Cоздание всех виджетов'''
        self.questions_frame = tkinter.Frame(self.window)
        self.question_text = tkinter.Label(self.questions_frame)
        self.question_answer_1 = tkinter.Label(self.questions_frame)
        self.question_answer_2 = tkinter.Label(self.questions_frame)
        self.question_answer_3 = tkinter.Label(self.questions_frame)
        self.question_answer_4 = tkinter.Label(self.questions_frame)
        self.buttons_frame = tkinter.Frame(self.questions_frame)
        self.anwer_button_1 = tkinter.Button(
            self.buttons_frame, text='1', command=lambda: self.on_click(0)
        )
        self.anwer_button_2 = tkinter.Button(
            self.buttons_frame, text='2', command=lambda: self.on_click(1)
        )
        self.anwer_button_3 = tkinter.Button(
            self.buttons_frame, text='3', command=lambda: self.on_click(2)
        )
        self.anwer_button_4 = tkinter.Button(
            self.buttons_frame, text='4', command=lambda: self.on_click(3)
        )
        

    def position_widgets(self) -> None:
        '''Позиционирование всех виджетов'''
        self.questions_frame.pack(expand=True)
        self.question_text.pack(pady=(0, 50))
        self.question_answer_1.pack()
        self.question_answer_2.pack()
        self.question_answer_3.pack()
        self.question_answer_4.pack()
        self.buttons_frame.pack(pady=50)
        self.anwer_button_1.pack(side='left', padx=20)
        self.anwer_button_2.pack(side='left', padx=20)
        self.anwer_button_3.pack(side='left', padx=20)
        self.anwer_button_4.pack(side='left', padx=20)

    def show_question(self) -> None:
        '''Наполняет виджеты текстами вопроса'''
        question = questions[self.quiestion_index]
        self.question_text['text'] = question['вопрос']
        self.question_answer_1['text'] = '1. ' + question['ответы'][0]
        self.question_answer_2['text'] = '2. ' + question['ответы'][1]
        self.question_answer_3['text'] = '3. ' + question['ответы'][2]
        self.question_answer_4['text'] = '4. ' + question['ответы'][3]

    def on_click(self, button_index: int) -> None:
        '''
        Сравнивает индекс кнопки с индексом правильного ответа.
        Если вопросы не кончились, показывает следующий,
        иначе показыввает результаты
        '''
        question = questions[self.quiestion_index]
        if button_index == question['индекс правильного ответа']:
            self.right_anwers += 1
        else:
            self.wrong_anwers += 1
        if self.quiestion_index + 1 == len(questions):
            self.show_result()
        else:
            self.quiestion_index += 1
            self.show_question()

    def show_result(self) -> None:
        '''Показывает результат викторины'''
        self.questions_frame.pack_forget()
        self.results_frame = tkinter.Frame(self.window)
        self.results_frame.pack()
        tkinter.Label(self.results_frame, text='Викторина завершена!').pack()
        tkinter.Label(self.results_frame, text=f'Всего вопросов: {len(questions)}').pack()
        tkinter.Label(self.results_frame, text=f'Правильных ответов: {self.right_anwers}').pack()
        tkinter.Label(self.results_frame, text=f'Ошибок: {self.wrong_anwers}').pack()
        tkinter.Button(self.results_frame, text='начать заного', command=self.start).pack()

    def start(self) -> None:
        self.quiestion_index = 0
        self.wrong_anwers = 0
        self.right_anwers = 0
        if self.results_frame:
            self.results_frame.pack_forget()
        self.questions_frame.pack()
        self.show_question


App()
