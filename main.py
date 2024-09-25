import tkinter as tk
import time
import random

# Function to select a random line of text from a file
def select_text():
    with open('text.txt', 'r') as f:
        lines = f.readlines()
        return random.choice(lines).strip()

# Typing Test class to manage the typing test logic
class Typing_Speed_App:
    
    def __init__(self,root):
        self.root = root
        self.root.title('Typing Speed Test')

        #Variables
        self.target_text = select_text()  # Get random text
        self.current_text = []
        self.start_time = None
        self.wpm = 0


        #GUI Elements
        self.intro_label = tk.Label(root, text="Welcome to Typing Test!", font=('Arial', 16))
        self.intro_label.pack(pady=10)

        self.start_label = tk.Label(root, text="Press Start to begin..!", font=('Arial', 12))
        self.start_label.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)
        
        self.text_label = tk.Label(root, text=self.target_text, font=('Arial', 14),wraplength=500)
        self.text_label.pack(pady=20)
        
        self.entry_text = tk.Entry(root, font=('Arial', 14), width=50)
        self.entry_text.pack()
        self.entry_text.bind('<KeyRelease>',self.key_press)

        self.wpm_label = tk.Label(root, text="WPM: 0", font=('Arial', 12))
        self.wpm_label.pack(pady=10)
        
        self.restart_button = tk.Button(root, text="Restart", command=self.restart_test, state='disabled')
        self.restart_button.pack(pady=10)
        
        
    # Start the typing test
    def start_test(self):
        self.start_time = time.time()
        self.start_label.config(text="Type the text below:")
        self.start_button.config(state='disabled')
        self.restart_button.config(state='disabled')
        self.entry_text.delete(0, tk.END)
        self.entry_text.focus()


    # Handle key press events
    def key_press(self,event):
        typed_text = self.entry_text.get()
        
        # Calculate WPM after every key press
        if self.start_time:
            time_elapsed = max(time.time() - self.start_time, 1)
            self.wpm = round((len(typed_text) / (time_elapsed / 60)) / 5)
            self.wpm_label.config(text=f"WPM: {self.wpm}")
            
        # Check for correctness and color-code the text
        correct_text = self.target_text[:len(typed_text)]
        if typed_text == correct_text:
            self.entry_text.config(fg='green')
        else:
            self.entry_text.config(fg='red')

        # End test if the full text is typed correctly
        if typed_text == self.target_text:
            self.end_test()

    # End the typing test
    def end_test(self):
        self.start_label.config(text="Test Complete!")
        self.restart_button.config(state='normal')
        self.entry_text.config(state='disabled')

    # Restart the test
    def restart_test(self):
        self.target_text = select_text()  # Select new text
        self.text_label.config(text=self.target_text)
        self.start_time = None
        self.current_text = []
        self.wpm = 0
        self.wpm_label.config(text="WPM: 0")
        self.entry_text.config(state='normal', fg='black')
        self.entry_text.delete(0, tk.END)
        self.start_label.config(text="Press Start to begin!")
        self.start_button.config(state='normal')
        self.restart_button.config(state='disabled')


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = Typing_Speed_App(root)
    root.mainloop()


# import curses
# from curses import wrapper
# import time
# import random

# def select_text():
#     with open('text.txt','r') as f:
#         lines = f.readlines()
#         return random.choice(lines).strip()

# def start_screen(stdscr): # for introduction
#     stdscr.clear() # for making screen clean
#     stdscr.addstr('Welcome to Typing Test!') # print  to change color of text --> curses.color_pair(1)
#     stdscr.addstr('\nPress any key to start !') 
#     stdscr.refresh() # refresh the page
#     stdscr.getstr() # wait for input

# def display_text(stdscr, target, current, wpm=0): # Overlaying Text
    
#     stdscr.addstr(target) # print  to change color of text --> curses.color_pair(1)
        
#     for i, char in enumerate(current):
#         correct_char = target[i]
#         color = curses.color_pair(1)
#         if correct_char != char:
#             color = curses.color_pair(2)
#         stdscr.addstr(0,i, char, color ) 
#         stdscr.addstr(1,0, f"WPM : {wpm}")  


# def wpm_test(stdscr): # for text printing
#     target_text = "select_text()"
#     current_text = []
#     wpm=0
#     start_time = time.time()
#     stdscr.nodelay(True)
    
#     while True:
#         time_elapsed = max(time.time() - start_time, 1)
#         wpm = round(    (   len(current_text)  /   (time_elapsed/60)    )   /5 )
        
#         stdscr.clear()
#         display_text(stdscr=stdscr, target=target_text, current=current_text, wpm=wpm)
#         stdscr.refresh()
        
#         if "".join(current_text) == target_text:
#             stdscr.nodelay(False)
#             break
        
#         try:
#             key = stdscr.getkey()
#         except:
#             continue
        
        
#         if ord(key) == 27:
#             break
        
#         if key in ("KEY_BACKSPACE", '\b', "\x7f"):
#             if len(current_text) > 0:
#                 current_text.pop()
#         elif len(current_text) < len(target_text):
#             current_text.append(key)
        
       
    
    
    
    
#     # stdscr.clear() # for making screen clean
    
#     # stdscr.refresh() # refresh the page
#     stdscr.getstr() # wait for input
    
# def main(stdscr):
#     curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
#     curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
#     curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
#     start_screen(stdscr)
    
#     while True:
#         wpm_test(stdscr)
#         stdscr.addstr(2,0,"You have completed the Test.....")
#         stdscr.addstr(3,0,"Press any key to continue....")
       
#         key = stdscr.getkey()
#         if ord(key) == 27:
#             break

# wrapper(main)






# # def display_text(stdscr, target, current, wpm=0): # Overlaying Text
    
# #     stdscr.addstr(target) # print  to change color of text --> curses.color_pair(1)
# #     display_label = ttk.Label(root, text=stdscr.addstr(target))
# #     display_label.grid(row=0,column=0, sticky=tk.W),    #grid for where you want to print this label
        
# #     for i, char in enumerate(current):
# #         correct_char = target[i]
# #         color = curses.color_pair(1)
# #         if correct_char != char:
# #             color = curses.color_pair(2)
            
# #         stdscr.addstr(0,i, char, color ) 
# #         intro_label = ttk.Label(root, text=stdscr.addstr(0,i, char, color ))
# #         intro_label.grid(row=1,column=0, sticky=tk.W),    #grid for where you want to print this label
        
# #         stdscr.addstr(1,0, f"WPM : {wpm}")  
# #         intro_label = ttk.Label(root, text=stdscr.addstr(1,0, f"WPM : {wpm}"))
# #         intro_label.grid(row=2,column=0, sticky=tk.W),    #grid for where you want to print this label


# # def wpm_test(stdscr): # for text printing
# #     target_text = select_text()
# #     current_text = []
# #     wpm=0
# #     start_time = time.time()
# #     stdscr.nodelay(True)
    
# #     while True:
# #         time_elapsed = max(time.time() - start_time, 1)
# #         wpm = round(    (   len(current_text)  /   (time_elapsed/60)    )   /5 )
        
# #         stdscr.clear()
# #         display_text(stdscr=stdscr, target=target_text, current=current_text, wpm=wpm)
# #         stdscr.refresh()
        
# #         if "".join(current_text) == target_text:
# #             stdscr.nodelay(False)
# #             break
        
# #         try:
# #             key = stdscr.getkey()
# #         except:
# #             continue
        
        
# #         if ord(key) == 27:
# #             break
        
# #         if key in ("KEY_BACKSPACE", '\b', "\x7f"):
# #             if len(current_text) > 0:
# #                 current_text.pop()
# #         elif len(current_text) < len(target_text):
# #             current_text.append(key)
        
       
    
    
    
    
# #     # stdscr.clear() # for making screen clean
    
# #     # stdscr.refresh() # refresh the page
# #     stdscr.getstr() # wait for input
    
    
   
# # def main(stdscr):
# #     curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
# #     curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
# #     curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
# #     #Label
# #     intro_label = ttk.Label(root, text='Welcome to Typing Test..!\nPress any key to start !')
# #     intro_label.grid(row=0,column=0, sticky=tk.W),    #grid for where you want to print this label


# #     def continueButton():
# #         submit_button.deletecommand()
    
    

# # # Continue Button
# #     submit_button = ttk.Button(root, text='Submit', command=continueButton)
# #     submit_button.grid(row=6,column=0)

    
# #     start_screen(stdscr)
    
# #     while True:
# #         wpm_test(stdscr)
        
# #         outro_label = ttk.Label(root, text=stdscr.addstr(2,0,"You have completed the Test.....\nPress any key to continue...."))
# #         outro_label.grid(row=0,column=0, sticky=tk.W),    #grid for where you want to print this label
# #         stdscr.addstr(2,0,"You have completed the Test.....")
# #         stdscr.addstr(3,0,"Press any key to continue....")
       
# #         key = stdscr.getkey()
# #         if ord(key) == 27:
# #             break
# #         root.mainloop()   