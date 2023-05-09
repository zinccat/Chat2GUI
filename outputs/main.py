from nicegui import ui

# create a label to display the result
result = ui.label(text='0')

# create an input field for the user to input the calculation
calculation = ui.input(label='Enter calculation:', placeholder='e.g. 2+2')

# create a function to evaluate the calculation and update the result label
def evaluate_calculation():
    try:
        result.set_text(str(eval(calculation.value)))
    except:
        result.set_text('Error')

# create a button to evaluate the calculation
ui.button(text='Calculate', on_click=evaluate_calculation)

# create a reset button to clear the input and result
def reset():
    calculation.set_value('')
    result.set_text('0')

ui.button(text='Reset', on_click=reset)

ui.run()