import tkinter
import random
from questions import questions


class App:
    '''Приложение'''
    def __init__(self, shuffle_questions=False) -> None:
        self.window = tkinter.Tk()
        self.window.option_add('*Font', ('Arial', 30))
        self.window.bind('<Escape>', lambda _: self.window.destroy())
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.window.geometry(f'{screen_width}x{screen_height}')
        self.main_frame = tkinter.Frame(self.window)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')
        self.quiestion_index = 0
        self.right_anwers = 0
        self.wrong_anwers = 0
        self.shuffle_questions = shuffle_questions
        self.start()
        self.window.mainloop()

    def clear(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def start(self) -> None:
        self.clear()
        self.quiestion_index = 0
        self.right_anwers = 0
        self.wrong_anwers = 0
        if self.shuffle_questions:
            random.shuffle(questions)
        self.show_question()

    def show_question(self) -> None:
        question = questions[self.quiestion_index]
        tkinter.Label(self.main_frame, text=question['вопрос']).pack()
        for answer in question['ответы']:
            tkinter.Button(
                self.main_frame,
                text=answer,
                command=lambda arg=answer: self.on_button(arg),
            ).pack(side='left', padx=60, pady=60)

    def on_button(self, button_text) -> None:
        self.clear()
        question = questions[self.quiestion_index]
        if button_text == question['индекс правильного ответа']:
            self.right_anwers += 1
        else:
            self.wrong_anwers += 1

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.quiestion_index += 1
        if self.quiestion_index < len(questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self) -> None:
        '''Показывает результат викторины'''
        tkinter.Label(self.main_frame, 
                      text='Викторина завершена!').pack()
        tkinter.Label(self.main_frame, 
                      text=f'Всего вопросов: {len(questions)}').pack()
        tkinter.Label(self.main_frame, 
                      text=f'Правильных ответов: {self.right_anwers}').pack()
        tkinter.Label(self.main_frame, 
                      text=f'Ошибок: {self.wrong_anwers}').pack()
        tkinter.Button(self.main_frame, text='начать заново', 
                       command=self.start).pack()


App(shuffle_questions=True)
