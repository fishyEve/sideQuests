from taipy.gui import Gui  # The main GUI class for creating and displaying the application
import taipy.gui.builder as tgb # The builder module for constructing the GUI components
from math import cos, exp

value = 10 # Initial value set to 10, this will be used to compute the data and display it in the GUI

def compute_data(decay:int)->list: # Function to compute data based on the decay value
    # Generate a list of values by applying the formula cos(i/6) * exp(-i * decay / 600) for i in range(100)
    return [cos(i/6) * exp(-i*decay/600) for i in range(100)]

def on_slider(state): # Function that is triggered when the slider value changes
    # Update the 'data' state with the computed data based on the current value of the slider
    state.data = compute_data(state.value)
  
# Create the page layout using the Taipy builder (tgb)
with tgb.Page() as page:
    tgb.text(value="# Taipy- Is this working?", mode="md") # Add a markdown header with text, since I've never done this stuff before
    tgb.text(value="Value: {value}") # Display the current value of the slider
    tgb.slider(value="{value}", on_change=on_slider) # Add a slider that binds to 'value' and calls on_slider when changed
    tgb.chart(data="{data}") # Add a chart that displays the computed data

# Compute the initial data with the starting value of 10 (value = 10)
data = compute_data(value)

# Create and run the Taipy GUI with the constructed page layout and set the window title to "Dynamic chart"
if __name__ == "__main__":
    Gui(page=page).run(title="Dynamic chart")
