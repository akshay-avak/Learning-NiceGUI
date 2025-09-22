from nicegui import ui

ui.label("Welcome Back Agent 47")
ui.link("Goto google search","https://www.google.com/")

ui.chat_message("Hello Good Morning",name="Akshay",stamp="now",avatar="https://robohash.org/XG4.png?set=set1&size=150x150")


ui.chat_message("Hello Good Morning",name="Akshay",stamp="now",avatar="https://robohash.org/V67.png?set=set1&size=150x150",sent=True)


ui.markdown("This is some **Bold Markdown Text**.")


ui.mermaid('''
graph LR;
           A-->B-->C
           A-->D-->C
 ''')

ui.html('This is some <strong>HTML</strong> text using html tags in the python code.')

ui.run()