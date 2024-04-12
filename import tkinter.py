import tkinter

def on_click(*event):
    label_1['bg'] = 'gold'
    label_1['text'] = 'победа'

def color_window(*event):
    window['bg'] = 'seashell'

# виджет - window + gadget
#типы - 1) контент, 2) контейнер


window = tkinter.Tk() # создание окна
window.geometry('1200x900') # задаем размер окна
window.title('приложение') # задали заголовок
window.option_add("*Font", "Arial 60")

label_1 = tkinter.Label(window, text='нажми')
label_1.bind('<Button 1>', on_click)
button = tkinter.Button(
    window, text='не нажимай', borderwidth= 20, command =on_click
    )
label_1.pack(expand=False)
button.pack(expand=True)
label_1['bg'] = 'green'
label_1['padx'] = 30
label_1['pady'] = 17
button['bg'] = 'red'
window['bg'] = 'salmon'
window.bind('<Up>', color_window)
window.mainloop() # всегда последний
