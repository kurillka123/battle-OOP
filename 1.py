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
        self.start()
        self.window.mainloop()

    def start(self) -> None:
        self.quiestion_index = 0
        self.right_anwers = 0
        self.wrong_anwers = 0   
        random.shuffle(questions)
        self.show_question()

    def show_question(self) -> None:
        question = questions[self.quiestion_index]
        tkinter.Label(self.main_frame, text=question['вопрос']).pack()
        for answer in question['ответы']:
            tkinter.Button(self.main_frame, 
                           text=answer, 
                           command=lambda: self.on_button(answer)
                           ).pack()
        

    def on_button(self, button_text) -> None:
        question = questions[self.quiestion_index]
        if button_text == question['ответ']:
            self.right_answers += 1
        else:
            self.wrong_answers += 1

        for widget in self.main_frame.winfo_children():#возвращает список дочерних видов
            widget.destroy


        self.quiestion_index += 1
        if self.quiestion_index < len(question):
            self.show_question
        else:
            pass



App(shuffle_questions=True)
